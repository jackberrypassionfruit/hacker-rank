const balancedSums = (arr) => {
  const reduceSum = (current, next) => {
    return current + next;
  };
  
  for (let i = arr.length - 1; i >= 0; i--) {
    const left = arr.slice(0, i).reduce(reduceSum, 0);
    const right = arr.slice(i + 1).reduce(reduceSum, 0);
    console.log(`left: ${left} / right: ${right}`);

    if (left === right ) {
      return arr[i];
    }
  }

  return 'NO';
}

console.log(balancedSums([2, 0, 0, 0]));