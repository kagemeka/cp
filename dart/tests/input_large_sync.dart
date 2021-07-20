import 'dart:io';

void main()  {
  var lines = <String>[];
  while (true) {
    var line = stdin.readLineSync();
    if (line == null) {
      break;
    }
    lines.add(line); // No more error about `String?`.
  }
  print(lines.length);
}
