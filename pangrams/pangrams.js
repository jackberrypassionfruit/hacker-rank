const pangrams = s => {
  const letter = 'a'
  // console.log(letter.charCodeAt(0)); // 97
  // 'a' -> 97
  // 'A' -> 65

  const number = 97;
  // console.log(String.fromCharCode(number)); // a
  // 97 -> 'a'
  // 65 -> 'A'

  if (s.length < 26){
    return 'not pangram';
  }

  const alphabet = {};

  for (let i = 0; i < 26; i++) {
    const newLetter = String.fromCharCode(97 + Number(i));
    alphabet[newLetter] = false;
  }

  for (let char of s) {
    if (char !== ' ') {
      alphabet[char.toLowerCase()] = true;
    }
  }

  // console.log(alphabet);

  for (let check of Object.values(alphabet)) {
    if (!check) {
      return 'not pangram';
    }
  }

  return 'pangram';

  // console.log(Object.values(alphabet)); // big long obj
} 

console.log(pangrams('We promptly judged antique ivory buckles for the next prize'));
// console.log(pangrams('We fucked'));