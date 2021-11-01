#include <iostream>



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::cout << 1;
  for (int i = 0; i < n; i++) std::cout << 0;
  std::cout << '\n';
}