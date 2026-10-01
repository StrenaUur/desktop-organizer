# Desktop Organizer Script

A simple and efficient Python script designed to clean up and organize your desktop automatically. It categorizes files based on their file extensions and moves them into organized subfolders (e.g., Images, Documents, Code, Archives).

## Features

- **Automated Categorization**: Automatically detects file extensions and moves them to matching directories.
- **OneDrive Compatibility**: Automatically checks both local user path and OneDrive Desktop path.
- **Safe Execution**: Ignores existing folders, hidden files, and the script file itself.
- **Customizable**: Easy to add or modify file categories and extension mapping.

## File Categories

- **Images**: `.jpg`, `.png`, `.gif`, `.webp`, etc.
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, etc.
- **Archives**: `.zip`, `.rar`, `.7z`, etc.
- **Installers**: `.exe`, `.msi`, `.iso`, etc.
- **Videos**: `.mp4`, `.mkv`, `.avi`, etc.
- **Audio**: `.mp3`, `.wav`, etc.
- **Code**: `.py`, `.js`, `.html`, `.cpp`, etc.
- **Others**: Any unmatched file types.

## Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/desktop-organizer.git](https://github.com/YOUR_USERNAME/desktop-organizer.git)
   cd desktop-organizer