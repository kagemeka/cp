fun joinOptions(options: Collection<String>): String {
  return options.joinToString(prefix="[", postfix="]")
}


fun main() {
  var a = listOf("a", "b")
  var s = joinOptions(a)
  println(s)
}