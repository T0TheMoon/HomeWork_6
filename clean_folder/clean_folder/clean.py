import os
import shutil
import sys
import re

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = (
"a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
"f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()


def normalize(name):
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', "_", new_name)
    return f"{new_name}.{'.'.join(extension)}"


extensions_guide = {
    'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
    'videos': ('AVI', 'MP4', 'MOV', 'MKV'),
    'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
    'archives': ('ZIP', 'GZ', 'TAR')
}
# Normalize для відповідності файлів
UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = (
"a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
"f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()


def normalize(name):
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', "_", new_name)
    return f"{new_name}.{'.'.join(extension)}"


# Функція, яка має опрацювати файл
def process_file(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension[1:].upper()

    # З'ясування категорії файлу
    for category, ext_list in extensions_guide.items():
        if extension in ext_list:
            return category
    return 'unknown'


# Функція для обробки папок
def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(file_path):
                continue

            category = process_file(file)
            normalized_name = normalize(file)
            new_file_path = os.path.join(folder_path, category, normalized_name)

            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
            shutil.move(file_path, new_file_path)


# Main функція
def main():
    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        return

    folder_path = sys.argv[1]

    for category in extensions_guide.keys():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    process_folder(folder_path)
    print("Sorting complete.")


if __name__ == "__main__":
    main()