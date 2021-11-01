import typing 
import re


def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,4}$', input()) else 'No')


main()