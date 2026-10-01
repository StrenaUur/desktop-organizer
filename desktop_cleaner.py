import os
import shutil

#Dynamic Desktop Path Detection
#Handles standard Desktop and OneDrive Desktop locations
USER_PROFILE = os.path.expanduser("~")
ONEDRIVE_DESKTOP = os.path.join(USER_PROFILE, "OneDrive", "Desktop")
DEFAULT_DESKTOP = os.path.join(USER_PROFILE, "Desktop")

if os.path.exists(ONEDRIVE_DESKTOP):
    DESKTOP_PATH = ONEDRIVE_DESKTOP
elif os.path.exists(DEFAULT_DESKTOP):
    DESKTOP_PATH = DEFAULT_DESKTOP
else:
    DESKTOP_PATH = None

#Extension Mappings
EXTENSION_MAPS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".iso", ".dmg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp", ".cs"]
}

def organize_desktop():
    """Organizes files on the desktop into categorized folders based on extension."""
    if not DESKTOP_PATH or not os.path.exists(DESKTOP_PATH):
        print("Error: Desktop folder could not be found.")
        return

    print(f"Organizing Desktop at: {DESKTOP_PATH}\n")

    #Scan all items in the desktop directory
    for item in os.listdir(DESKTOP_PATH):
        item_path = os.path.join(DESKTOP_PATH, item)

        #Skip directories
        if os.path.isdir(item_path):
            continue

        #Skip hidden files and the script file itself
        if item.startswith(".") or item == os.path.basename(__file__):
            continue

        #Extract file extension
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        #Determine target category folder
        target_folder = "Others"  # Default folder for unmatched extensions
        for folder_name, extensions in EXTENSION_MAPS.items():
            if ext in extensions:
                target_folder = folder_name
                break

        #Create a target folder path
        target_dir = os.path.join(DESKTOP_PATH, target_folder)
        os.makedirs(target_dir, exist_ok=True)

        #Move file to the designated folder
        destination = os.path.join(target_dir, item)
        shutil.move(item_path, destination)
        print(f"Moved: {item} -> {target_folder}/")

    print("\nDesktop organization complete!")


if __name__ == "__main__":
    organize_desktop()