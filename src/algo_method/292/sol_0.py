import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^.*algo.*$', input()) else 'No')

main()