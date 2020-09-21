from contextlib import contextmanager,nullcontext
from pathlib import Path 
import os
from tempfile import TemporaryDirectory
import shutil
from dataclasses import dataclass

@dataclass
class Dirs:
    previous: os.PathLike
    current: os.PathLike

@contextmanager
def cd(subdirectory = None):
    previous = os.getcwd()
    tmp_dir =  TemporaryDirectory(dir=previous) if subdirectory is None else nullcontext(subdirectory)
    with tmp_dir as f:
        current = f
        d = Dirs(previous=previous,current=current)
        try:
            os.chdir(f)    
            yield d
        finally:
            os.chdir(previous)
    
        
    



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