import os

pth = "kennethlove2-2012-04-29.txt"

def cleanup(path):
    for file in os.scandir(path):
        if file.is_file():
            file = file.path.split('/')[1]
            split_file = file.split('-')
            ext = split_file[3].split('.')
            old_name = path + '/' + file
            new_name = path + '/' + file[1] + '-' + split_path[2] + '-' + ext[0] + '-' + split_path[0] + '.' + ext[1]
    os.rename(old_name, new_name)
    
