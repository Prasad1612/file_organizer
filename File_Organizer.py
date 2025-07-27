import os
import shutil

# ✅ Target directory
directory = r'C:\Users\User\Downloads'  # Your File Path

# ✅ Folder name mapping for code file types
code_subfolders = {
    'py': 'Python',
    'js': 'JavaScript',
    'html': 'HTML',
    'css': 'CSS',
    'cpp': 'C++',
    'c': 'C',
    'cs': 'C#',
    'java': 'Java',
    'php': 'PHP',
    'json': 'JSON',
    'xml': 'XML',
    'ts': 'TypeScript',
    'sql': 'SQL',
    'sh': 'Shell',
    'bat': 'Batch'
}

# ✅ General file extension mapping (non-code)
file_extensions = {
    # Documents
    'pdf': 'PDFs',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'rtf': 'Documents',
    'odt': 'Documents',

    # Spreadsheets
    'csv': 'Data',
    'xlsx': 'Data',
    'xls': 'Data',
    'ods': 'Data',

    # Presentations
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'odp': 'Presentations',

    # Images
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',
    'webp': 'Images',
    'svg': 'Images',
    'ico': 'Images',
    'heic': 'Images',

    # Archives
    'zip': 'Archives',
    'rar': 'Archives',
    '7z': 'Archives',
    'tar': 'Archives',
    'gz': 'Archives',
    'bz2': 'Archives',

    # Audio
    'mp3': 'Music',
    'wav': 'Music',
    'flac': 'Music',
    'aac': 'Music',
    'ogg': 'Music',
    'm4a': 'Music',

    # Videos
    'mp4': 'Videos',
    'mkv': 'Videos',
    'avi': 'Videos',
    'mov': 'Videos',
    'wmv': 'Videos',
    'flv': 'Videos',
    'webm': 'Videos',

    # Executables
    'exe': 'Executables',
    'msi': 'Executables',
    'apk': 'Executables',

    # System/Config Files
    'ini': 'System',
    'log': 'System',
    'tmp': 'System',
    'bak': 'System',

    # Design & Media Projects
    'psd': 'Designs',
    'ai': 'Designs',
    'xd': 'Designs',
    'fig': 'Designs',
    'sketch': 'Designs',
}

# ✅ File organizing logic
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        ext = filename.split('.')[-1].lower()

        # Special handling for code files
        if ext in code_subfolders:
            subfolder = code_subfolders[ext]
            folder_path = os.path.join(directory, 'Code', subfolder)
        elif ext in file_extensions:
            folder_path = os.path.join(directory, file_extensions[ext])
        else:
            continue  # skip unlisted file types

        # Create target folder if needed
        os.makedirs(folder_path, exist_ok=True)

        # Move the file
        shutil.move(file_path, os.path.join(folder_path, filename))

print("📁 Files organized.")
