import argparse


def test_files():
    print("Testing all files...")


def test_single_file(filename):
    print(f"Testing {filename}...")


def generate_files():
    print("Generating files to a new folder...")


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
