from pathlib import Path
import os




if __name__ == "__main__":
    os.chdir(__file__)
    print("Current Working Directory " , os.getcwd())
    subdir = Path('some_subdirectory')
    subdir.mkdir()
    (subdir / 'my_file.txt').write_text('hello world!')