import os
import shutil
import sys

def organize_folder(folder_path):
    # Create directories for different file types
    file_types = {
        '.pdf': 'PDFs',
        '.doc': 'Word_Documents',
        '.docx': 'Word_Documents',
        '.dot': 'Word_Documents',
        '.odt': 'Word_Documents',
        '.xls': 'Excels',
        '.xlsx': 'Excels',
        '.csv': 'Excels',
        '.zip': 'Compressed_Folders',
        '.rar': 'Compressed_Folders',
        '.ipynb': 'Jupyter_Notebooks',
        '.pbix': 'PowerBI_Files',
        '.pptx': 'PowerPoints'
    }
    
    # Find file extensions present in the folder
    extensions = set()
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            file_extension = os.path.splitext(item)[-1].lower()
            if file_extension in file_types:
                extensions.add(file_extension)
    
    # Create target directories for each file type
    for extension in extensions:
        file_type_directory = file_types.get(extension)
        target_directory = os.path.join(folder_path, file_type_directory)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
    
    # Move files to appropriate directories
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[-1].lower()
            file_type_directory = file_types.get(file_extension)
            if file_type_directory:
                shutil.move(item_path, os.path.join(folder_path, file_type_directory, item))
            else:
                os.remove(item_path)  # Delete files with unsupported extensions
    
    print("Tidying up done")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py folder_path")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        sys.exit(1)
    
    organize_folder(folder_path)
