// Given two strings s and t , write a function to determine if t is an anagram of s.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

function isAnagram(s, t){
	const map = {};
	s.split('').map(c => map[c] === undefined ? map[c] = 1 : map[c] += 1);
	t.split('').map(c => map[c] === undefined ? map[c] = -1 : map[c] -= 1);
    console.log(map);
	return Object.keys(map).every(k => map[k] === 0);
}