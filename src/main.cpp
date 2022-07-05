#include <bits/stdc++.h>
using namespace std;

template<typename T, typename A>
auto count_common_subsequences(const A& a, const A& b) -> T {
  int n = a.size(), m = b.size();
  vector<T> dp(m + 1, 1);
  for(int i = 0; i < n; i++) {
    for(int j = m - 1; j >= 0; j--) dp[j + 1] -= dp[j] * (a[i] != b[j]);
    for(int j = 0; j < m; j++) dp[j + 1] += dp[j];
  }
  return dp[m];
}

template<typename T, T v, std::enable_if_t<(v > 0)>* = nullptr>
struct const_mod {
  static constexpr auto get() -> T { return v; }
};

template<typename M> struct modint {
  using T = typename std::decay<decltype(M::get())>::type;

  T value;

  using Self = modint;

  constexpr static auto m() -> T { return M::get(); }

  template<typename U> constexpr static auto norm(U x) -> T {
    return (x % m() + m()) % m();
  }

  constexpr modint(): value() {}

  template<typename U> modint(U x): value(norm(x)) {}

  auto operator()() -> const T& { return value; }

  template<typename T> explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> Self {
    return Self(value == 0 ? value : m() - value);
  }

  auto operator+=(Self& rhs) -> Self& {
    value += rhs.value;
    value -= (value >= m()) * m();
    return *this;
  }

  friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
    T v;
    stream >> v;
    x.value = norm(v);
    return stream;
  }

  friend auto operator<<(std::ostream& stream, Self const& x) -> std::ostream& {
    return stream << x.value;
  }

  friend auto operator+(Self& lhs, Self& rhs) -> Self {
    return Self(lhs) += rhs;
  }
};

template<typename T> auto operator+(T& a, T& b) -> T { return T(a) += b; }

template<typename T> auto operator-(T& a, T& b) -> T { return T(a) -= b; }

template<typename T> auto operator*(T& a, T& b) -> T { return T(a) *= b; }

template<typename T> auto operator/(T& a, T& b) -> T { return T(a) /= b; }

// template <typename A> // Arithmetic
// class modular_int {

//   T value;
//   using Self = modular_int;
//   constexpr static auto mod() -> T { return A::mod(); }

//   template <typename U>
//   constexpr static auto norm(const U& x) -> T {
//     return (x % mod() + mod()) % mod();
//   }

// public:
//   constexpr modular_int() : value() {}

//   template <typename U>
//   modular_int(const U& x) {
//     value = norm(x);
//   }

//   auto operator()() const -> const T& { return value; }
//   template <typename T>
//   explicit operator T() const {
//     return static_cast<T>(value);
//   }

//   auto operator-() const -> Self { return Self(A::neg(value)); }
//   auto operator+=(const Self& rhs) -> Self& {
//     value = A::add(value, rhs.value);
//     return *this;
//   }
//   auto operator-=(const Self& rhs) -> Self& { return *this += -rhs; }
//   auto operator++() -> Self& { return *this += 1; }
//   auto operator--() -> Self& { return *this -= 1; }
//   auto operator++(int) -> Self {
//     Self res(*this);
//     *this += 1;
//     return res;
//   }
//   auto operator--(int) -> Self {
//     Self res(*this);
//     *this -= 1;
//     return res;
//   }
//   auto operator*=(const Self& rhs) -> Self& {
//     value = A::mul(value, rhs.value);
//     return *this;
//   }

//   [[nodiscard]] auto inv() const -> Self { return Self(A::inv(value)); }

//   auto operator/=(const Self& rhs) -> Self& { return *this *= rhs.inv(); }

//   friend auto operator+(const Self& lhs, const Self& rhs) -> Self {
//     return Self(lhs) += rhs;
//   }
//   friend auto operator-(const Self& lhs, const Self& rhs) -> Self {
//     return Self(lhs) -= rhs;
//   }
//   friend auto operator*(const Self& lhs, const Self& rhs) -> Self {
//     return Self(lhs) *= rhs;
//   }
//   friend auto operator/(const Self& lhs, const Self& rhs) -> Self {
//     return Self(lhs) /= rhs;
//   }
//   friend auto operator==(const Self& lhs, const Self& rhs) -> bool {
//     return lhs.value == rhs.value;
//   }
//   friend auto operator!=(const Self& lhs, const Self& rhs) -> bool {
//     return lhs.value != rhs.value;
//   }

//   friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
//     T v;
//     stream >> v;
//     x.value = norm(v);
//     return stream;
//   }
//   friend auto operator<<(std::ostream& stream, const Self& x) ->
//   std::ostream& {
//     return stream << x.value;
//   }
// };

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;
  using mint = modint<const_mod<int, 1000000007>>;

  vector<mint> a(n), b(m);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < m; i++) cin >> b[i];

  a[1] = a[1] + a[0];
  cout << a[1] << endl;

  // cout << (dp[m] + mod) % mod << endl;
}
