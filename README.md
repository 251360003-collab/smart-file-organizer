# Smart File Organizer

This project automatically organizes files into folders based on their file extensions.

## Features

- Organizes files automatically
- Creates folders by file type
- Supports PDF, JPG, PNG, TXT and other file formats
- Uses Python automation

## Technologies Used

- Python
- os
- shutil

## How to Run

```bash
python file_organizer.py
```

## Example

Before:

```text
test_files/
├── report.pdf
├── image.jpg
├── notes.txt
├── screenshot.png
```

After:

```text
test_files/
├── pdf/
│   └── report.pdf
├── jpg/
│   └── image.jpg
├── txt/
│   └── notes.txt
└── png/
    └── screenshot.png
```

## Author

Bhanvi Soni
