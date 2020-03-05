function findMedianSortedArrays(nums1, nums2) {
  let combinedArr = [...nums1, ...nums2].sort(function(a, b){return a-b});
  let middleIdx = Math.floor(combinedArr.length / 2);
  // if the total length of combinedArr is odd
  if (combinedArr.length % 2 !== 0){
      return combinedArr[middleIdx];
  } else {
      return (combinedArr[middleIdx - 1] + combinedArr[middleIdx]) / 2;
  }
};