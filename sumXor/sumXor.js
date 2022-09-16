const sumXor = n => {
  xorResult = 0;
  Xs = [];
  pass = true;

  // x is the potential 
  for (let x = 0; x < n; x++) {
    let tmpN = n;
    let powOf2 = 50 // for use when using big numbers
    
    for (let powOf2 = 3; powOf2 >= 0; powOf2--) {
      let tmpX = x;
      
      // store whether tmp or x have a 1 in each place, by checking if it's bigger than each power of 2, starting from 8
      let digitFlipTmpN = Math.floor(tmpN / 2**powOf2);
      let digitFlipX = Math.floor(tmpX / 2**powOf2);
      if ((digitFlipTmpN) && (digitFlipX)) {
        pass = false;
        break;
      }
      console.log(`digitFlipTmpN is ${digitFlipTmpN} and digitFlipX is ${digitFlipX}`)
      if (digitFlipTmpN) {
        tmpN -= 2**powOf2;
      }
      if (digitFlipX) {
        tmpX -= 2**powOf2;
      }
      console.log(`Xs is ${Xs} and xorResult is ${xorResult}, tmpX is ${tmpX} and tmpN is ${tmpN}`);
    }

    if (pass) {
      Xs.push(x);
      xorResult++;
    }
    pass = false;
  }

  return xorResult;
}

console.log(sumXor(4));

// bitwise Xor examples:
// 0101 -> 5
// 1010 -> 10
// 1111 -> 15
// YES

// 1001 -> 9
// 0110 -> 6
// 1111 -> 15
// YES

// 0101 -> 5
// 1110 -> 14
// 1011 -> 11
// No

// 0100 -> 4
// 0010 -> 2
// 0110 -> 6
// YES

