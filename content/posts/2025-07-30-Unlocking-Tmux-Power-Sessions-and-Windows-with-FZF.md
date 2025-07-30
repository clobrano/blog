---
title: "Unlocking Tmux Power: Sessions and Windows with FZF"
date: 2025-07-30T15:31:10+02:00
draft: true
---

Last week, I made a small change to my tmux configuration. I added some display-popups to show my sessions and windows, using `fzf` for fuzzy finding and a preview feature. At first, I thought this would just be a nice little improvement to my setup.

Before this change, I used tmux with a single session for all my open projects and contexts. I would just create many windows within that one session, and honestly, it often became a bit of a mess. Finding what I needed was sometimes tricky, and it felt disorganized.

But then, something clicked. Having quicker access to sessions and a clear preview of their content was a huge discovery for me. Now, I can separate my work contexts much better. Each project or task gets its own session. This simple change has made working with tmux sessions genuinely enjoyable.

It's important to say that tmux sessions and windows are always there by default. They are core features. But for me, the default way to access and switch between them felt a bit hidden or less intuitive. This prevented me from using them to their full potential. The quick, visual access provided by the pop-ups transformed how I interact with tmux, making these powerful features easy to use and a real game-changer for my workflow.

Here are the lines I added to my `tmux.conf` to make this happen:

```tmux
bind-key -r C-s display-popup -E "tmux list-sessions -F '#{session_name}' | fzf --preview 'tmux list-windows -t {}' | xargs tmux switch-client -t"
bind-key -r C-w display-popup -E "tmux list-windows -F '#{window_name}' | fzf --preview 'tmux capture-pane -t {} -p' | xargs tmux select-window -t"
```

The first line binds `Ctrl-s` to a popup that lists all tmux sessions. I can use `fzf` to filter them, and it shows a preview of the windows within the selected session. When I pick one, it switches me to that session.

The second line does something similar for windows. `Ctrl-w` brings up a popup with all windows across all sessions, also using `fzf` with a preview. The preview shows the content of the window, which is super helpful. Selecting a window takes me right to it.

These small additions have made a big difference in how I manage my terminal environment.
