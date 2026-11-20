---
title: "annotate.nvim"
description: ""
date: "2026-11-20T11:24:15Z"
github_url: "https://github.com/clobrano/annotate.nvim"
stars: 1
forks: 0
language: "Lua"
topics:
  []
---

# annotate.nvim

Leave annotations on exact pieces of code, then hand them to an AI agent as one markdown block, with a quote of the code and a link to where it is.

- Annotate a **character selection** (`v`), whole lines (`V`), or the cursor line
- Annotations find their code again after the file changed: the annotated text is stored and searched for when the buffer opens. While the buffer is open they follow your edits.
- Export to the clipboard, a file, or a tmux pane (pasted with bracketed paste, so agent CLIs take it as one input)
- Works in [gh-review.nvim](https://github.com/gh-tui-tools/gh-review.nvim) diff buffers: the source becomes a GitHub link at the PR commit
- No dependencies. Neovim 0.9+.

## Export format

````markdown
## Annotations (2)

* NOTE #1:
  > ```go
  > r.Client.Update(ctx, obj)
  > ```
  > source: pkg/reconcile.go:4:12-4:36

  Should be a Patch: Update conflicts with the status writer.

* NOTE #2:
  > ```go
  > Timeout *metav1.Duration
  > ```
  > source: https://github.com/org/repo/blob/3f2a9c1/api/v1/types.go#L40

  Is a default needed here?
````

Source formats:

| Annotation | Source |
|---|---|
| characters | `path:line:col-line:col` (1-based, end inclusive) |
| lines | `path:line` or `path:start-end` |
| buffer with no file on disk (gh-review) | `https://<host>/<owner>/<repo>/blob/<sha>/<path>#L<start>-L<end>` |

Paths are relative to the git root of the file itself, not to Neovim's working directory.

## Installation

```lua
{
  "clobrano/annotate.nvim",
  keys = {
    { "<leader>aa", function() require("annotate").add() end, mode = { "n", "x" }, desc = "Annotate" },
    { "<leader>ae", function() require("annotate").edit() end, desc = "Annotate: edit" },
    { "<leader>ad", function() require("annotate").delete() end, desc = "Annotate: delete" },
    { "<leader>al", function() require("annotate").list() end, desc = "Annotate: list" },
    { "<leader>ax", function() require("annotate").export("tmux") end, desc = "Annotate: send to agent pane" },
    { "<leader>ay", function() require("annotate").export() end, desc = "Annotate: copy" },
    { "]a", function() require("annotate").jump(1) end, desc = "Next annotation" },
    { "[a", function() require("annotate").jump(-1) end, desc = "Previous annotation" },
  },
  event = "VeryLazy", -- so existing annotations show when files open
  opts = {},
}
```

Map visual-mode keys with a Lua function as above, not with `:`: the function sees the live selection, including its columns.

## Commands

```vim
:Annotate [add]          " annotate the selection or the cursor line (:'<,'>Annotate add for a range)
:Annotate edit           " edit the annotation under the cursor
:Annotate delete         " delete the annotation under the cursor
:Annotate list           " all annotations of the project in the quickfix list
:Annotate export [clipboard|file|tmux]
:Annotate preview        " show the export in a split
:Annotate clear          " archive and remove all annotations of the project
:Annotate! export        " same as export, but only the current buffer's annotations
:Annotate! preview       " same as preview, but only the current buffer's annotations
```

With `clear_after_export`, the bang variants archive and remove only the
exported annotations, not the whole project's.

Exporting to tmux shows the annotation count before anything is sent: the
pane picker prompt includes it, and a configured `tmux.target` gets a
confirm dialog first, so old forgotten annotations don't slip through.

When several annotations overlap, edit and delete act on the smallest one under the cursor.

In the popup: `<C-s>` saves, `q` or `<Esc>` cancels.

## Configuration

Defaults:

```lua
require("annotate").setup({
  label = "NOTE", -- on the box, and items start with "* NOTE #1:"
  display = {
    box = true,
    sign = true,
    icon = "▍",
    hl = "DiagnosticInfo", -- sign and box
    range_hl = "DiagnosticVirtualTextInfo", -- the annotated text
    wrap = 60, -- wrap the comment box text at this display width; false = never wrap
  },
  popup = { width = 70, height = 6, border = "rounded", submit = "<C-s>", cancel = "q" },
  data_dir = vim.fn.stdpath("data") .. "/annotate",
  export = {
    header = "## Annotations (%d)", -- or false
    format = nil, -- function(annotation, index) -> string
    clear_after_export = false,
    file = ".annotations.md", -- relative to the project root
    register = "+",
  },
  tmux = {
    target = nil, -- e.g. "{last}"; nil picks from the panes of the session
    submit = false, -- press Enter after pasting
  },
  resolvers = {},
})
```

### Custom export format

`export.format` gets each annotation and its number:

| Field | Meaning |
|---|---|
| `text` | the comment |
| `code`, `lang` | annotated text and filetype |
| `path`, `url` | path, and web link for buffers with no file |
| `lnum`, `col`, `end_lnum`, `end_col`, `linewise` | position (lines 1-based, columns 0-based bytes, end exclusive) |

`require("annotate.export").source(a)` returns the source string, and `require("annotate.export").format(a, i)` is the default formatter.

### Resolvers

A resolver tells annotate.nvim what a buffer that is not a file is. Return nil to pass:

```lua
resolvers = {
  function(bufnr)
    local path = vim.api.nvim_buf_get_name(bufnr):match("^myplugin://(.+)$")
    if path then
      return {
        root = require("annotate.source").cwd_root(), -- project the annotation belongs to
        key = path, -- unique id of this content in the project
        path = path,
        url = nil, -- link without "#L.." if the agent can't read the file locally
      }
    end
  end,
}
```

## Storage

One JSON file per project root in `data_dir`. `:Annotate clear` (and `clear_after_export`) moves it to `data_dir/archive/`.

If an annotation's text can't be found when the buffer opens, it stays where it was and its box says "text not found".

## Tests

```sh
nvim --headless -u NONE -c "luafile tests/run.lua"
```
