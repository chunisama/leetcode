// Let's call an array A a mountain if the following properties hold:

// A.length >= 3
// There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
// Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

// Example 1:

// Input: [0,1,0]
// Output: 1
// Example 2:

// Input: [0,2,1,0]
// Output: 1

function peakIndexInMountainArray(A, lower = 0, higher = A.length - 1) {
  if (lower === higher) return lower;
  let middle = Math.floor((lower + higher) / 2);
  if (A[middle] > A[middle + 1] && A[middle] > A[middle -1]){
      return middle;
  } else if (A[middle] < A[middle + 1]){
      return peakIndexInMountainArray(A, middle + 1, higher);
  } else {
      return peakIndexInMountainArray(A, lower, middle);
  }
};