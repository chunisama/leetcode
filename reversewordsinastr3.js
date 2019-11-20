var reverseWords = function(s) {
  let result = '';
  let words = s.split(' ');
  for (let i = 0; i < words.length; i++){
      if (i !== 0){
          words[i] += " ";
      } 
      for(j = words[i].length - 1; j >= 0; j--){
          if (words[i][j] === "`") {
              result += "'";
          }
          result += words[i][j];   
      }
  }
  return result;        
};