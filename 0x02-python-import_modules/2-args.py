#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{arg} arguments:")
        for i in range(1, arg+1):
            print("{}: {}".format(i, sys.argv[i]))
