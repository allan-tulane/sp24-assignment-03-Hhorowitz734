# CMPS 2200 Assignment 3
## Answers

**Name:** Benjamin Horowitz

Place all written answers from `assignment-03.md` here for easier grading.

**1a** - We can use the following steps to solve this problem:

1) Choose the coin with the greatest denomination < N (If the denomination == N we are done)
2) Subtract the value of the coin from N and repeat the first step until N is 0

**1b** - We need to do 2 proofs here

1) To prove the greedy-choice property:
- When we choose a coin, we choose the largest coin which has a denomination 2^k <= N.
- Suppose we instead chose 2 coins of the lower denomination (2 * 2^(k-1)). This would leave us with more coins, which would contradict the greedy choice property.
- Therefore, this property is satisfied.

2) To prove the optimal substructure property:
- Every time we choose a coin of denomination 2^k, we have to solve the same problem again N - 2^k
- We know that making change for a larger amount would require more coins than making change for a smaller amount, as this is intuitive.
- If we chose a non-optimal value p instead of k,
we would have N - 2^p change to make. Since p < k, N - 2^p > N - 2^k, hence choosing k will always be optimal.

**1c** - Work/Span

1) The work of this approach is log_2(N), since this is literally the amount of times it would take to subtract 2^n before you reach 0.
2) The span of this approach is also log_2(N), since you could not parallelize this. 

**2a** - Counterexample:

1) Let's say there are 3 denominations: 1, 3, and 4
2) If you had 6 dollars, our algorithm would suggest selecting 4, then 1, then 1 (3 coins)
3) However, the optimal solution is 3 and then 3 (2 coins)

**2b** - To show the optimal substructure problem, we can use an inductive proof:

1) Base Case -> Let's say that N is the smallest denomination that is available. The optimal solution is to use 1 coin of that denomination.
2) Inductive Case -> Assume we can find an optimal solution for all amounts < N. We can reduce our problem to the base case by repeatedly choosing N - the smallest denomination coin. Therefore, the optimal substructure is maintained.

**2c** - Design an algorithm

1) For our algorithm, we can use an approach similar to our fibonnaci lab. We can create a list coins[] where we will store the minimum number of coins for each amount i. Then, we use the recursive property I outlined in 2b, setting each index i of coins to coins[i - denomination] for every denomination < i. Then, the last index will be the answer.
2) The work of this bottom up approach is O(n), as is the span. This is because we need to compute every problem exactly once with no duplicates.
