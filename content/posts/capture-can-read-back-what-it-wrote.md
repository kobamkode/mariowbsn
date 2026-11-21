+++
author = 'Mario Wibisono'
date = '2026-11-21T00:00:00+07:00'
draft = false
title = 'Capture Can Read Back What It Wrote'
summary = 'Capture started as an append. A month of daily use moved the friction from writing to finding, so it grew capture ids, timestamps on tasks, a listing mode, and capture open.'
description = 'Capture started as an append. A month of daily use moved the friction from writing to finding, so it grew capture ids, timestamps on tasks, a listing mode, and capture open.'
tags = ['pkm', 'cli', 'go', 'obsidian']
+++

When I wrote about [capturing ideas from the shell](/posts/capture-ideas-from-shell/), capture had one job: append a line to today's daily note. That job held up. I use it every day, and the writing side never got in the way.

What got in the way was everything after writing. A line lands in the vault and then I cannot point at it. I cannot see it again without opening Obsidian. The tool solved the capture and left the recall unsolved, so six versions later it does both.

## Every capture has an id

```
- 09:15 | 0b17a3b | i think i need to learn math
```

Seven hex characters between pipes, the shape of a git short hash. It exists so a single line can be called back: grep the vault for it, or hand it to an agent with a sentence like "explore `0b17a3b` in the journal". Without an id, a capture is only findable by remembering words close enough to grep for, which defeats the point of writing it down.

Ids are random and collisions are left to chance. Twenty-eight random bits across one day's file make a duplicate vanishingly unlikely, and a dedupe scan would cost a re-read on every capture for a problem that does not happen.

Tasks picked up the id too, and while I was there they picked up the timestamp they were missing.

```
- [ ] | 09:16 | b7e4f21 | go to dentist
```

A bare checkbox does not say when it was written, so it sorted wrong against every note around it. Notes and tasks now share the same `time | id | text` tail; only the opening column differs.

## Reading the day back

```
$ capture -l
- 09:15 | 0b17a3b | i think i need to learn math
- [ ] | 09:16 | b7e4f21 | go to dentist
- 09:20 | 3c9d0ae | remember the milk
```

`-l` prints today's captures verbatim, in file order. A day with nothing captured prints nothing and exits 0, so it is safe in a script or a prompt. It refuses text, stdin, and `-t`, so a command I fumbled fails loudly instead of quietly dropping the words I typed.

`-w` widens it to the past week. The last seven notes, oldest day first, each under a `## YYYY-MM-DD` heading, days with no captures skipped.

```
$ capture -l -w
## 2026-10-13
- 08:00 | e02f7d9 | yesterday note
- [ ] | 18:30 | 1d3b6a4 | dentist tomorrow

## 2026-10-14
- 09:15 | c48e5f0 | today note
```

This is the part I did not expect to use as much as I do. Weekly review used to start with opening Obsidian and skimming files. Now it starts with one command in the terminal where I already am, and Obsidian is for what happens after I decide something is worth keeping.

## Opening the day

```
$ capture open
```

`capture open` opens today's note in Obsidian, creating an empty file first when the day has none. It is the one command for the moment the shell ran out and the vault is where the work is. It hands an `obsidian://open` URI to the desktop with the absolute path, so a vault display name that does not match its folder does not matter.

`open` had to become a reserved word: it is a command only as the first argument, and `capture -- open` still captures the word itself.

## What did not change

Still one binary. Still no daemon, no database, no background process. Each invocation reads the environment, opens the file, and exits. Captures only ever append; listing only reads; `open` only creates a missing file and launches a URI. The three environment variables and the append-only shape survived every one of these changes, which is why they were cheap to make.

`capture --version` reports the version baked in by the Go toolchain, so releases are just git tags and updating is the install command again:

```sh
go install github.com/kobamkode/capture@latest
```

The loop is closed now. I write from where I am, I read from where I am, and I open the vault when I am organizing. The thought never leaves the terminal unless I decide it should.

Source and docs live at [github.com/kobamkode/capture](https://github.com/kobamkode/capture).
