import os 
import shutil
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
    
print(read_file('C:/Users/ageeha927/Downloads/sample.txt'))

def append(file_path, new_content):
    with open(file_path, 'a') as file:
        file.write(new_content)

print(append('C:/Users/ageeha927/Downloads/sample.txt', "Additional line added for file operations."))

def create_folder(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path) 
    print(f"Directory {path} created")

print(create_folder('C:/Users/ageeha927/Desktop/', 'Files'))

def move(files, directory):
    shutil.move(files, directory)

print(move('C:/Users/ageeha927/Desktop/sample.txt', 'C:/Users/ageeha927/Desktop/Files'))

def write_file(file_path, new_content):
    with open(file_path, 'w') as file:
        file.write(new_content)

print(write_file( 'C:/Users/ageeha927/Desktop/Files/file1.txt', 'hello'))
print(write_file( 'C:/Users/ageeha927/Desktop/Files/file2.txt', 'hello'))

def delete(directory):
    os. remove(directory)

print(delete('C:/Users/ageeha927/Desktop/Files/file2.txt'))

def rename(file_old_name, file_new_name):
    os.rename(file_old_name, file_new_name)

print(rename('C:/Users/ageeha927/Desktop/Files/file1.txt', 'C:/Users/ageeha927/Desktop/Files/renamed_file.txt'))

def list_files(path):
    for root, dir, files in os.walk(path):
        print(f'Current directory: {root}')
        print("Files:")
        for file in files:
            print(os.path.join(root, file))
        print("------------------------------------")

print(list_files('C:/Users/ageeha927/Desktop/Files'))

def make_archive(my_archive, archive_type, directory_to_archive):
    shutil.make_archive(my_archive, archive_type, directory_to_archive)

print(make_archive('C:/Users/ageeha927/Desktop/archive', 'zip', 'C:/Users/ageeha927/Desktop/Files' ))
