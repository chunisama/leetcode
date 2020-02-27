// Given a non-empty array of integers, return the k most frequent elements.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]

// todo: Need to finish this one

function topKFrequent(nums, k){
  if (nums.length === 1) return nums[0];
  let counter = {};
  for (let i = 0; i < nums.length; i++) {
    var num = nums[i];
    if (counter[num] === undefined) {
      counter[num] = 1;
    }
    counter[num]++;
  }
  return counter.keys.map((num) => {num >= k});
}