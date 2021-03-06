'use strict';
const fs = require('fs');
const mod = BigInt(1e9+7);

function sum(...a) {var s = 0; for (var x of a) s += x; return s;}
function max(...a) {return a.reduce((x, y) => x>y?x:y)}
function min(...a) {return a.reduce((x, y) => x<y?x:y)}

class ABC001 {
  static A(input) {
    var lines = input.trim().split('\n');
    var [h1, h2] = lines;
    console.log(h1-h2);
  }
  static B(input) {
    var lines = input.trim().split('\n');
  }
  static C(input) {
    var lines = input.trim().split('\n');
  }
  static D(input) {
    var lines = input.trim().split('\n');
  }
}

class ABC002 {
  static A(input) {
    var lines = input.trim().split('\n');
    console.log(max(...lines[0].split(' ').map(x => +x)));
  }
  static B(input) {
    const vowels = new Set('aeiou');
    var a = new Set('a');
    var b = vowels;
    console.log(b);
    console.log(vowels);
    var lines = input.trim().split('\n');
  }
  static C(input) {
    var lines = input.trim().split('\n');
  }
  static D(input) {
    var lines = input.trim().split('\n');
  }
}

class ABC041 {
  static A(input) {
    var s, i
    input = input.trim().split('\n');
    [s, i] = input;
    i = parseInt(i, 10);
    console.log(s[i-1]);
  }
  static B(input) {
    var a, b, c;
    input = input.trim().split(' ').map(BigInt);
    [a, b, c] = input;
    var ans = a * b % mod * c % mod;
    ans = Number(ans);
    console.log(ans);
  }
  static C(input) {
    var [n, height] = input.trim().split('\n');
    height = height.split(' ').map(x => +x);
    n = +n;
    var height = Object.keys(height).map(key => [+key+1, height[key]]);
    height.sort((a, b) => b[1]-a[1]);
    for (var [i, _] of height) {console.log(i);}
  }
  static D(input) {
    var lines = input.trim().split('\n');
    var [n, m] = lines[0].split(' ').map(x => +x);
    var edges = new Array(n).fill(0);
    for (var i = 0; i < m; i++) {
      var [x, y] = lines[1+i].split(' ').map(x => +x);
      edges[x-1] |= 1<<(y-1);
    }
    var comb = new Array(1<<n).fill(null); comb[0] = 1;
    function count(edges, bit) {
      if (comb[bit] != null) {return comb[bit];}
      comb[bit] = 0;
      for (var i = 0; i < n; i++) {
        if (bit>>i&1 && !edges[i]) {
          var nxt_bit = bit & ~(1<<i);
          var nxt_edges = edges.slice();
          for (var j = 0; j < n; j++) {
            nxt_edges[j] &= ~(1<<i);
          }
          comb[bit] += count(nxt_edges, nxt_bit);
        }
      }
      return comb[bit];
    }
    console.log(count(edges, (1<<n)-1));
  }
}

class ABC042 {
  static A(input) {
    var cnt = {};
    var a = input.trim().split(' ').map(x => +x);
    for (var x of a) {
      cnt[x] = cnt[x] ? cnt[x]+1 : 1;
    }
    var ans = cnt[5]==2 && cnt[7]==1 ? 'YES' : 'NO';
    console.log(ans);
  }
  static B(input) {
    var lines = input.trim().split('\n');
    var [n, l] = lines[0].split(' ').map(x => +x);
    var s = lines.slice(1,);
    s.sort();
    console.log(s.join(''));
  }
  static C(input) {

  }
  static D(input) {
  }
}

class ABC173 {
  static A(input) {
    var n = +input.trim();
    console.log(Math.floor((n+999)/1000)*1000 - n);
  }
  static B(input) {
    var lines = input.trim().split('\n');
    var n = +lines[0];
    var cnt = {
      'AC': 0,
      'WA': 0,
      'TLE': 0,
      'RE': 0
    }
    for (var i = 0; i < n; i++) {
      cnt[lines[1+i]]++;
    }
    for (var [verd, c] of Object.entries(cnt)) {
      console.log(`${verd} x ${c}`);
    }
  }
  static C(input) {
    var lines = input.trim().split('\n');
    var [h, w, k] = lines[0].split(' ').map(x => +x);
    var c = lines.slice(1);
    var tot = 0;
    for (var i = 0; i < (1<<h); i++) {
      for (var j = 0; j < (1<<w); j++) {
        var cnt = 0;
        for (var y = 0; y < h; y++) {
          if (i>>y&1) continue;
          for (var x = 0; x < w; x++) {
            cnt += c[y][x]=='#' && !(j>>x&1);
          }
        }
        tot += cnt == k;
      }
    }
    console.log(tot);
  }
  static D(input) {
    var lines = input.trim().split('\n');
    var n = +lines[0];
    var a = lines[1].split(' ').map(x => +x);
    a.sort((a, b) => b-a);
    var m = Math.floor((n-2)/2);
    var s = a[0] + sum(...a.slice(1, 1+m))*2 + (n&1)*a[1+m];
    console.log(s);
  }
  static E(input) {
  }
  static F(input) {
  }
}

var a = {
  a: function() {
    console.log(1)
  }
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
// ABC002.B(input);
a.a();
