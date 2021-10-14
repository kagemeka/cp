#include  <bits/stdc++.h>
using namespace std;


template<typename T>
double triangle_area(pair<T,T> p0, pair<T,T> p1, pair<T,T> p2, bool sign=true) {
  T x0 = p1.first - p0.first;
  T x1 = p2.first - p0.first;
  T y0 = p1.second - p0.second;
  T y1 = p2.second - p0.second;
  double s = (x0*y1 - x1*y0)/2.;
  return (sign ? s : abs(s));
}


int main() {
  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  pair<int, int> p0, p1, p2;
  p0 = make_pair(a, b);
  p1 = make_pair(c, d);
  p2 = make_pair(e, f);
  auto s = triangle_area(p0, p1, p2, false);
  cout << setprecision(16)  << s <<'\n';
}