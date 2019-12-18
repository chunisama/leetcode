// Given a positive integer n, find the least number of perfect square numbers 
// (for example, 1, 4, 9, 16, ...) 
// which sum to n.

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.

function squareNums(n){
  let squares = [];
  for (let i = 1; i * i < n; i++) {
    squares.push(i * i);
  }
  return squares;
}
function perfectSquares(n){
  let squares = squareNums(n);
  let value = n;
  let minResult = Infinity;
  for (let i = 0; i < squares.length; i++) {
    for (let quantity = 1; quantity * squares[i] <= value; quantity++) {
      if (minResult > quantity && quantity * squares[i] === value) {
        minResult = quantity;
      }
    }
  }
  return minResult;
}


console.log(perfectSquares(12));