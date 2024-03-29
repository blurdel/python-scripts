import argparse
import os


# Command line params
argMap = { "fname": "none.txt", "-v": False, "count": 0 }

def main() :

    print("cwd:", os.getcwd())

    parser = argparse.ArgumentParser(prog="clargs")
    parser.add_argument("-f", required=True, metavar="filename", help="The input filename")
    parser.add_argument("-n", required=False, type=int, default=1, help="the count n to iterate")
    parser.add_argument("-v", action='store_true', help="Show version info and exit")

    try:
        args = parser.parse_args()
        print("args", args)

        if not args.f is None:
            argMap['fname'] = args.f.strip()
        
        argMap['count'] = args.n
        argMap['-v'] = args.v

    except Exception as e:
        print("Exception:", str(e))
        return -1

    print()
    print("### argMap contents ###")
    for key, val in argMap.items():
        print("{}: {}".format(key, val))
    print()

    if not os.path.exists(argMap['fname']):
        print("Error: input file not found, exiting ...")
        return 1
    else:
        print("Input file was found!")


if __name__ == "__main__":
    exit(main())
