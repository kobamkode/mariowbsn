+++
author = 'Mario Wibisono'
date = '2026-11-21T00:00:00+07:00'
draft = false
title = 'Capture Can Read Back What It Wrote'
summary = 'Capture started as an append. A month of daily use moved the friction from writing to finding, so it grew capture ids, timestamps on tasks, a listing mode, a find command, and capture open.'
description = 'Capture started as an append. A month of daily use moved the friction from writing to finding, so it grew capture ids, timestamps on tasks, a listing mode, a find command, and capture open.'
tags = ['pkm', 'cli', 'go', 'obsidian']
+++

When I wrote about [capturing ideas from the shell](/posts/capture-ideas-from-shell/), capture had one job: append a line to today's daily note. That job held up. I use it every day, and the writing side never got in the way.

What got in the way was everything after writing. A line lands in the vault and then I cannot point at it. I cannot see it again without opening Obsidian. The tool solved the capture and left the recall unsolved, so seven versions later it does both.

## Every capture has an id

```
- 09:15 | 0b17a3b | i think i need to learn math
```

Seven hex characters between pipes, the shape of a git short hash, so a single line can be called back. Say `capture find 0b17a3b`, or hand the same token to an agent: "explore `0b17a3b` in the journal".

An id beats a phrase for both jobs. Words are for the human reading the line back; the id is for anything that has to find it later. A phrase only greps if I remember it close enough, and it can match several lines at once. The id is one exact token: `find` returns the line, and the same token can be handed to an agent as the next piece of work, so a capture can be acted on without being retyped.

Ids are random and collisions are left to chance. Twenty-eight random bits across one day's file make a duplicate vanishingly unlikely, and a dedupe scan would cost a re-read on every capture for a problem that does not happen.

Tasks picked up the id too, and while I was there they picked up the timestamp they were missing.

```
- [ ] | 09:16 | b7e4f21 | go to dentist
```

A bare checkbox does not say when it was written, so it sorts wrong against every note around it. Notes and tasks now share the same `time | id | text` tail; only the opening column differs.

## Calling a capture back

```
$ capture find 0b17a3b
/home/mario/vault/journal/daily/2026-10-13.md:4:- 09:15 | 0b17a3b | i think i need to learn math
```

`find` reads every daily note, not just today's, and prints each matching line as `path:line:text`, oldest day first. Grep was the first answer, and it worked because the vault is only Markdown and I knew where the days lived. `find` does the same lookup without that knowledge: it reads only files named by `CAPTURE_DAILY_FORMAT`, so unrelated notes cannot supply a hit and a misconfigured directory is not swept.

Matching is on the id column, not the text, so a capture that happens to mention another id does not shadow the real line. A task you ticked off in Obsidian still matches too: the checkbox changed, the id did not.

A malformed id fails before the vault is read, so a truncated paste says so instead of quietly matching some other line. A well-formed id with no match prints nothing and exits 0, the same as an empty listing.

## Reading the day back

```
$ capture -l
- 09:15 | 0b17a3b | i think i need to learn math
- [ ] | 09:16 | b7e4f21 | go to dentist
- 09:20 | 3c9d0ae | remember the milk
```

`find` answers "where is this one thing"; `-l` answers "what did I write today".

`-l` prints today's captures verbatim, in file order. A day with nothing captured prints nothing and exits 0, so it is safe in a script or a prompt. It refuses text, stdin, and `-t`, so a command I fumbled fails loudly instead of quietly dropping the words I typed.

`-w` widens it to the past week: the last seven notes, oldest day first, each under a `## YYYY-MM-DD` heading, days with no captures skipped.

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

`capture open` opens today's note in Obsidian, creating an empty file first when the day has none. It is the command for the moment the shell runs out and the vault is where the work is. It hands an `obsidian://open` URI to the desktop with the absolute path, so a vault display name that does not match its folder does not matter.

`open` had to become a reserved word: it is a command only as the first argument, and `capture -- open` still captures the word itself.

## What did not change

Still one binary. Still no daemon, no database, no background process. Each invocation reads the environment, opens the file, and exits. Captures only ever append; listing and `find` only read; `open` only creates a missing file and launches a URI. The three environment variables and the append-only shape survived every one of these changes, which is why these changes were cheap.

`capture --version` reports the version baked in by the Go toolchain, so releases are still just git tags and updating is the install command again:

```sh
go install github.com/kobamkode/capture@latest
```

The tags are cut for me now. A workflow runs the tests on every push to `main` and tags the next version from the commit subjects since the last tag: a `feat:`, or a breaking `!:` on any type, bumps the minor; everything else bumps the patch. Tags are annotated and never moved, and a push whose `HEAD` is already tagged does nothing. The first tag it cut was v0.7.1, the release that added the workflow.

The loop is closed now. I write from where I am, I read from where I am, and I open the vault when I am organizing. The thought never leaves the terminal unless I decide it should.

Source and docs live at [github.com/kobamkode/capture](https://github.com/kobamkode/capture).
