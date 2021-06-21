import os

def treewalker(start):
    total_size = 0
    total_files = 0

    for root, dirs, files in os.walk(start):
        subtotal = sum(
            os.path.getsize(os.path.join(root, name)) for name in files
        )
        total_size += subtotal
        file_count = len(files)
        total_files += file_count
        print(root, 'consumes', end='')
        print(subtotal, end='')
        print('bytes in', file_count, 'non-directory files')
    print(start, 'contains', total_files, 'files with a combined size of', 'total_size', bytes)

treewalker('.git')
