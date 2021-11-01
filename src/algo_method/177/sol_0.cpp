#include <iostream>



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int a, n;
  std::cin >> a >> n;
  std::cout << (a | (1 << n)) << '\n';
}