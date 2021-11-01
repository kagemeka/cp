import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.search(r'\d{3,}', input()) else 'No')

main()