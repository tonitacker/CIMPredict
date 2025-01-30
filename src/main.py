import sys

if sys.platform.startswith("win"):
    from main_windows import main
elif sys.platform.startswith("darwin"):  # macOS
    from main_macos import main
elif sys.platform.startswith("linux"):
    from main_linux import main
else:
    raise RuntimeError("Unsupported OS")

if __name__ == "__main__":
    main()
