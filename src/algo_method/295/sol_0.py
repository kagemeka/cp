import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^\d{3}-\d{4}$', input()) else 'No')

main()