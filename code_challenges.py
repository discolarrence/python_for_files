import os

# write a function named absolute that takes two arguments, a path string and a root string. 
# If the path is not already absolute, return the path with the root prepended to it.
def absolute(path, root):
    if os.path.isabs(path):
        return path
    else:
        return root + path

#Create a function named dir_contains takes a path to a directory and a list of file names. 
#If all of the file names exist within that directory, return True, otherwise, return False.
def dir_contains(path, names):
    files = list(os.listdir(path))
    for name in names:
        if name not in files:
            return False
    return True

# Create a function named create_daily_dir in backup.py. 
# This function should take a string which will be a date in either year-month-day (2012-12-22) or month-day-year (12-22-2012) format. 
# Use that to create a directory like 2012-12-22 (year-month-day) in the financial directory (which is in the current directory).
def create_daily_dir(date):
    os.makedirs('financial/{}'.format(date))

# Finish the function named cleanup in consistency.py. 
# This function should take a string which will be a path to a local directory. The file names in this directory are messy. 
# Clean them up so they all follow the same pattern.
# Filenames consist of a username (alphanumeric, 3-12 characters)
# and a date (four digit year, two digit month, two digit day),
# and an extension. They should end up in the format
# year-month-day-username.extension.

def cleanup(path):
    for f in os.scandir(path):
        if f.is_file():
            f = f.path.split('/')[1]
            filename = f.split('.')[0]
            extension = f.split('.')[1]
            date = []
            for _ in filename.split('-'):
                try:
                    int(_)
                    date.append(_)
                except ValueError:
                    username = _
            old_name = path + '/' + f
            new_name = path + '/' + '-'.join(date) + '-' + username + '.' + extension
            os.rename(old_name, new_name)

# Make a function named delete_by_date. It should take date string like 2015-10-31 and delete any files in the "backups" local directory that have that date in their filename.
def delete_by_date(date):
    for filename in os.listdir(os.getcwd() + '/backups'):
        if date in filename:
            os.remove('backups/' + filename)
