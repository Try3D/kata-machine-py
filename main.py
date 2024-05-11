import os
import shutil
import argparse


def test_files():
    print("Testing all files...")


def test_single_file(filename):
    print(f"Testing {filename}...")


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
        if args.filename:
            test_single_file(args.filename)
        else:
            test_files()
    elif args.action == "generate":
        generate_files()
    elif args.action == "clean":
        clean_files()


if __name__ == "__main__":
    main()
