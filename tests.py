from functions.get_files_info import get_files_info

def test_get_file_info():
    dirs = (".", "pkg", "/bin", "../")
    for dir in dirs:
        print(f"Result for {dir} directory:")
        print(get_files_info("calculator", dir))


def main():
    test_get_file_info()




main()