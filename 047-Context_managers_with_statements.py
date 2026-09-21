with open("doc.txt" ,"r") as file:
    data=file.read()
    print(data)

  
#open() — Opens a file for reading, writing, or appending and returns a file object.
#tempfile — Creates temporary files and directories that are automatically managed and cleaned up.
#zipfile — Used to create, read, extract, and manage ZIP archives.
#contextlib.ExitStack — Manages multiple context managers dynamically and ensures proper cleanup.
#pathlib.Path().open() — Opens a file using a Path object, providing a cleaner object-oriented approach to file handling.

#“These are different tools for managing files and resources; we choose them based on the task, and many of them can be used with context managers (with).”
