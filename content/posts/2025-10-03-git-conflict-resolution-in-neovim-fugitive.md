---
title: "Git Conflict Resolution in Neovim Fugitive"
date: 2025-10-03T19:50:43+02:00
draft: false
---

# Neovim Workflow: Mastering Git Conflict Resolution

This is mostly a "note to myself" kind of post, to celebrate my win against my own laziness.

For a long time I used Fugitive’s excellent 3-way diff, typically accessed via `:Gvdiffsplit!` with satisfaction, however, my common friction point was the back-and-forth between the editor and the terminal to run `git status` just to find the next file.

I knew there was a much simpler integrated workflow, but only today I took the time to find it :).

## 1. The Actionable Status List

The key to efficiency is recognizing that Fugitive's status buffer (`:Git`) is a complete, live list of your Git state that allows immediate interaction.

1.  **Get the List:** Run the primary Fugitive command:

    ```vim
    :Git
    ```

    This displays your files, including all those marked as **`Unmerged`** (U).

2.  **Jump and Diff:** Instead of manually typing filenames, simply navigate your cursor to an unmerged file and press:

    ```
    dv
    ```

    This executes a vertical split diff (`:Gvdiffsplit!`), immediately showing the 3-way view (Local, Merged, Remote) for the file under the cursor.

## 2. Resolving Conflicts

Now it is just a matter to use the split diff view and resolve the conflicts.

To resolve just the difference block your cursor is currently on, use the following commands:

  * **Jump Next/Previous Hunk:** `]c` / `[c`
  * **Accept Hunk from Local:** Run `:diffget //2`
  * **Accept Hunk from Remote:** Run `:diffget //3`


When you want to accept one version of the file completely, instead, you must tell the command to act on the **entire range** (`%`). This is done by prefixing the command with `:%`.

| Action | Command (Uses Fugitive's Buffer Suffix) |
| :--- | :--- |
| **Accept All Local (Ours)** | `:%diffget //2` |
| **Accept All Remote (Theirs)** | `:%diffget //3` |

***Note on Buffers:*** The suffixes `//2` and `//3` reliably identify the Local and Remote buffers created by Fugitive, replacing the need for ambiguous buffer numbers or long file names.

## 3\. Staging and Completing the Task

After you've finished resolving a file, move back to **`:Git`** status buffer. The file is now clean but remains unstaged. To mark the resolution as complete, simply hit:

```
s
```

**`s`** (for Stage) executes `git add <file>`, moving the file out of the `Unmerged` or `Unstaged` list. You can immediately move the cursor down to the next conflicted file, maintaining a fast, seamless flow entirely within Neovim.

