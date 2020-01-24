// Write a function that takes a string as input and reverse only the vowels of a string.

// Example 1:

// Input: "hello"
// Output: "holle"
// Example 2:

// Input: "leetcode"
// Output: "leotcede"

function reverseVowels(s){
  let arr = s.split('');
  let i = 0, j = arr.length - 1;
  let set = new Set("aeiouAEIOU");
  while(i < j){
    if(set.has(arr[i]) && set.has(arr[j])){
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
      j--;
    }else if(!set.has(arr[i]) && set.has(arr[j])){
      i++;
    }else if(set.has(arr[i]) && !set.has(arr[j])){
      j--
    }else{
      i++;
      j--;
    }
  }
}