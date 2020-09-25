from pathlib import Path
import os
from tempfile import TemporaryDirectory
from contextlib import nullcontext


class cd:

    def __init__(self,subdirectory=None):
        
        self.temp_dir = TemporaryDirectory(dir=os.getcwd()) if subdirectory is None else nullcontext(subdirectory)

    def __enter__(self):
        self.current = self.temp_dir.__enter__()
        self.previous = os.getcwd()
        os.chdir(self.current)

        return self
    
    def enter(self):
        self.__enter__()
    
    def __exit__(self,*args):
        os.chdir(self.previous)
        self.temp_dir.__exit__(None,None,None)
        

    def exit(self):
        self.__exit__(None,None,None)





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