from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test_get_file_info():
    dirs = (".", "pkg", "/bin", "../")
    for dir in dirs:
        print(f"Result for {dir} directory:")
        print(get_files_info("calculator", dir))

def test_get_file_contents():
    files = ("main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py")
    for file in files:
        print(f"Result for {file} file:")
        print(get_file_content("calculator", file))


def main():
    # test_get_file_info()
    test_get_file_contents()


main()