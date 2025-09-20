from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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

def test_run_python_file():
    test_cases =  [
        ("main.py", ),
        ("main.py", ["3 + 5"]),
        ("tests.py", ),
        ("../main.py", ),
        ("nonexistent.py", )
    ]
    for case in test_cases:
        print(f'Result for "{case[0]}" file:')
        if len(case) > 1:
            print(run_python_file("calculator", case[0], case[1]))
        print(run_python_file("calculator", case[0]))


def main():
    # test_get_file_info()
    # test_get_file_contents()
    # test_write_file()
    test_run_python_file()


main()