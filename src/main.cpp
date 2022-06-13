#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <optional>
#include <stdexcept>
#include <type_traits>
#include <vector>

namespace dsalgo::rust_types {
using u8 = uint8_t;
using u16 = uint16_t;
using u32 = uint32_t;
using u64 = uint64_t;
using u128 = __uint128_t;
using i8 = int8_t;
using i16 = int16_t;
using i32 = int32_t;
using i64 = int64_t;
using i128 = __int128_t;
using usize = std::size_t;
using isize = std::make_signed<std::size_t>::type;
using f32 = float;
using f64 = double;
using f128 = __float128;

template <typename T>
using vec = std::vector<T>;

} // namespace dsalgo::rust_types

using namespace dsalgo::rust_types;

namespace dsalgo::iteration_macro {

#define range(i, lo, hi, step) for (int i = lo; i < hi; i += step)
#define repeat(times) for (int _ = 0; _ < times; ++_)
#define loop while (true)

} // namespace dsalgo::iteration_macro

namespace dsalgo::euclidean_modular_gcd_inv {
using namespace dsalgo::rust_types;

// return pair(g: gcd(mod, n), x: inverse(n / g) \mod (mod / g))
auto euclidean_mod_gcd_inv(u64 mod, u64 n) -> std::pair<u64, u64> {
  assert(0 < n && n < mod);
  i64 a = n, b = mod;
  i64 x00 = 1, x01 = 0;
  while (b) {
    x00 -= a / b * x01;
    std::swap(x00, x01);
    a %= b;
    std::swap(a, b);
  }
  u64 gcd = a;
  u64 u = mod / gcd;
  if (x00 < 0) x00 += u;
  assert(0 <= x00 && x00 < (i64)u);
  return {gcd, x00};
}

} // namespace dsalgo::euclidean_modular_gcd_inv

namespace dsalgo {

// return pair(g: gcd(mod, n), x: inverse(n / g) \mod (mod / g))
auto extgcd_modinv(int64_t mod, int64_t n)
    -> std::pair<int64_t, std::optional<int64_t>> {
  assert(mod > 1 && 0 <= n && n < mod);
  if (n == 0) return {mod, std::nullopt};
  auto a = n, b = mod;
  int64_t x00 = 1, x01 = 0;
  while (b) {
    auto q = a / b, r = a % b;
    x00 -= q * x01;
    std::swap(x00, x01);
    a = b;
    b = r;
  }
  auto gcd = a;
  if (x00 < 0) x00 += mod / gcd;
  assert(0 <= x00 && x00 < mod / gcd);
  return {gcd, x00};
}

template <uint32_t v, std::enable_if_t<2 <= v>* = nullptr>
struct static_mod {
  static constexpr auto get() -> uint32_t { return value; }

private:
  static constexpr uint32_t value = v;
};

template <typename I>
struct dynamic_mod {
  static constexpr auto get() -> uint32_t { return value; }
  static constexpr void set(uint32_t v) {
    assert(2 <= v);
    value = v;
  }

private:
  static uint32_t value;
};
template <typename I>
uint32_t dynamic_mod<I>::value;

template <typename M>
class modular {
  uint32_t value;
  constexpr static auto mod() -> uint32_t { return M::get(); }
  static auto normalize(const int64_t& x) -> uint32_t {
    return (x % mod() + mod()) % mod();
  }

public:
  constexpr modular() : value() {}
  modular(const uint64_t& x) { value = normalize(x); }
  auto operator()() const -> const uint32_t& { return value; }
  template <typename T>
  explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> modular { return modular(mod() - value); }
  auto operator+=(const modular& rhs) -> modular& {
    uint64_t v = (uint64_t)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  auto operator-=(const modular& rhs) -> modular& {
    uint64_t v = value;
    if (v < rhs.value) v += mod();
    value = v - rhs.value;
    return *this;
  }
  auto operator++() -> modular& { return *this += 1; }
  auto operator--() -> modular& { return *this -= 1; }
  auto operator++(int) -> modular {
    modular res(*this);
    *this += 1;
    return res;
  }
  auto operator--(int) -> modular {
    modular res(*this);
    *this -= 1;
    return res;
  }
  auto operator*=(const modular& rhs) -> modular& {
    value = (uint64_t)value * rhs.value % mod();
    return *this;
  }

  auto mul_inv() const -> std::optional<modular> {
    auto [g, inv] = extgcd_modinv(mod(), value);
    if (g != 1) return std::nullopt;
    return inv;
  }

  auto operator/=(const modular& rhs) -> modular& {
    if (auto inv = rhs.mul_inv()) {
      return *this *= *inv;
    } else {
      throw;
    }
  }

  friend auto operator+(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) += rhs;
  }
  friend auto operator-(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) -= rhs;
  }
  friend auto operator*(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) *= rhs;
  }
  friend auto operator/(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) /= rhs;
  }
  friend auto operator==(const modular& lhs, const modular& rhs) -> bool {
    return lhs.value == rhs.value;
  }
  friend auto operator!=(const modular& lhs, const modular& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& is, modular& x) -> std::istream& {
    int64_t v;
    is >> v;
    x.value = normalize(v);
    return is;
  }
  friend auto operator<<(std::ostream& os, const modular& x) -> std::ostream& {
    return os << x.value;
  }
};

