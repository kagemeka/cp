#include <bits/stdc++.h>

void solve()
{
  using namespace std;
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;

  vector<int> a(n);
  vector<int> b(n);
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = 0; i < n; i++)
    cin >> b[i];

  int k = 20;
  vector<vector<long long>> cnt_a_by_bitlength(k + 1, vector<long long>(k, 0));
  vector<vector<long long>> cnt_b_by_bitlength(k + 1, vector<long long>(k, 0));
  vector<long long> cnt_a(k, 0), cnt_b(k, 0), cnt_a_length(k + 1, 0), cnt_b_length(k + 1, 0);

  for (int x : a)
  {
    int l = 0;
    while (1 << l <= x)
      l++;

    cnt_a_length[l]++;
    for (int i = 0; i < k; i++)
    {
      cnt_a_by_bitlength[l][i] += x >> i & 1;
      cnt_a[i] += x >> i & 1;
    }
  }

  for (int x : b)
  {
    int l = 0;
    while (1 << l <= x)
      l++;

    cnt_b_length[l]++;
    for (int i = 0; i < k; i++)
    {
      cnt_b_by_bitlength[l][i] += x >> i & 1;
      cnt_b[i] += x >> i & 1;
    }
  }

  long long tot = 0;

  for (int i = 0; i < k; i++)
  {
    tot += (1 << i) * (cnt_a[i] * (n - cnt_b[i]) + cnt_b[i] * (n - cnt_a[i]));
  }

  for (int l = 0; l < k + 1; l++)
  {
    for (int i = 0; i < k; i++)
    {
      tot -= (1 << i) * (cnt_a_by_bitlength[l][i] * (cnt_b_length[l] - cnt_b_by_bitlength[l][i]) + cnt_b_by_bitlength[l][i] * (cnt_a_length[l] - cnt_a_by_bitlength[l][i]));

      tot += (1 << i) * (cnt_a_by_bitlength[l][i] * cnt_b_by_bitlength[l][i]);
    }
  }
  cout << tot << endl;
}

int main()
{
  using namespace std;

  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    solve();
  }
  return 0;
}