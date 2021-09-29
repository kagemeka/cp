# [AtCoder ABC003 D - AtCoder社の冬](https://atcoder.jp/contests/abc003/tasks/abc003_4)


# keywords 


# summary
$$
|A \cap B| \\
= |A \cup B| - |\overline{A} \cup \overline{B}| \\
= |A \cup B| - |\overline{A}| + |\overline{B}| - |\overline{A} \cap \overline{B}| \\
$$
- $\because$ inclusion-exclution principle
  - $|A \cup B| = |A|+ |B| - |A \cap B|$
  - $|A \cup B| = |A| + |B| + |C| - |A\cap B| - |B\cap C| - |C\cap A| + |A\cap B\cap C|$
  - $|\cup_{i=1}^{n}A_i| = \sum_{j=1}^{n}{((-1)^{j - 1}\sum_{S\prime \subseteq{S}, |S\prime| = j}{|\cap_{i\in S\prime}{A_i}|})} = \sum_i{|A_i|} - \sum_{i\lt j}{|A_i \cap A_j|} + \sum_{i\lt j\lt k}{|A_i \cap A_j \cap A_k|} + ... + (-1)^{n - 1}|A_1 \cap A_2 \cap ... \cap A_n|$

- let 
  - $A_0 :=$ patterns in which at least one item is placed at north space.
  - $A_1 :=$ patterns in which at least one item is placed at south space.
  - $A_2 :=$ patterns in which at least one item is placed at west space.
  - $A_3 :=$ patterns in which at least one item is placed at east space.

- we want to calculate $|\cap_{i=0}^{3}A_i|$
$$
|\cap_{i=0}^{3}A_i| \\
= |\cup_{i=0}^{3}A_i| - |\cup_{i=0}^{3}\overline{A_i}| \\
= \sum_{j=1}^{4}{((-1)^{j - 1}\sum_{S\prime \subseteq{S}, |S\prime| = j}{|\cap_{i\in S\prime}{\overline{A_i}}|})}
$$


# code 
## sol_0, sol_1, sol_2
- python


# similar 


# references
- [wiki en inclusion-exclution principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)
- [wiki ja inclusion-exclution principle](https://ja.wikipedia.org/wiki/%E5%8C%85%E9%99%A4%E5%8E%9F%E7%90%86)
