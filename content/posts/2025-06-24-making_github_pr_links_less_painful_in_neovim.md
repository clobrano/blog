---
title: "Making Github PR links less painful in Neovim"
date: 2025-06-24T16:26:37+02:00
draft: false
---

As developers, many of us keep some form of journal or notes to track our daily work, and Markdown is often the format of choice. When I'm jotting things down, I frequently include web links. Markdown offers a couple of ways to handle these: either inline like `[label](https://actuallink.com)` or as a reference link, where you use `[label]` in the text and define `[label]: https://actuallink.com` somewhere else, usually at the bottom of the page.

I've grown to prefer the latter, mostly for two simple reasons. First, Neovim can sometimes get a little messy with long inline links, especially when lines wrap. Second, and perhaps more importantly, reference links let me use the same `[label]` multiple times without needing to rewrite the full URL every single time. It's a small win, but it adds up!

The downside, though, is that manually writing out those reference links can be pretty tedious. This is especially true for structured links, like those to GitHub Pull Requests. So, as often happens, I ended up tinkering in Neovim and came up with a little function to streamline this process, particularly for GitHub PRs.

It's not a perfect, bulletproof solution for every link under the sun, but it has genuinely been a huge help for my personal workflow recently. Essentially, I copy a GitHub PR link to my clipboard, run this function, and it automatically creates the Markdown reference at the bottom of my current file and inserts the readable label where my cursor is.

Here’s the little snippet that does the trick for me:

```lua
function FromGithubLinkToMarkdownPRRef()
  -- e.g. https://github.com/<org>/<project>/pull/<number>
  -- will be converted to [<org/<project> PR<number>]
  -- and a Markdown reference link will be created at
  -- the end of the buffer like below:
  -- [<org/<project> PR<number>]: https://github.com/<org>/<project>/pull/<number>

  local github_link = vim.fn.getreg('+') -- Get content from the system clipboard
  if not github_link or github_link == '' then
    vim.notify("Clipboard is empty.", vim.log.levels.WARN, { title = "GitHub Link" })
    return
  end

  -- Regex to extract organization, project, and PR number
  local pattern = "https://github.com/([^/]+)/([^/]+)/pull/(%d+)"
  local org, project, pr_number = string.match(github_link, pattern)

  if not (org and project and pr_number) then
    vim.notify("Clipboard content is not a valid GitHub PR link.", vim.log.levels.ERROR, { title = "GitHub Link" })
    return
  end

  local markdown_label = string.format("[%s/%s PR%s]", org, project, pr_number)
  local markdown_ref = string.format("[%s/%s PR%s]: %s", org, project, pr_number, github_link)

  local bufnr = vim.api.nvim_get_current_buf()
  local last_line = vim.api.nvim_buf_line_count(bufnr)

  -- Insert the markdown reference at the end of the buffer.
  vim.api.nvim_buf_set_lines(bufnr, last_line, last_line, false, {markdown_ref})

  -- Insert the markdown label at the current cursor position
  -- 'c' for character-wise insert, 'false' for inserting before cursor, 'true' for moving cursor to end of paste
  vim.api.nvim_put({markdown_label}, "c", false, true)

  vim.notify("GitHub PR link converted and reference added.", vim.log.levels.INFO, { title = "GitHub Link" })
end
```

Here instead a short video showing what it actually does :D

{{< youtube 8BUv8hV5LBc >}}

