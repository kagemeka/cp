
def fn(i: int) -> int:
  return i ** 2 + 1


def test():
  palette = (
    (1 << 11) - 1, 
    (1 << 15) - 1, 
    (1 << 22) - 1,
  )
  print(palette)
  i = 1
  i = fn(i)
  c = tuple(
    int(p * i % 255)
    for p in palette
  )
  print(c)
  


if __name__ == '__main__':
  test()

