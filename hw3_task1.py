import os
import shutil
import concurrent.futures

def copy_files(source_dir, target_dir='/Users/reiraserizawa/Documents/uni_sorted'):
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            target_path = os.path.join(target_dir, extension, file)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)

def main(source_dir, target_dir='/Users/reiraserizawa/Documents/uni_sorted'):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(copy_files, source_dir, target_dir)

if __name__ == '__main__':
    source_directory = '/Users/reiraserizawa/Documents/uni'
    target_directory = '/Users/reiraserizawa/Documents/uni_sorted'
    main(source_directory, target_directory) 