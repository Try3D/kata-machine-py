import os
import shutil
import pytest
import argparse


def fuzzy_test_search(search):
    test_files = [
        f[:-3]
        for f in os.listdir("tests")
        if f.startswith("test_") and f.endswith(".py")
    ]

    matches = [test_file for test_file in test_files if search in test_file]

    return matches


def test_single_file(search):
    matches = fuzzy_test_search(search)

    if not matches:
        print("Cannot find any test files to run.")
    else:
        for match in matches:
            test_module = f"tests/{match}"
            pytest.main([f"{test_module}.py", "-s"])


def generate_files():
    print("Generating files to a new folder...")
    src_dir = "src"
    exercises_dir = "exercises"
    if not os.path.exists(exercises_dir):
        os.makedirs(exercises_dir)

    for file_name in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, file_name)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, exercises_dir)


def clean_files():
    print("Cleaning files...")
    exercises_dir = "exercises"
    if os.path.exists(exercises_dir):
        shutil.rmtree(exercises_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Utility for testing, generating, and cleaning files"
    )
    parser.add_argument(
        "action", choices=["test", "generate", "clean"], help="Action to perform"
    )
    parser.add_argument("filename", nargs="?", help="Filename to test")

    args = parser.parse_args()

    if args.action == "test":
        if not args.filename:
            print("Error: Filename must be provided for the 'test' action.")
            return
        test_single_file(args.filename)
    elif args.action == "generate":
        generate_files()
    elif args.action == "clean":
        clean_files()


if __name__ == "__main__":
    main()
