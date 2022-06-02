#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv) - 1
    if arg_num == 0:
        print(f"{}".format(arg_num))
    else:
        result = []
        for i in range(1, arg_num + 1):
            result.append(int(argv[i]))
        print(f"{}".format(sum(result)))
