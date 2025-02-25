import os

def rename():
    directory = "./change"  # Folder containing files to rename
    try:
        # Get all files sorted by creation time (st_birthtime) in reverse order (newest first)
        files = sorted(
            (f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))),
            key=lambda x: os.stat(os.path.join(directory, x)).st_birthtime)

        if not files:
            print("No files found in the 'change' folder.")
            return

        mapping_file = os.path.join(directory, "file_mapping.txt")
        with open(mapping_file, "w") as f:
            for i, filename in enumerate(files, start=1):
                f.write(f"{i},{filename}\n")
                new_name = f"{i}{os.path.splitext(filename)[1]}"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

        print("Files renamed and mapping saved to 'file_mapping.txt'.")
    except AttributeError:
        print("Your filesystem doesn't support st_birthtime (true creation time).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    rename()
