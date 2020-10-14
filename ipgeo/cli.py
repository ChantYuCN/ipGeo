"""Console script for ipgeo."""
import argparse
import sys
from ipgeo import APIrequest


def main():
    """Console script for ipgeo."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    parser.add_argument("-v",
                        "--verbosity",
                        default=None,
                        help="increase output verbosity.")
    parser.add_argument("-i",
                        "--ip",
                        default=None,
                        help="refer to given ip to locat the contry.")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "ipgeo.cli.main")

    print(args)
    APIrequest(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
