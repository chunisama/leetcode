// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note:

// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1:
// Input: [2,2,1]
// Output: 1

// Example 2:
// Input: [4,1,2,1,2]
// Output: 4

function singleNumber(nums){
  let counter = {};
  nums.forEach((num) => {
    if (!counter[num]) {
      counter[num] = 1;
    } else {
      counter[num] += 1;
    }
  })
  for (const num in counter) {
    if (counter[num] === 1) {
      return num;
    }
  }
}

