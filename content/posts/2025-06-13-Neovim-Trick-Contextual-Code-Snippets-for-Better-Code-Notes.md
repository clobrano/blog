---
title: "Neovim custom function: Contextual Code Snippets for Better Code Notes"
date: 2025-06-13T16:45:37+02:00
draft: false
---

As developers, we're constantly sifting through code, often needing to capture snippets and their context for personal notes, team discussions, or future reference. Copy-pasting code is straightforward, but quickly losing track of its exact origin can be a real headache. I found myself wishing for a faster way to grab a code selection and its precise remote link (like a GitHub permalink), formatted just right.

So, I tinkered around and came up with this small Neovim function. It's nothing groundbreaking, but it has genuinely streamlined my personal note-taking workflow. When I select a block of code, I just call this function. Here's what it does for me:

1.  **Yanks the selected code:** It grabs the exact lines I've highlighted.
2.  **Generates a remote link:** By leveraging the well-known Tim Pope's [fugitive](https://github.com/tpope/vim-fugitive) plugin, it automatically creates a permalink to that specific code selection in its hosted repository.
3.  **Formats and stores:** It combines the code and its link into a clean Markdown code block, with the link as a comment. This entire formatted output then lands in my system clipboard, ready to be pasted wherever I need it.

For instance, during a code review, I can quickly select a block, run this function, and paste a perfectly contextualized snippet with its exact source link into my markdown document. It cuts down on manual link hunting and helps ensure my notes are always precise. Perhaps this idea could be a starting point for your own Neovim note-taking enhancements!

{{< youtube uJdZoMiXjZQ >}}


Here is the full code
```lua
function CopyCodeAndPermalink()
  -- Yank current selection in z register
  vim.cmd('normal! `<v`>"ay')
  local saved_selection = vim.fn.getreg('a')
  -- Get Remote link of the selection
  vim.cmd("'<,'>GBrowse!")
  local link = vim.fn.getreg('+')
  -- Get the current filetype
  local filetype = vim.bo.filetype
  local allowed_filetypes = {
    ["c"] = true,
    ["cpp"] = true,
    ["sh"] = true,
    ["go"] = true,
    ["lua"] = true,
    ["python"] = true,
  }
  local output = ""
  if allowed_filetypes[filetype] then
    output = output .. "```" .. filetype .. "\n"
  end
  output = output .. "// " .. link .. "\n"
  output = output .. saved_selection .. "\n"
  output = output .. "```"
  vim.fn.setreg('+', output)
end
```
