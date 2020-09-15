
from contextlib import contextmanager
from pathlib import Path
import os
import shutil
from tempfile import mkdtemp


@contextmanager
def cd(subdirectory=None):
    orginal_dir = os.getcwd()
    if subdirectory is None:
        tmpdir = subdirectory = mkdtemp(dir = orginal_dir)
    else:
        tmpdir = None
    try:
        os.chdir(subdirectory)
        yield
    finally:
        os.chdir(orginal_dir)
        if tmpdir: shutil.rmtree(tmpdir)
        print("Getting out of context manager")








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
