---
date: "2013-07-28T00:00:00Z"
excerpt: Fun with overflows
draft: false
share: true
tags:
- python
title: What Goes Around, Comes Around
---

Few weeks ago I begun the [Udacity](https://www.udacity.com/)'s course **Software Testing**. The course covers the basics of software testing (you don't say? :D) and it is pretty good since there are video lessons and exercises, quizes to put yourself to the test.

In one of the quizes, as part of a bigger problem (implement the [Luhn Checksum](http://en.wikipedia.org/wiki/Luhn_algorithm)<a rel="nofollow" href="#footnote1" id="ref_footnote1"><sup>1</sup></a> algorithm), I needed to convert an integer number into a list, that is not a big problem actually, but the implementation gave me a little surprise.

The idea is

* divide the number by 10
* push the decimal part into the list
* take the integer part
* repeat all until the integer part is over

The following is the code

{{< highlight python >}}
def num2list(n):
    lst = []
    while int(n) != 0:
        n = int(n) / 10.0
        # This extracts only the decimal part (e.g. 123.4 - 123 == 0.4)
        dec = int((n - round(n)) * 10.0)
        lst.append(dec)
    return lst

if __name__ == '__main__':
    print num2list(1234)
{{< / highlight >}}

surprisingly the result of the test was '[1,1,3,4]'. What happened to the number '2'?

To better understand the behavior of the code, I added just one print

{{< highlight python >}}
def num2list(n):
    lst = []
    while int(n) != 0:
        n = int(n) / 10.0
        dec = int((n - round(n)) * 10.0)
        lst.append(dec)
        print('n=%1.1f, round(n)=%1.1f, [(n-round(n)) x 10]=%1.1f, dec=%d' %
               (n, round(n), (n-round(n)) * 10, dec))
    return lst[::-1]  # This is for reverse the list
{{< / highlight >}}

the following is the new output

    n=123.4, round(n)=123.0, [(n-round(n)) x 10]=4.0, dec=4
    n=12.3, round(n)=12.0, [(n-round(n)) x 10]=3.0, dec=3
    n=1.2, round(n)=1.0, [(n-round(n)) x 10]=2.0, dec=1
    n=0.1, round(n)=0.0, [(n-round(n)) x 10]=1.0, dec=1
    [1, 1, 3, 4]

Ok I know, the output is not very clear, however we can see that the implementation worked well for each iteration except for the third, when the number '2' was expected to be extracted, and not the number '1'. In fact at the third step, when n=1.20, the value of the following expression

    [(n-round(n)) x 10] =
    = [(1.2 - 1.0) * 10.0]

is equal to '2.0' as expected, but the value of the variable 'dec' (just the integer part of the previous result) became '1' out of the blue (or so it seemed)!
It took me a little time to figure out the problem (basically to be sure that the fault was not in the code), but then I got it: the approximation!
Actually the debug message prints '2.0' approximating to **the closer value**, while the actual value is something like 1.9999999999..., so taking only the integer part result in having just '1'.
The fix is to apply the operator 'int' to the 'round' approximation of '[(n-round(n)) x 10], that by definition (see [here](http://docs.python.org/2/library/functions.html#round)).

> Values are rounded to the closest multiple of 10

so this is the final function

{{< highlight python >}}
def num2list(n):
    print n
    lst = []
    while int(n) != 0:
        n = int(n) / 10.0
        dec = int(round((n - round(n)) * 10.0))
        if dec < 0:
            dec = 10 - abs(dec)
        lst.append(dec)
    return lst[::-1]
{{< / highlight >}}

When a non negative check of 'dec' has been added to cope with the numbers > 5

    Without the check if n = 1.6
    round(n) = 2.0 (instead of 1.0)
    n - round(n) = -0.4 (instead of 0.6) and dec == 4

    With the check since dec is negative (-4)
    dec = 10 - 4 = 6 OK!

 an alternative would be

{{< highlight python >}}
if round(n) > n:
    dec = round(n) - n...
else:
    dec = n - round(n)...
{{< / highlight >}}

#### Footnotes
1. The test warned to avoid checking Wikipedia about the Luhn algorithm because in the same page there is a (really better than mine :D) python example <a rel="nofollow" href="#ref_footnote1" id="footnote1">[↩]</a>.

