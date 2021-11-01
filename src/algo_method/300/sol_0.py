import typing 
import re



def main() -> typing.NoReturn:
    print('Yes' if re.search(r'cat|dog', input()) else 'No')

main()