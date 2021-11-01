#include <iostream>



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n = 9;
  int cnt = 0;
  for (int i = 0; i < 5; i++) cnt += n >> i & 1;
  std::cout << cnt << '\n';
}