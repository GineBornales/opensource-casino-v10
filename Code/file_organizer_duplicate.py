import os
import shutil
import subprocess

source_dir = os.path.dirname(os.path.abspath(__file__))
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".html", ".css", ".js", ".py", ".php"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}

def organize_files():
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        if not os.path.isfile(filepath):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        category = "Others"

        for cat, extensions in categories.items():
            if ext in extensions:
                category = cat
                break

        dest_folder = os.path.join(source_dir, category)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        new_path = os.path.join(dest_folder, filename)
        if os.path.exists(new_path):
            base, ext = os.path.splitext(filename)
            new_filename = f"{base}_duplicate{ext}"
            new_path = os.path.join(dest_folder, new_filename)
        
        try:
            shutil.move(filepath, new_path)
            print(f"Moved {filename} to {category}/")
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

if __name__ == "__main__":
    print("Starting file organization...")
    organize_files()
    print("File organization completed!")
