# Python Learning Archive

**Games, small web experiments, and scripting projects from learning Python.**

This collection shows early exploration rather than one polished product. Projects have independent dependencies and may retain local paths or unfinished experiments.

## Start with the games

- [Filler](Filler/): a browser-game experiment with Flask and board-solving helpers.
- [Cursor Game](Cursor%20Game/): a desktop game experiment.
- [Q4Project](Q4Project/): an interactive school-project game with sound assets.
- [FontsGame](FontsGame/): graphical experiments and learning scripts.
- [Testing](Testing/) and [Testing2](Testing2/): smaller language exercises.
- `BruteForcePassword/`: an old security exercise; its password, username, and IP-list inputs were removed from the public repository.

## Running locally

Choose a folder, inspect its imports and asset paths, and install dependencies in a dedicated virtual environment. There is no repository-wide installation command. Run media-heavy games from their own folder so relative assets resolve.

## Responsible use

Older scraping and credential-related experiments are not secure application patterns or recommended entry points. Do not run network scripts against systems without explicit authorization, use real credentials, or use personal contact lists. Inspect anything that sends email, reads files, or opens network connections before execution. Sensitive sample files and a local password database were removed from the public repository.
