import Foundation

private func readStrings() -> [String] {
  return readLine()!.split(separator: " ").map { String($0) }
}
private class Scanner {
  private var tokens: [String] = []
  init() {}
  func str() -> String {
    while tokens.isEmpty { tokens = readStrings().reversed() }
    return tokens.popLast()!
  }
  func strs(_ n: Int) -> [String] { return (0..<n).map { _ in str() } }
  func int() -> Int { return Int(str())! }
  func ints(_ n: Int) -> [Int] { return (0..<n).map { _ in int() } }
  func intMatrix(_ h: Int, _ w: Int) -> [[Int]] {
    return (0..<h).map { _ in (0..<w).map { _ in int() } }
  }
}

private func printArr<T>(_ a: [T]) {
  let n = a.count
  for i in 0..<n { print(a[i], terminator: i == n - 1 ? "\n" : " ") }
}

func zAlgorithm<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var lcp = [Int](repeating: 0, count: n)
  var l = 0
  for i in 1..<n {
    let r = l + lcp[l]
    var d = r <= i ? 0 : min(lcp[i - l], r - i)
    while i + d < n && a[i + d] == a[d] { d += 1 }
    lcp[i] = d
    if r < i + d { l = i }
  }
  lcp[0] = n
  return lcp
}

func zAlgorithmFindAll<T: Comparable>(_ a: [T], _ pattern: [T]) -> [Int] {
  let p = pattern
  let (n, m) = (a.count, p.count)
  let z = Array(zAlgorithm(p + a)[m...])
  var indices = [Int]()
  for i in 0..<n where z[i] >= m { indices.append(i) }
  return indices
}

func main() {
  // let sc = Scanner()
  // let s = sc.str()
  // let t = sc.str()
  print(zAlgorithmFindAll(Array("ababababc"), Array("aba")))
}

main()
