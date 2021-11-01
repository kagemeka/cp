import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.match(r'^a{1,5}b{10}c*$', input()) else 'No')

main()