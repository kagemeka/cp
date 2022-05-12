#include <cassert>
#include <cstdint>
#include <iostream>
#include <type_traits>
#include <vector>

template <uint32_t v, std::enable_if_t<2 <= v>* = nullptr> struct static_mod {
  static constexpr uint32_t get() { return value; }

private:
  static constexpr uint32_t value = v;
};

template <typename I> struct dynamic_mod {
  static constexpr uint32_t get() { return value; }
  static constexpr void set(uint32_t v) {
    assert(2 <= v);
    value = v;
  }

private:
  static uint32_t value;
};
template <typename I> uint32_t dynamic_mod<I>::value;

template <typename M> class modular {
  uint32_t value;
  constexpr static uint32_t mod() { return M::get(); }
  static uint32_t normalize(const int64_t& x) { return (x % mod() + mod()) % mod(); }

public:
  constexpr modular() : value() {}
  modular(const uint64_t& x) { value = normalize(x); }
  const uint32_t& operator()() const { return value; }
  template <typename T> explicit operator T() const { return static_cast<T>(value); }

  modular& operator+=(const modular& rhs) {
    uint64_t v = (uint64_t)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  modular& operator-=(const modular& rhs) {
    uint64_t v = value;
    if (v < rhs.value) v += mod();
    value = v - rhs.value;
    return *this;
  }
  modular& operator++() { return *this += 1; }
  modular& operator--() { return *this -= 1; }
  modular operator++(int) {
    modular res(*this);
    *this += 1;
    return res;
  }
  modular operator--(int) {
    modular res(*this);
    *this -= 1;
    return res;
  }
  modular operator-() const { return modular(mod() - value); }
  modular& operator*=(const modular& rhs) {
    value = (uint64_t)value * rhs.value % mod();
    return *this;
  }
  // TODO: enable inverse() method and division operator if mod() is prime.
  // Modular inverse() const { return pow(*this, mod() - 2); }
  //   Modular &operator/=(const Modular &rhs) {
  //     *this *= rhs.inverse();
  //     return *this;
  //   }

  friend modular operator+(const modular& lhs, const modular& rhs) { return modular(lhs) += rhs; }
  friend modular operator-(const modular& lhs, const modular& rhs) { return modular(lhs) -= rhs; }
  friend modular operator*(const modular& lhs, const modular& rhs) { return modular(lhs) *= rhs; }
  friend bool operator==(const modular& lhs, const modular& rhs) { return lhs.value == rhs.value; }
  friend bool operator!=(const modular& lhs, const modular& rhs) { return lhs.value != rhs.value; }

  friend std::istream& operator>>(std::istream& is, modular& x) {
    int64_t v;
    is >> v;
    x.value = normalize(v);
    return is;
  }
  friend std::ostream& operator<<(std::ostream& os, const modular& x) { return os << x.value; }
};

using mint1000000007 = modular<static_mod<1000000007>>;
using mint998244353 = modular<static_mod<998244353>>;

template <typename S, typename G> S pow_semigroup_recurse(const S& s, uint64_t n) {
  assert(n > 0);
  if (n == 1) return s;
  S x = pow_semigroup_recurse<S, G>(s, n >> 1);
  x = G::operate(x, x);
  if (n & 1) x = G::operate(x, s);
  return x;
}

template <typename S, typename G> S pow_semigroup(S s, uint64_t n) {
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

template <typename S, typename M> S pow_monoid(const S& s, uint64_t n) {
  if (n == 0) return M::identity();
  return pow_semigroup<S, M>(s, n);
}

template <typename S, typename G> S pow_group(const S& s, int64_t n) {
  return n >= 0 ? pow_monoid<S, G>(s, n) : pow_monoid<S, G>(G::invert(s), -n);
}

using mint = mint1000000007;

struct mod_mul {
  static mint operate(const mint& a, const mint& b) { return a * b; }
  static mint identity() { return 1; }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  using namespace std;

  int n;
  cin >> n;

  const int K = 1 << 17;

  vector<int> count(K);
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    ++count[a];
  }

  // harmonic series
  for (int i = 1; i < K; i++) {
    for (int j = i * 2; j < K; j += i) {
      count[i] += count[j];
    }
  }
  vector<mint> res(K);
  for (int i = 0; i < K; i++) {
    res[i] = pow_monoid<mint, mod_mul>(2, count[i]) - 1;
  }
  // mobius transform
  for (int i = K - 1; i > 0; i--) {
    for (int j = i * 2; j < K; j += i) {
      res[i] -= res[j];
    }
  }

  mint tot = 0;
  for (int i = 0; i < K; i++) {
    tot += res[i] * i;
  }
  cout << tot << '\n';
}
