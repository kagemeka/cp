import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.search(r'\d', input()) else 'No')

main()