# chess-discord-rpc
A guide to have custom rpc on your Discord profile when using Lichess or Chess.com
ONLY WORKS ON LINUX-BASED SYSTEMS as of now. Requires root permissions.

## How to do it
1. Download the latest release, it comes with both Lichess and Chess.com executables. Delete either folder if you dont want it before continuing.
2. Go into the folder of lichess, chesscom, or both, and edit the python files. Simply replace "Stormlightnoway" with your own username wherever it is said.
3. Run the installer with `./install.sh`. This will move the executables and .desktop files to the correct places.
You should be able to search for Lichess or Chess.com as a native program now, and it will work with your discord! If you ever need to modify the python script(s), the locations are at `/usr/share/applications/lichess/` or `/usr/share/applications/chesscom/`! 

## Other stuff
The "native" chess client binaries are created with Nativefier, you can use the tool yourself if you do not trust the ones I've provided, just make sure the file names match up.
I may try to use GitHub actions in the future.
