#include <iostream>
#include <vector>


int main() {
  using namespace std;
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int h, w; cin >> h >> w;
  vector<vector<int>> c(h, vector<int>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> c[i][j];
    }
  }
}