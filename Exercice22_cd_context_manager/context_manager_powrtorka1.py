
from contextlib import contextmanager
from pathlib import Path
import os
import shutil
from tempfile import TemporaryDirectory
from dataclasses import dataclass

@dataclass
class Dirs:
    previous: Path
    current: Path


@contextmanager
def nullcontext(return_value=None):
    yield return_value

# @contextmanager
# def cd(subdirectory=None):
#     original_dir = os.getcwd()
#     cm = TemporaryDirectory(dir=original_dir) if subdirectory is None else nullcontext(subdirectory)
#     sub_dir_path = cm.args[0] if not isinstance(cm,TemporaryDirectory) else cm.name
#     obj = Dirs(Path(original_dir),Path(sub_dir_path))
#     with cm as temp_sub:
#         os.chdir(temp_sub)
#         try:
#             yield obj
#         finally:
#             os.chdir(original_dir)

class cd:
    def __init__(self,subdirectory):
        self.original_dir = os.getcwd()
        self.cm = TemporaryDirectory(dir=self.original_dir) if subdirectory is None else nullcontext(subdirectory)
        self.sub_dir_path = self.cm.args[0] if not isinstance(self.cm,TemporaryDirectory) else self.cm.name

    def __enter__(self):
        with self.cm as temp_sub:
            os.chdir(temp_sub)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)

    




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