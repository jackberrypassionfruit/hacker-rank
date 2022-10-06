const sumXor = n => {
  let xorResult = 0;
  let Xs = [];
  let pass = true;

  // x is the potential 
  for (let x = 0; x < n; x++) {
    // n = 6;
    // let x = 2;

    let tmpN = n;
    let powOf2 = 50 // for use when using big numbers
    let tmpX = x;  // ** move to line 10
    
    console.log(`x: ${x}, n: ${n}`);
    for (let powOf2 = 3; powOf2 >= 0; powOf2--) {
      console.log(`pow2: ${powOf2}, tmpX: ${tmpX}, tmpN: ${tmpN}`);
      
      // console.log(`Xs is ${Xs} and xorResult is ${xorResult}, tmpX is ${tmpX} and tmpN is ${tmpN}`);
      // store whether tmp or x have a 1 in each place, by checking if it's bigger than each power of 2, starting from 8
      let digitFlipTmpN = Math.floor(tmpN / 2**powOf2);
      let digitFlipX = Math.floor(tmpX / 2**powOf2);
      if ((digitFlipTmpN) && (digitFlipX)) {
        // console.log(`digitFlipTmpN is ${digitFlipTmpN} and digitFlipX is ${digitFlipX}`)
        console.log("Breaking");
        pass = false;
        break;
      }
      if (digitFlipTmpN) {
        tmpN -= 2**powOf2;
      }
      if (digitFlipX) {
        tmpX -= 2**powOf2;
      }
    }

    if (pass) {
      Xs.push(x);
      xorResult++;
    }
    pass = true;
  
  }

  console.log(Xs);
  console.log(xorResult);
  return Xs, xorResult;
}

//console.log(
sumXor(10)//);

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

