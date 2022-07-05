
#include <bits/stdc++.h>

using namespace std;

template <typename T, int n>
struct matrix {
  array<T, n * n> d;
  auto operator[](pair<int, int> idx) -> T& {
    auto [i, j] = idx;
    return d[i * n + j];
  }
  // matrix() {
  //   for (int i = 0; i < N; i++) dat[i].fill(T(0));
  // }
  // static auto eye() -> matrix {
  //   matrix res;
  //   for (int i = 0; i < N; i++) res[i][i] = 1;
  //   return res;
  // }
  // auto operator+(const matrix& A) const -> matrix {
  //   matrix res;
  //   for (int i = 0; i < N; i++)
  //     for (int j = 0; j < N; j++) res[i][j] = dat[i][j] + A[i][j];
  //   return res;
  // }
  // auto operator*(const matrix& A) const -> matrix {
  //   matrix res;
  //   for (int i = 0; i < N; i++)
  //     for (int k = 0; k < N; k++)
  //       for (int j = 0; j < N; j++) res[i][j] += dat[i][k] * A[k][j];
  //   return res;
  // }
  // auto pow(long long n) const -> matrix {
  //   matrix a = *this, res = eye();
  //   for (; n; a = a * a, n >>= 1)
  //     if (n & 1) res = res * a;
  //   return res;
  // }
};
