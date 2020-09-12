from pathlib import Path
import os

class cd:
    def __init__(self,subdirectory_path):
        self.subdirectory_path = subdirectory_path

    def __enter__(self):
      #  print("Current Working Directory " , os.getcwd())
        self.main_dir = os.getcwd()
        os.chdir(os.path.join(self.main_dir,self.subdirectory_path))
     #   print("Current Working Directory after changing " , os.getcwd())

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.main_dir)
       # print("__exit__ Current Working Directory " , os.getcwd())





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