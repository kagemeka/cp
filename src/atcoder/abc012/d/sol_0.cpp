#include <iostream>

#include <vector>


namespace graph_theory {
  
template<typename T> struct Edge { const int u, v; T data; };


template<typename T, typename U>
struct SparseDirectedGraph {
  using E = Edge<U>;  // G::E edge{u, v, data};
  std::vector<T> nodes;
  std::vector<std::vector<E>> edges;    
  SparseDirectedGraph(int n) : nodes(n), edges(n) {}
  void add_edge(const E &e) { edges[e.u].push_back(e); }
};


template <typename T, typename U>
struct DenseDirectedGraph {
  std::vector<T> nodes;
  std::vector<std::vector<U>> edges;
  DenseDirectedGraph(int n) : nodes(n), edges(n, std::vector<U>(n)) {}
  std::vector<U>& operator[](int i) { return edges[i]; } 
};


template <typename T, typename U>
struct UndirectedGraph {
  using E = Edge<U>;
  std::vector<T> nodes;
  std::vector<E> edges;
  UndirectedGraph(int n) : nodes(n) {}
  SparseDirectedGraph<T, U> to_directed() const {
    SparseDirectedGraph<T, U> g(nodes.size());
    g.nodes = nodes;
    for (const E &e : edges) {
      g.add_edge(e);
      g.add_edge(E{e.v, e.u, e.data});
    };
    return g;
  }
};

} // graph_theory

// namespace graph_theory::shortest_path::floyd_warshall {
//   void f() {}
// }



#include <limits>


namespace graph_theory::shortest_path::floyd_warshall {

namespace {
  template <typename T> struct Data { T cost; };
  template <typename T> using Graph = DenseDirectedGraph<void *, Data<T>>;
}

template <typename T>
Graph<T> make_graph(int n) {
  T inf = std::numeric_limits<T>::max();
  
}
// template <typename T>
// std::vector<std::vector<T>> floyd_warshall(::Graph<T> g) {

// }

} // 

// namespace graph_theory {
//   namespace shortest_path {
//     template <typename T> struct FloydWarshallData { T cost; };
//     template <typename T> using FloydWarshallGraph = DenseDirectedGraph<Void *, FloydWarshallData<T>>;

//     template <typename T>
//     FloydWarshallGraph<T> make_floyd_warshall_graph(int n) {
//       T inf = std::numeric_limits<T>::max();
      
//     }
//     template <typename T>
//     std::vector<std::vector<T>> floyd_warshall(FloydWarshallGraph<T> g) {

//     }
//   }
// } // kagemeka::graph_theory::shortest_path::


int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  // int n, m; std::cin >> n >> m;
  using G = graph_theory::shortest_path::floyd_warshall::Graph<long long>;

}