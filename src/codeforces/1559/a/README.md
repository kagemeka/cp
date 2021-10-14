# [A. Mocha and Math](https://codeforces.com/contest/1559/problem/A)




# keywords 
- greedy




# summary
- at first, left -> right, $\forall{i}\in{i \lt n},  a_{i + 1} = a_{i + 1} \land a_{i}$
- next, right -> left, $\forall{i}\in{i \gt 1},  a_{i - 1} = a_{i - 1} \land a_{i}$
- all values become $a_1 \land a_2 \land ... \land a_n$