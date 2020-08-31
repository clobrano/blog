---
date: "2013-01-01T00:00:00Z"
excerpt: What do you expect to receive from an empty queue?
draft: false
share: true
tags:
- python
title: The std queue's long memory
---


I wrote this just like a note of something unexpected I noticed few days ago.

The subject of this post is the [C++ std::queue](http://www.cplusplus.com/reference/queue/queue/). It's usage is pretty simple, it represents a FIFO queue, with standard APIs ''push'' and ''pop'' to insert and remove elements, ''front'' to get the first element from the queue and a ''size' method to get the number of stored elements (there is also a back API, to get the last, but it does not matter now).

The fact
--------

What do you expect to receive if you try to get an element from an empty queue?

Well, the answer here is "it depends". In fact it depends on the signature of the `std::queue::front` method, which is the following:

```cpp
const value_type& front ( ) const;
```

where the ''value_type'' is the type defined for the container, let's say an integer.

```cpp
const int& front ( ) const;
```

With this signatore calling ''front'' from a empty queue we could have a negative value, zero or whatever, but in any case it would be a valid value, that is something that we could have pushed into the queue before, instead of an error value.

Avoiding any mistake here is pretty simple: test the emptyness of the queue

```cpp
if(myQueue->empty() == false)
{
    value = myQueue->front()
}
```

but just for curiosity what is the actual value returned? It turns out that it returns a value __previously stored and already removed from the queue!__

I wrote this simple test to show what happens :)

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main()
{
    queue<int>* myQueue = new queue<int>();

    cout << "Queue start size (0 expected) = " << myQueue->size() << endl;
    cout << "Queue start front element (0 expected) = " << myQueue->front() << endl;

    int base = 33330000;

    /* Just some normal push and N pop */
    for(int i = 0; i < 1000; i=i+2)
    {
        myQueue->push(base + i);
        myQueue->pop();
    }

    /*
     * At this point the size of the queueu is 0 again as expected, BUT if you ask
     * for the FRONT element from the queue, you will get one of the values
     * previously inserted and already removed!
     */
    cout << "Queue size (0 expected) = " << myQueue->size() << endl;
    cout << "Queue front element (0 expected) = " << myQueue->front() << endl;

    /*
     * A sequence of other pop and front will return other values inserted previously
     * while the queue becomes an invalid number.
     * WARNING: a sequence of pop on an empty queue will cause a segmentation fault :)
     */
    myQueue->pop();
    cout << "Empty queue size after pop (0 expected) = " << myQueue->size() << endl;
    cout << "Empty queue front element (0 expected) = " << myQueue->front() << endl;

    return 0;
}
```

this is the ouput

```sh
Queue start size (0 expected) = 0
Queue start front element (0 expected) = 0
Queue size (0 expected) = 0
Queue front element (0 expected) = 33330488
Empty queue size after pop (0 expected) = 4294967295
Empty queue front element (0 expected) = 33330490
```

