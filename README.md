# Impact Analytics - Python Assignment - Case Study

## Problem Statement

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day. 

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal
The solution should output the probability as a fraction in the format `"miss_graduation_sequences / total_sequences"`, without actually performing the division or reducing the fraction to a decimal.

## Solution Approach
The solution is implemented using a recursive approach with memoization to efficiently calculate the number of valid attendance sequences and the number of sequences that result in missing the graduation ceremony.

### Recursive Function with Memoization
- The function `count_sequences(n, absent)` counts the number of valid sequences of length `n` with `absent` consecutive absences at the end.
- Memoization is used to store the results of sub problems to avoid redundant calculations and improve efficiency.

### Base Case
- For \( n = 0 \): only one valid sequence of length 0 (the empty sequence), no absences allowed.

### Recursive Relations
- If `absent` is 0, the function considers all valid sequences of length `n-1` with any number of absences up to 3 and adds an attended day.
- If `absent` is 1, 2, or 3, the function considers valid sequences of length `n-1` with one fewer absence and adds a missed day.

### Time Complexity
- The time complexity of the solution is \( O(N) \), as each state (combination of `n` and `absent`) is computed at most once due to memoization.

### Space Complexity
- The space complexity is \( O(N) \), due to the storage required for memoization and the call stack.