using mint1000000007 = modular<static_mod<1000000007>>;
using mint998244353 = modular<static_mod<998244353>>;

template <typename S, typename G>
auto pow_semigroup_recurse(const S& s, uint64_t n) -> S {
  assert(n > 0);
  if (n == 1) return s;
  S x = pow_semigroup_recurse<S, G>(s, n >> 1);
  x = G::operate(x, x);
  if (n & 1) x = G::operate(x, s);
  return x;
}

template <typename S, typename G>
auto pow_semigroup(S s, uint64_t n) -> S {
  assert(n > 0);
  S x = s;
  --n;
  while (n > 0) {
    if (n & 1) x = G::operate(x, s);
    s = G::operate(s, s);
    n >>= 1;
  }
  return x;
}

template <typename S, typename M>
auto pow_monoid(const S& s, uint64_t n) -> S {
  if (n == 0) return M::identity();
  return pow_semigroup<S, M>(s, n);
}

template <typename S, typename G>
auto pow_group(const S& s, int64_t n) -> S {
  return n >= 0 ? pow_monoid<S, G>(s, n) : pow_monoid<S, G>(G::invert(s), -n);
}

template <typename S, S (*op)(S, S)>
auto accumulate(std::vector<S> v) -> std::vector<S> {
  for (int i = 0; i < (int)v.size(); ++i) {
    v[i + 1] = op(v[i], v[i + 1]);
  }
  return v;
}

template <typename T>
auto mul(T a, T b) -> T {
  return a * b;
}

template <typename S>
auto factorial_table(usize size) -> std::vector<S> {
  assert(size > 0);
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 0);
  v[0] = 1;
  return accumulate<S, mul<S>>(v);
}

template <typename S>
auto inverse_factorial_table(usize size) -> std::vector<S> {
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 1);
  v[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  reverse(v.begin(), v.end());
  v = accumulate<S, mul<S>>(v);
  reverse(v.begin(), v.end());
  return v;
}

template <typename S>
class combination {
  std::vector<S> fact, inv_fact;

public:
  combination(usize size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }
  auto operator()(usize n, usize k) -> S {
    if (n < k) return 0;
    return fact[n] * inv_fact[k] * inv_fact[n - k];
  }

  auto inverse(usize n, usize k) -> S {
    if (n < k) return 0;
    return inv_fact[n] * fact[k] * fact[n - k];
  }
};

template <typename S>
class homogeneous_product {
  combination<S> choose;

public:
  homogeneous_product(usize size) : choose(size) {}
  auto operator()(usize n, usize k) -> S {
    return n == 0 ? 0 : choose(n + k - 1, k);
  }
};

template <typename mint>
struct mod_mul {
  static auto operate(const mint& a, const mint& b) -> mint { return a * b; }
  static auto identity() -> mint { return 1; }
  static auto invert(const mint& a) -> mint { return 1 / a; }
};

template <typename T>
auto pascal_triangle(usize size) -> std::vector<std::vector<T>> {
  std::vector<std::vector<T>> p(size, std::vector<T>(size, 0));
  for (usize i = 0; i < size; ++i) p[i][0] = 1;
  for (usize i = 1; i < size; ++i) {
    for (usize j = 1; j < size; ++j) {
      p[i][j] = p[i - 1][j - 1] + p[i - 1][j];
    }
  }
  return p;
}

template <typename T>
class cached_pascal_triangle {
  std::unordered_map<unsigned long long int, T> cache;

public:
  cached_pascal_triangle() = default;

  auto operator()(usize n, usize k) -> T {
    if (n < k) return 0;
    if (k == 0) return 1;
    unsigned long long int key = (unsigned long long int)n << 32 | k;
    if (cache.count(key) == 0) {
      cache[key] = (*this)(n - 1, k - 1) + (*this)(n - 1, k);
    }
    return cache[key];
  }
};

