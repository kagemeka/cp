import functools
import typing




class Accumulate:
    @staticmethod
    def __call__(
        func: typing.Callable,
        identity: int,
    ):
        def fn(
            a: typing.Iterable[int],
        ) -> int:
            return functools.reduce(
                func,
                a,
                identity,
            )
        return fn



T = typing.TypeVar('T')
def accumulate(
    e: T,
) -> typing.Callable[
    [typing.Callable[[T, T], T]],
    typing.Callable[[typing.Iterable[T]], T], 
]:
    def decorate(
        op: typing.Callable[[T, T], T],
    ) -> typing.Callable[[typing.Iterable[T]], T]:
        import functools 
        def wrapped(a: typing.Iterable[T]) -> T:
            return functools.reduce(op, a, e)
        return wrapped
    return decorate

@accumulate(0)
def xor(a: int, b: int) -> int:
    return a ^ b


def main() -> typing.NoReturn:
    print(xor((0, 1, 2, 4)))



if __name__ == '__main__':
    main()