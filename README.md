# Ready or Not Mod Verification Tool

The **Ready or Not Mod Verification Tool** is a Python-based graphical user interface (GUI) application designed specifically for the game "Ready or Not." It assists users in verifying the contents of the "Paks" folder, where mods are typically stored, against an expected list of files and folders. This tool identifies any unexpected mods or files present in the "Paks" directory, allowing users to manage and clean up their mods effectively.

## Requirements
- Python 3.x installed on your system.
- Tkinter library (comes pre-installed with Python).

## Instructions

### Downloading the Release Build
1. Go to the [Releases](https://github.com/Snaping14/Ready-or-Not-Mod-Remover/releases) page of this repository.
2. Download the latest release build (e.g., `ReadyOrNotModRemover_v1.1.py
`).

### Running the Tool
1. Open a terminal or command prompt.
2. Navigate to the directory where the extracted files are located.
3. Run the script using the command:
```
python ReadyOrNotModRemover_v1.1.py
```
### How to Use
1. **To find the "Paks" folder in the Ready or Not game:**
- Right-click on the game in the Steam library.
- Hover over "Manage" and then click on "Browse Local Files."
- This will open File Explorer at the root directory of the game.
- Navigate to `ReadyOrNot -> Content -> Paks`.
- Copy the path of the "Paks" folder.
2. Launch the application by executing the script as mentioned in the instructions above.
3. Enter the full path of the "Paks" folder you copied into the provided "Enter Folder Path" field.
4. Click the "Check for Unexpected Items" button to initiate the verification process.
5. The tool will display a summary of unexpected mods or files found in the specified "Paks" folder.
6. If any unexpected items are detected, the "Delete Unexpected/Missing Items" button will appear. Click this button to remove these items from the "Paks" folder after confirming the deletion.
7. Once the deletion process is complete, a confirmation message will be displayed.
8. Close the application window when finished.

**Caution**: Exercise extreme caution while deleting files and folders, as the deletion process cannot be undone. **Backup your files** before using this tool, and use it **at your own risk**.

## Contributions and Issues
Contributions, bug reports, and suggestions for improvements are welcome! Feel free to open an issue or pull request on this GitHub repository.

## License
This tool is open-source and released under the MIT License.
