





from contextlib import contextmanager
from pathlib import Path
import os

@contextmanager
def cd(*args):

    subdirectory = args[0] if len(args)>0 else ""
    original_dir = os.path.abspath(os.curdir)

    try:
        if subdirectory == "": 
            os.mkdir("tmp_16wleaw")
            os.chdir("tmp_16wleaw")
        else:
            os.chdir(subdirectory)
        yield
    finally:
        print("I have just got out of with statement")
        os.chdir(original_dir)
        if subdirectory == "": 
            os.rmdir("tmp_16wleaw")

    











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
    # /home/trey