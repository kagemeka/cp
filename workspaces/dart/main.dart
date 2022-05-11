import 'dart:io';
import 'dart:async';
import 'dart:convert';

class Scanner {
  List<String> _tokens = [];
  int _pos = 0;

  Scanner() {
    _readAsync();
  }

  Future<void> _readAsync() async {
    var lines = stdin.transform(utf8.decoder).transform(const LineSplitter());
    await for (final line in lines) {
      if (line == "") break;
      _tokens += line.split(" ");
    }
  }

  Future<String> scanManually() async {
    while (_pos >= _tokens.length) {
      // for manual input.
      await Future.delayed(Duration(milliseconds: 0));
    }
    return _tokens[_pos++];
  }

  Future<int> scanIntManually() async {
    return int.parse(await scanManually());
  }

  String scan() {
    return _tokens[_pos++];
  }

  int scanInt() {
    return int.parse(scan());
  }
}

void main() async {
  var sc = Scanner();
  // print(await sc.scanManually());
  // print(await sc.scanIntManually());
  for (int i = 0; i < 1 << 15; i++) {
    // print(await sc.scanManually());
    await sc.scanManually();
    // sc.scan();
  }
  // print(
}
