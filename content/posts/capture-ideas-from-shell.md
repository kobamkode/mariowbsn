+++
author = 'Mario Wibisono'
date = '2026-10-15T00:00:00+07:00'
draft = false
title = 'Capture Ideas from the Shell'
summary = 'A thought arrives while I am working in the terminal. Writing it down used to cost a round trip to Obsidian. capture became the front door of my Obsidian workflow instead.'
description = 'A thought arrives while I am working in the terminal. Writing it down used to cost a round trip to Obsidian. capture became the front door of my Obsidian workflow instead.'
tags = ['pkm', 'cli', 'go', 'obsidian']
+++

The thought arrives while I am in the middle of something. A fix I want to try later, a task that I need to complete, an idea worth keeping. I have a daily note in Obsidian for exactly this. Writing it means I leave the terminal, open Obsidian, find today's note, type one sentence, switch back. Ten seconds of work that has nothing to do with the problem I am solving.

## Why I built it

What I actually needed was one line on disk, appended to today's file. Not a capture app, not a plugin suite. Just an append. I do not work in Obsidian. I work in a terminal all day, with shells, editors, and logs. When I need to write one sentence down, the shell is already in front of me and everything else is behind it.

So I built [capture](https://github.com/kobamkode/capture), a small Go binary that appends to today's daily note, and every design decision follows from that single job. There is no daemon, no database, no background process. Each invocation reads the environment, opens the file, appends, and exits.

It is configured with three environment variables. `CAPTURE_VAULT` points at the vault and fails when unset. `CAPTURE_DAILY_DIR` selects the folder for daily notes. `CAPTURE_DAILY_FORMAT` takes a Go time layout for the filename. I keep them in an alias in my shell rc, so `capture` works anywhere I open a terminal.

## In practice

Everything I do with it comes in three forms.

```
$ capture i think i need to learn math
$ capture -t go to dentist
$ cat ideas.txt | capture
```

The first form writes a note with a local timestamp, like `- 09:15 | i think i need to learn math`. The second writes a task as an unchecked checkbox. The third reads stdin and writes one entry per non-empty line, which is how I empty a scratch file after a long session.

Each run appends to today's daily note and creates it when missing. When the date rolls over, the next capture starts the new day's file. The file ends up looking like this.

```
- 09:15 | i think i need to learn math
- [ ] go to dentist
- 09:20 | remember the milk
```

## The front door of my Obsidian workflow

Capture is not a side tool that happens to write Markdown. It is the front door of the whole vault. Every note and every task enters Obsidian through the shell now, in one line, without breaking flow. When a thought arrives I do not decide whether it is worth the round trip anymore. There is no round trip, so it goes in.

That changed what Obsidian is for. It stopped being where I capture and became where I read and organize. During weekly review I open the vault, skim the days, and move what matters into real notes and links. The vault fills itself from the terminal while I work, and the review has something to work with.

The friction is gone because the tool moved to where the problem is. The thought never leaves the terminal, so neither do I.

Install it with `go install github.com/kobamkode/capture@latest`.

Source and docs live at [github.com/kobamkode/capture](https://github.com/kobamkode/capture).
