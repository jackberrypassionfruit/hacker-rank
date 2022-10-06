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

  const combinations = nCr(m + w, 3)  // all possible combos

  const allMenOutcomes = Math.floor(fact(m) / (6 * fact(m - 3)));
  const allWomenOutcomes = Math.floor(fact(w) / (6 * fact(w - 3)));
  
  console.log(combinations);
  console.log(allMenOutcomes);
  console.log(allWomenOutcomes);

  return combinations - allMenOutcomes - allWomenOutcomes;
}

console.log(`answer is ${diverseDeputation(1, 3)}`);
