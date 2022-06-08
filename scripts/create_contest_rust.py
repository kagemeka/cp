import typing
import sys
import os


def dump_toml(
    data: typing.Mapping[str, typing.Any],
    path: str,
) -> typing.NoReturn:
    import toml
    with open(file=path, mode='w') as f:
        toml.dump(o=data, f=f)


def load_toml(path: str) -> dict:
    import toml
    with open(file=path, mode='r') as f:
        return toml.load(f=f)


def create_workspace(path: str, members: typing.List[str]) -> typing.NoReturn:
    data = {'workspace': {'members': members}}
    os.makedirs(path, exist_ok=True)
    dump_toml(data, f'{path}/Cargo.toml')


def create_crate(path: str) -> typing.NoReturn:
    os.system(f'cargo new {path}')
    os.remove(f'{path}/src/main.rs')
    bin_dir = f'{path}/src/bin/'
    os.makedirs(bin_dir, exist_ok=True)
    with open(file=f'{bin_dir}/sol_0.rs', mode='w') as f: pass


def main() -> typing.NoReturn:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--workspace',
        type=str,
        default='.',
        help='relative path from current directory to workspace.',
        required=False,
    )
    parser.add_argument(
        '-c', '--crates',
        type=str,
        nargs='+',
        help='relative path from current directory (or workspace if specified) to crates.',
        required=True,
    )
    args = parser.parse_args()
    workspace, members = args.workspace, args.crates

    # if workspace is not None:
    create_workspace(workspace, members)

    for member in members:
        path = member if workspace is None else f'{workspace}/{member}'
        create_crate(path)


if __name__ == '__main__':
    main()
