'use strict';



class IO {

  private fs: (
    any
  ) = require(
    'fs',
  )

  chunks: Generator;


  private readStdin(): (
    string
  ) {
    const fs = this.fs
    return fs.readFileSync(
      '/dev/stdin',
      'utf8',
    );
  }


  private toChunks(
    s: string,
  ): (
    string[]
  ) {
    return (
      s.trim().split(/ |\n/)
    );
  }


  private *toGen(
    chunks: string[],
  ): (
    Generator
  ) {
    for (var c of chunks) {
      yield c;
    }
  }


  constructor() {
    const fs = this.fs;
    const chunks: (
      string[]
    ) = this.toChunks(
      this.readStdin(),
    );
    this.chunks = this.toGen(
      chunks,
    );
  }


  read(): string {
    return (
      this.chunks.next().value
    );
  }


  readInt(): number {
    return +this.read();
  }
}



abstract class Solver {

  io: IO;


  constructor() {
    this.io = new IO();
  }


  abstract prepare(): void;


  abstract solve(): void;


  run(): void {
    this.prepare();
    this.solve();
  }
}



class Problem
extends Solver {


  prepare(): void {
    const io = this.io;
  }


  solve(): void {
  }
}



function main() {
  new Problem().run();
}


main()
