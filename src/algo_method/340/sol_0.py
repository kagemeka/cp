import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^[a-z]+(-[a-z]+)*$', input()) else 'No')

main()