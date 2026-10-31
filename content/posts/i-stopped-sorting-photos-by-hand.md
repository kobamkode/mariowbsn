+++
author = 'Mario Wibisono'
date = '2026-10-31T00:00:00+07:00'
draft = false
title = 'I Stopped Sorting Photos by Hand'
summary = 'Sorting a card into dated folders by hand was the boring step before culling. Kanistr copies photos and videos into folders named after the day they were taken, so I can start culling right away.'
description = 'Sorting a card into dated folders by hand was the boring step before culling. Kanistr copies photos and videos into folders named after the day they were taken, so I can start culling right away.'
tags = ['photography', 'rust', 'workflow']
+++

When I get home from a shoot, the card has a few hundred files on it. Some are from that day, some are from a trip two weeks ago that I never cleared. They all sit in `DCIM` folders with names like `DSCF4821.RAF`, so before I can delete a single bad frame I have to figure out which photo belongs to which day and move it there.

I used to do this in the file manager. Select the files, make a folder for each date, drag things around. It works, but it takes a while and I get it wrong sometimes. A file stays on the card, a day ends up split across two folders, or a photo taken after midnight goes into the wrong one. None of that is hard. It is just annoying, and I would rather spend that time looking at the photos.

So I wrote [Kanistr](https://github.com/kobamkode/kanistr). You plug the card in, choose a destination folder, press Import, and it copies everything into:

```
<destination>/<date>/<date>_<original name>
```

The date comes from the EXIF `DateTimeOriginal` tag, or `CreateDate` for videos. If neither exists, it falls back to the file's modified time. The capture date is the one I care about. Modified time changes every time the file is copied, so it cannot tell me when the photo was actually taken.

The date format supports `YYYY`, `MM`, `DD`, `HH`, and `SS`. I use `YYYYMMDD`, which gives me `20261031/20261031_DSCF4821.RAF`. It also scans the usual mount points on Linux, macOS, and Windows, so I do not have to point it at a folder. It picks up JPEG, HEIC, CR3, NEF, ARW, DNG, RAF, MP4, and MOV files. I shoot Fujifilm, so most of what I import is RAF.

A few details matter when you are copying files you cannot lose:

- It only reads the card. Nothing is ever written back to it.
- It never overwrites. An identical file is skipped, and a different file with the same name gets a `-1` suffix, so running an import twice is safe.
- Copies run in parallel, one to ten at a time.
- Folders named `MISC` and files starting with `._` are ignored.

That last one is small, but it keeps the camera's junk out of the library.

Once the import finishes I open the destination and start culling. Each day has its own folder, which is how I like to review a shoot. I cull first, then edit, and by then the library already makes sense.

I have not sorted a card by hand since.

Kanistr is written in Rust with GPUI. Builds for Linux, Windows, and macOS are on the [releases page](https://github.com/kobamkode/kanistr/releases), or you can run it from source with `cargo run --release`. The code is at [github.com/kobamkode/kanistr](https://github.com/kobamkode/kanistr).
