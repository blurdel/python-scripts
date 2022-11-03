import argparse
import os
import parser


# Command line params
argMap = { "fname": "none.txt", "-v": False }

def main() :

    print("cwd:", os.getcwd())

    parser = argparse.ArgumentParser("arg parse")
    parser.add_argument("-f", required=True, metavar="filename", help="The input filename")
    parser.add_argument("-v", action='store_true', help="Show version info and exit")

    try:
        args = parser.parse_args()
        print("args", args)

        if not args.f is None:
            argMap['fname'] = args.f.strip()
        argMap['-v'] = args.v

    except Exception as e:
        print("Exception:", str(e))
        return -1


    print("### argMap contents ###")
    for key, val in argMap.items():
        print("{}: {}".format(key, val))
    print()

    if not os.path.exists(argMap['fname']):
        print("Error: input file not found, exiting ...")
        return 1


if __name__ == "__main__":
    exit(main())
