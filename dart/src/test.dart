
abstract class Solver {
  void prepare() {}
  void solve() {}
}



mixin Run<T extends Solver> {
  void call() {
    var sol = this as T;
    sol.prepare();
    sol.solve();
  }
}



class Problem
with Run<Problem>, IO
implements Solver {
  void prepare() {
  }

  void solve() {
  }
}



void main() async {
  var p = new Problem();
  p();
}