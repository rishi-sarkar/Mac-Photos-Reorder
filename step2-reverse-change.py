import os


def reverse():
    directory = "./photos"  # Folder containing renamed files
    try:
        mapping_file = os.path.join(directory, "file_mapping.txt")
        if not os.path.exists(mapping_file):
            print("Mapping file 'file_mapping.txt' not found in the 'photos' folder.")
            return

        with open(mapping_file, "r") as f:
            for line in f:
                number, original_name = line.strip().split(",", 1)
                current_name = os.path.join(
                    directory, f"{number}{os.path.splitext(original_name)[1]}")
                original_path = os.path.join(directory, original_name)
                if os.path.exists(current_name):
                    os.rename(current_name, original_path)

        print("Original file names restored.")
        # Delete the mapping file
        os.remove(mapping_file)
        print("Original file names restored, and 'file_mapping.txt' deleted.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    reverse()
