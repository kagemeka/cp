#include <bits/stdc++.h>

int dist(int a, int b, int c, int x) {
  return b * (x / (a + c) * a + std::min(x % (a + c), a));
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::string s;
  std::cin >> s;
}
