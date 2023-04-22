+++
title = "Smart Dates in Obsidian With Espanso"
date = 2023-04-22T17:48:33+02:00
tags = ["Obsidian", "Espanso"]
draft = false
+++

I use some plugins in [Obsidian](https://obsidian.md/) to help me keep track of job tasks.
It is a combination of Templater, Tasks, Dataview, and MetaEdit. The latter is handy for editing frontmatter from a Dataview table without opening the file itself; however, when I want to set dates, there is no helper (i.e., calendar or smart date parsing, something like "input: next week, output: 2023-04-13").
I already use [Espanso - A Privacy-first, Cross-platform Text Expander](https://espanso.org/) to set today's date, but knowing that the Linux `date` built-in binary can do smart dates pretty quickly, I looked into the documentation of Espanso to create a bridge between the text editor (this time Obsidian) and the shell.
It was relatively easy.

On a shell the command is simply
```bash
date -d "next week" +%F  # +%F is the format YYYY-MM-DD
```

The Expanso configuration is
```yaml
  - regex: ";(?P<smart>.*);"
    replace: "{{output}}"
    vars:
      - name: output
        type: shell
        params:
          cmd: "date -d \"{{smart}}\" +%F"
```

So, when I type `;next week;` in Obsidian[^1] I get a smart generated date


[^1]: Well, in any text editor i use :)


