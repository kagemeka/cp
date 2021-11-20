#include <bits/stdc++.h>

template<typename T> class SparseTable_2D {
private:
    const int R, C;
    vector<int> LogTable;
    T**** Table;
public:
    SparseTable_2D(const vector<vector<T> >& v) : R((int)v.size()), C((int)v[0].size()), LogTable(max(R, C) + 1){
        for(int i = 2; i <= max(R, C); ++i){
            LogTable[i] = LogTable[i >> 1] + 1;
        }
        Table = new T***[LogTable[R] + 1];
        for(int k = 0; k <= LogTable[R] ; ++k){
            Table[k] = new T**[LogTable[C] + 1];
            for(int l = 0; l <= LogTable[C]; ++l){
                Table[k][l] = new T*[R];
                for(int i = 0; i < R; ++i){
                    Table[k][l][i] = new T[C];
                }
            }
        }
        for(int i = 0; i < R; ++i){
            for(int j = 0; j < C; ++j){
                Table[0][0][i][j] = v[i][j];
            }
        }
        for(int k = 1; (1 << k) <= R; ++k){
            for(int i = 0; i + (1 << k) <= R; ++i){
                for(int j = 0; j < C; ++j){
                    Table[k][0][i][j] = max(Table[k - 1][0][i][j], Table[k - 1][0][i + (1 << (k - 1))][j]);
                }
            }
        }
        for(int k = 0; (1 << k) <= R; ++k){
            for(int l = 1; (1 << l) <= C; ++l){
                for(int i = 0; i + (1 << k) <= R; ++i){
                    for(int j = 0; j + (1 << l) <= C; ++j){
                        Table[k][l][i][j] = max(Table[k][l - 1][i][j], Table[k][l - 1][i][j + (1 << (l - 1))]);
                    }
                }
            }
        }
    }
    ~SparseTable_2D(){
        for(int i = 0; i <= LogTable[R]; ++i){
            for(int j = 0; j <= LogTable[C]; ++j){
                for(int k = 0; k < R; ++k){
                    delete[] Table[i][j][k];
                }
                delete[] Table[i][j];
            }
            delete[] Table[i];
        }
        delete[] Table;
    }
    T query(const int lx, const int ly, const int rx, const int ry){
        const int kx = LogTable[rx - lx];
        const int ky = LogTable[ry - ly];
        return max({Table[kx][ky][lx][ly], Table[kx][ky][rx - (1 << kx)][ly], Table[kx][ky][lx][ry - (1 << ky)], Table[kx][ky][rx - (1 << kx)][ry - (1 << ky)]});
    }
};


int main() {
  using namespace std;

  int h0, w0, h1, w1, h2, w2;
  cin >> h0 >> w0 >> h1 >> w1 >> h2 >> w2;
  
  vector<vector<long long>> a(h0 + 1, vector<long long>(w0 + 1));
  for (int i = 0; i < h0; i++) {
    for (int j = 0; j < w0; j++) {
      cin >> a[i + 1][j + 1];
    }
  }

  auto s = a;
  for (int i = 0; i < h0; i++) {
    for (int j = 0; j < w0 + 1; j++) {
      a[i + 1][j] += a[i][j];
    }
  }
  for (int j = 0; j < w0; j++) {
    for (int i = 0; i < h0 + 1; i++) {
      a[i][j + 1] += a[i][j];
    }
  }

  h2 = min(h1, h2);
  w2 = min(w1, w2);

  auto s1 = s;
  auto s2 = s;
  for (int i = 0; i < h0 + 1 - h1; i++) {
    for (int j = 0; j < w0 + 1 - w1; j++) {
      s1[i][j] = s[i + h1][j + w1] - s[i + h1][j] - s[i][j + w1] + s[i][j];
    }
  }
  for (int i = 0; i < h0 + 1 - h2; i++) {
    for (int j = 0; j < w0 + 1 - w2; j++) {
      s2[i][j] = s[i + h2][j + w2] - s[i + h2][j] - s[i][j + w2] + s[i][j];
    }
  }
  
  auto sparse1 = SparseTable_2D(s1);

}