const diverseDeputation = (m , w) => {
  // nCr function for calculating # of Combinations
  // nCr(n, r) = n! / r!*(n - r)!

  const fact = (n) => {
    let res = 1;
    while (n > 1) {
      res *= n--;
    }
    return res;
  }

  const nCr = (n , r) => {
    return fact(n) / (fact(r) * fact(n - r));
  }

  const combinations = nCr(m + w, 3)// all possible combos

  // let allWomenProb = 1, allMenProb = 1;
  // for (let i = 0; i < 2; i++) {
  //   allWomenProb *= (w - i) / (w - i + m);
  //   allMenProb *= (m - i) / (m - i + w); 
  // }

  // const monoGenderProb = allWomenProb + allMenProb;

  const allMenOutcomes = Math.floor(fact(m) / (6 * fact(m - 3)));
  const allWomenOutcomes = Math.floor(fact(w) / (6 * fact(w - 3)));
  
  console.log(combinations);
  console.log(allMenOutcomes);
  console.log(allWomenOutcomes);

  return combinations - allMenOutcomes - allWomenOutcomes;
}

console.log(`answer is ${diverseDeputation(1, 3)}`);

// [1,2,3] women , [4,5,6] men
// 50%
// [2,3] women , [4,5,6] men
// 40%
// [3] women , [4,5,6] men
// 25%

// 3 -> 1
// 4 -> 4
// 5 -> 60