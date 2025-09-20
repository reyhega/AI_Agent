from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test_get_file_info():
    dirs = (".", "pkg", "/bin", "../")
    for dir in dirs:
        print(f'Result for "{dir}" directory:')
        print(get_files_info("calculator", dir))

def test_get_file_contents():
    files = ("main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py")
    for file in files:
        print(f'Result for "{file}" file:')
        print(get_file_content("calculator", file))

def test_write_file():
    test_cases = [
        ("lorem.txt", "wait, this isn't lorem ipsum"),
        ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("/tmp/temp.txt", "this should not be allowed")
    ]
    for case in test_cases:
        print(f'Writing "{case[1]}" to file "{case[0]}"')
        print(write_file("calculator", case[0], case[1]))


def main():
    # test_get_file_info()
    # test_get_file_contents()
    test_write_file()


main()