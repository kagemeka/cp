#include <iostream>
#include <vector>
#include <set>



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m, q;
  std::cin >> n >> m >> q;

  std::vector<std::vector<int>> g(n, std::vector<int>(n));
  for (int i = 0; i < m; i++) {
    int a, b, f;
    std::cin >> a >> b >> f;
    --a; --b;
    g[a][b] = g[b][a] = f;
  }

  std::vector<std::vector<int>> connected(n, std::vector<int>(n));

  std::vector<int> res; res.reserve(q);
  std::multiset<int> ms;
  while (q--) {
    char op;
    int x;
    std::cin >> op >> x;
    --x;
    for (int i = 0; i < n; i++) {
      if (i == x) continue;
      if (connected[x][i]) {
        ms.erase(ms.find(-g[x][i]));
      } else {
        ms.insert(-g[x][i]);
      }
      connected[x][i] ^= 1;
      connected[i][x] ^= 1;
    }
    res.push_back(-*ms.begin());
  }
  for (const int &x : res) {
    std::cout << x << '\n';
  }

}
