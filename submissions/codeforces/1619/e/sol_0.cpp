#include <iostream>
#include <vector>
#include <set>
#include <cassert>

int main() {
  using namespace std;
  // ios::sync_with_stdio(false);
  // cin.tie(nullptr);

  int t; cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<bool> exist(n + 1, false);
    vector<int> cnt(n + 1, 0);
    for (int x: a) {
      exist[x] = true;
      cnt[x]++;
    }
    vector<int> s = cnt;
    for (int i = 0; i < n; i++) {
      s[i + 1] += s[i];
      exist[i + 1] = exist[i + 1] & exist[i];
    }
    vector<int> res(n + 1, -1);

    int c = 0;
    res[0] = cnt[0];
    set<int> idx;
    if (cnt[0] >= 2) idx.insert(0);
    for (int i = 1; i < n + 1; i++) {
      if (exist[i - 1]) {
        res[i] = cnt[i];
        if (cnt[i] >= 2) idx.insert(i);
        continue;
      }
      if (s[i - 1] <= i - 1) break;
      if (cnt[i - 1] >= 1) {
        if (cnt[i] >= 2) idx.insert(i);
        res[i] = c + cnt[i];
        continue;
      }
      int j = *idx.rbegin();
      c += i - 1 - j;
      cnt[j]--;
      cnt[i - 1]++;
      if (cnt[j] <= 1) {
        idx.erase(j);
      };
      res[i] = c + cnt[i];
      if (cnt[i] >= 2) idx.insert(i);
    }
    for (int i = 0; i < n; i++) {
      cout << res[i] << ' ';
    }
    cout << res[n] << '\n';
  }

}
