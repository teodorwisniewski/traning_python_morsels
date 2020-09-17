from pathlib import Path
import os
import shutil
from tempfile import TemporaryDirectory
from contextlib import nullcontext

class cd:

    def __init__(self,subdirectory=None):
        self.cm_temp = TemporaryDirectory(dir=os.getcwd()) if subdirectory is None else nullcontext(subdirectory)
    
    def enter(self):
        self.__enter__()
    
    def exit(self):
        self.__exit__(None,None,None)

    def __enter__(self):
        self.previous = os.getcwd()
        self.current = self.cm_temp.__enter__()
        os.chdir(self.current)
        return self

    def __exit__(self, type, value, tb):
        # os.chdir has to be first. Otherwise we cannot remove a temporary file 
        # with temporary directory context maanger
        os.chdir(self.previous)
        self.cm_temp.__exit__(type, value, tb)
        



if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print("Current Working Directory " , os.getcwd())
    subdir = Path('some_subdirectory')
    try:
        subdir.mkdir()
        (subdir / 'my_file.txt').write_text('hello world!')
    except:
        print("file already exists")

    with cd(subdir):
        print(Path('my_file.txt').read_text())

    print(Path('my_file.txt').is_file())

    print("Current Working Directory " , os.getcwd())
    change_to_subdirectory = cd(subdir)
    print(Path('my_file.txt').is_file())

    with change_to_subdirectory:
        print(Path('my_file.txt').is_file())

    print(Path('my_file.txt').is_file())

    
    print(Path.cwd())
    # /home/trey
    with cd():
        print(Path.cwd())

    print(Path.cwd())


    with cd() as dirs:
        print('previous:', dirs.previous)
        print('current:', dirs.current)


    tempdir = cd()
    tempdir.enter()
    print(Path.cwd())
    tempdir.exit()
    print(Path.cwd())