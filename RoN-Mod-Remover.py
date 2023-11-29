import os
import tkinter as tk
from tkinter import messagebox

def list_files_in_folder(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def find_unexpected_files():
    folder_path = folder_path_entry.get()

    expected_folders = ["~mods", "mod.io"]
    expected_files = {
        "pakchunk0-WindowsNoEditor.pak",
        "pakchunk0-WindowsNoEditor_0_P.pak",
        "pakchunk1-WindowsNoEditor.pak",
        "pakchunk1-WindowsNoEditor_0_P.pak",
        "pakchunk2-WindowsNoEditor.pak",
        "pakchunk2-WindowsNoEditor_0_P.pak",
        "pakchunk3-WindowsNoEditor.pak",
        "pakchunk3-WindowsNoEditor_0_P.pak",
        "pakchunk4-WindowsNoEditor.pak",
        "pakchunk4-WindowsNoEditor_0_P.pak",
        "pakchunk5-WindowsNoEditor.pak",
        "pakchunk5-WindowsNoEditor_0_P.pak",
        "pakchunk6-WindowsNoEditor.pak",
        "pakchunk6-WindowsNoEditor_0_P.pak",
        "pakchunk7-WindowsNoEditor.pak",
        "pakchunk7-WindowsNoEditor_0_P.pak",
        "pakchunk8-WindowsNoEditor.pak",
        "pakchunk8-WindowsNoEditor_0_P.pak",
        "pakchunk9-WindowsNoEditor.pak",
        "pakchunk9-WindowsNoEditor_0_P.pak",
        "pakchunk10-WindowsNoEditor.pak",
        "pakchunk10-WindowsNoEditor_0_P.pak",
        "pakchunk11-WindowsNoEditor.pak",
        "pakchunk11-WindowsNoEditor_0_P.pak",
        "pakchunk12-WindowsNoEditor.pak",
        "pakchunk12-WindowsNoEditor_0_P.pak"
    }

    if not folder_path:
        messagebox.showerror("Error", "Please provide a folder path.")
        return

    files_in_folder = set(list_files_in_folder(folder_path))
    folders_in_folder = {f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))}

    unexpected_folders = folders_in_folder.difference(expected_folders)
    unexpected_files = files_in_folder.difference(expected_files)
    missing_files = expected_files.difference(files_in_folder)

    output_message = ""
    if unexpected_folders:
        output_message += f"Unexpected folders: {', '.join(unexpected_folders)}\n"
    if unexpected_files:
        output_message += f"Unexpected files: {', '.join(unexpected_files)}\n"
    if missing_files:
        output_message += f"Missing files: {', '.join(missing_files)}\n"

    if output_message:
        messagebox.showinfo("Check Result", f"Check result:\n{output_message}")
        create_delete_button(folder_path, unexpected_files, unexpected_folders, missing_files)

    else:
        messagebox.showinfo("Check Result", "No unexpected items found.")


def create_delete_button(folder_path, unexpected_files, unexpected_folders, missing_files):
    if not hasattr(root, 'delete_button_created'):
        root.delete_button = tk.Button(root, text="Delete Unexpected/Missing Items",
                                       command=lambda: delete_unexpected(folder_path, unexpected_files,
                                                                         unexpected_folders, missing_files))
        root.delete_button.pack()
        root.delete_button_created = True


def delete_unexpected(folder_path, unexpected_files, unexpected_folders, missing_files):
    confirm_delete = messagebox.askquestion("Confirm Deletion",
                                            "Are you sure you want to delete the unexpected/missing items?")
    if confirm_delete == 'yes':
        for file in unexpected_files:
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
        for folder in unexpected_folders:
            folder_path = os.path.join(folder_path, folder)
            os.rmdir(folder_path)
        messagebox.showinfo("Deletion Completed", "Unexpected/missing items deleted successfully.")
        root.delete_button.destroy()  # Remove the delete button after deletion
        del root.delete_button_created  # Reset the flag for the button creation
    else:
        messagebox.showinfo("Deletion Cancelled", "Deletion process cancelled.")


# Create the main window
root = tk.Tk()
root.title("Check and Delete Unexpected Files/Folders")

# Folder path input
folder_path_label = tk.Label(root, text="Enter Folder Path:")
folder_path_label.pack()
folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.pack()

# Button to check for unexpected files
check_button = tk.Button(root, text="Check for Unexpected Items", command=find_unexpected_files)
check_button.pack()

root.mainloop()