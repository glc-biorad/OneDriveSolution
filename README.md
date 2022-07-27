# OneDriveSolution
OneDrive interaction with python interface

# Current State:
A OneDrive class can be used to free up space and write to disk from OneDrive.

# Goals:
- Free up space on the local disk and move the file(s) to OneDrive.
- Download file(s) from OneDrive to the local machine.

# Modules:
- subprocess
  - Needed for running the attrib command for moving file(s) to OneDrive.
- os
  - Needed for dealing with paths.
- onedrive
  - Interface to OneDrive.

# Classes, Methods, and Functions:
- onedrive:
  - OneDrive (Class)
    - free_up_space (Method): move file(s) from the local disk to OneDrive
    - to_disk (Method): move file(s) from OneDrive to the local disk
    - change_path (Method): change the path OneDrive uses
- utility:
  - create_raw_string (Function): return a raw string from a string