template <typename T>
auto floyd_warshall(const vec<vec<T>>& min_edge_matrix) -> vec<vec<T>> {
  auto dist = min_edge_matrix;
  usize n = dist.size();
  for (usize i = 0; i < n; ++i) assert(dist[i].size() == n);
  for (usize i = 0; i < n; ++i) {
    dist[i][i] = std::min(dist[i][i], 0);
  }
  for (usize k = 0; k < n; ++k) {
    for (usize i = 0; i < n; ++i) {
      for (usize j = 0; j < n; ++j) {
        dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  for (usize i = 0; i < n; ++i) {
    if (dist[i][i] < 0) {
      throw std::logic_error("negative cycle found.");
    }
  }
  return dist;
}
} // namespace dsalgo

namespace dsalgo::debug_print {

template <typename T>
void print(vec<T> v) {
  for (usize i = 0; i < v.size(); ++i) {
    std::cout << v[i] << " \n"[i == v.size() - 1];
  }
}

template <typename T>
void print(const T& t) {
  std::cout << t << '\n';
}

template <typename T, typename... U>
void print(const T& t, const U&... args) {
  std::cout << t << ' ';
  print(args...);
}

template <typename T, typename... U>
void print(char sep, const T& t, const U&... args) {
  if (sizeof...(args) > 0) {
    std::cout << t << sep;
    print(sep, args...);
  } else {
    print(t);
  }
}

#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif

void _test_debug() {
  int a = 0, b = 2, c = 3;
  debug(a, b, c);

  vec<int> v{1, 2, 3, 4, 5};
  debug(v);
  debug(a, v);
  usize d = 0;
  print(d);
  repeat(10) { print(_); }
  range(i, 0, 10, 2) { print(i); }

  int i = 0;
  loop {
    i += 1;
    print(i);
    if (i == 10) break;
  }
}

} // namespace dsalgo::debug_print

namespace dsalgo::bit_length {

auto bit_length(u32 x) -> u8 { return 32 - __builtin_clz(x); }

auto bit_length(u64 x) -> u8 { return 64 - __builtin_clzll(x); }

auto bit_length(u128 x) -> u8 {
  return x >> 64 == 0 ? bit_length((u64)x) : bit_length((u64)(x >> 64)) + 64;
}

} // namespace dsalgo::bit_length

namespace dsalgo::prime_number_theorem {
using namespace rust_types;
using bit_length::bit_length;

auto prime_pi_approx_ln(u128 n) -> u128 {
  if (n < 2) return 0;
  return n * 3 / bit_length(n) >> 1;
}

} // namespace dsalgo::prime_number_theorem

namespace dsalgo::sieve_of_eratosthenes {
using namespace rust_types;

auto sieve_of_eratosthenes(usize size) -> vec<u32> {
  vec<u32> primes;
  primes.reserve(size >> 4);
  if (size > 2) primes.push_back(2);
  vec<bool> is_prime(size >> 1, true);
  for (usize i = 3; i < size; i += 2) {
    if (!is_prime[i >> 1]) continue;
    primes.emplace_back(i);
    for (usize j = i * i >> 1; j < size >> 1; j += i) is_prime[j] = false;
  }
  return primes;
}

} // namespace dsalgo::sieve_of_eratosthenes

using namespace dsalgo::debug_print;
auto main() -> int {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  using namespace std;
  using namespace dsalgo;
  using namespace dsalgo::prime_number_theorem;
  using sieve_of_eratosthenes::sieve_of_eratosthenes;

  auto primes = sieve_of_eratosthenes(100);
  print(primes);

  // int n, m;
  // cin >> n >> m;

  // constexpr int inf = 1 << 29;
  // vector<vector<int>> dist(n, vector<int>(n, inf));
  // for (int i = 0; i < m; ++i) {
  //   int a, b, t;
  //   cin >> a >> b >> t;
  //   --a;
  //   --b;
  //   dist[a][b] = t;
  //   dist[b][a] = t;
  // }
  // for (int i = 0; i < n; i++) {
  //   for (int j = 0; j < n; j++) {
  //     assert(dist[i][j] >= 0);
  //   }
  // }

  // dist = floyd_warshall(dist);

  // int mn = inf;

  // for (int i = 0; i < n; ++i) {
  //   mn = min(mn, *max_element(dist[i].begin(), dist[i].end()));
  // }
  // cout << mn << endl;
}
