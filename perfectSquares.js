// Given a positive integer n, find the least number of perfect square numbers 
// (for example, 1, 4, 9, 16, ...) 
// which sum to n.

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.


function numSquares(n) {
  const table = new Array(n + 1).fill(Infinity);
  table[0] = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j * j <= i; j++) {
      table[i] = Math.min(
        table[i],
        table[i - j * j] + 1,
      );
    }
  }
  return table[n];
}


console.log(perfectSquares(12));