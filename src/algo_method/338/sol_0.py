import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.search(r'\(.+\)', input()) else 'No')

main()