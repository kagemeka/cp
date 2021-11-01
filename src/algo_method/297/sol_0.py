import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.search(r'1\+1', input()) else 'No')

main()