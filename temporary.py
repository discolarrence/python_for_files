import os
import tempfile

#creating/deleting temporary files/directories in python shell

#create temporary directories
with tempfile.TemporaryDirectory() as tmpdirname:
    print("Created temporary directory named {}".format(tmpdirname))
    with open(os.path.join(tmpdirname, 'temp_file.txt'), 'w') as f:
        f.write('hello\n')
    input()

#create temporary file & read
with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write(b"hello\n")
    tmpfile.seek(0)
    tmpfile.read()

#create temporary file & close (can't see in directory)
fp = tempfile.TemporaryFile()
fp.write(b'hello\n')
fp.close()

#create temporary file (can see in directory)
fp = tempfile.NamedTemporaryFile()
fp.name