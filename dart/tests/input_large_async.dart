import 'dart:async';
import 'dart:io';
import 'dart:convert';

void main() async {
  // readLine().listen(processLine);
  var fn = InputAll();
  var ls = fn();
  // sleep(Duration(seconds: 1));
  print(ls);
}


class InputAll 
{
  List<String> ls = ['a',];
  int i = 0;
  List<String> call() {
    readLine().listen(
      processLine,
    );
    print(i);
    return ls;
  }


  Stream<String> readLine() => stdin
      .transform(utf8.decoder)
      .transform(const LineSplitter());

  void processLine(
    String line,
  ) {
    ls.add(line);
    ls[0] = line;
    // print(line);
    i += 1;
  }
}



// dart input_large.dart \
// < ../data/large_input.txt