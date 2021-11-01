import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^metho.+od$', input()) else 'No')

main()