"""Copies an entire folder and its contents into # a ZIP file whose filename
increments.
"""

import zipfile, os


def backup_to_zip(folder):
    """Backs up the entire contents of "folder" into a ZIP file.

    Args:
        folder (string): The name of a folder.
    """
    folder = os.path.abspath(folder)
    # Naming scheme for .zip backups.
    counter = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(counter) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        counter += 1
    # Creates the .zip file (backup).
    print(f"Creating {zip_file_name}...")
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    print()
    # Walks the entire folder tree and compress the files in each folder.
    for folder_name, subfolders, file_names in os.walk(folder):
        print(f"Adding files in {folder_name}...")
        backup_zip.write(folder_name)
        for file_name in file_names:
            temp_base = os.path.basename(folder) + '_'
            if file_name.startswith(temp_base) and file_name.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder_name, file_name))
    print()
    backup_zip.close()
    print("Done!")


def main():
    folder_name = input("Please enter the name of the folder you would like to backup: ")
    print()
    backup_to_zip(folder_name)


if __name__ == "__main__":
    main()
