import 'dart:io';

void main() async {
  // var n = 1 << 22;
  var n = 1 << 16;
  var ls = List<String>.filled(
    n, '1234567890\n',
  );
  var s = ls.join();
  
  // for (var i = 0; i < n; i++) {
  //   s += '1234567890\n';
  // }
  final filename = 
    '../data/large_input.txt';
  var file = await File(filename).writeAsString(s);
}
