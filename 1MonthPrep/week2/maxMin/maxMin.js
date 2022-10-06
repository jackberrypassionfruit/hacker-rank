/*
 * Complete the 'maxMin' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY arr
 */

const maxMin = (k, arr) => {
  arr = arr.sort((a, b) => a - b)
  console.log(arr)
  let minDiff
  let p = 0
  for (let i = 0; i < arr.length - k + 1; i++) {
    const diff = Math.abs(arr[i+k-1] - arr[i])
    if (diff < minDiff || minDiff === undefined) {
      minDiff = diff
      p = i
    }
    console.log(`diff: ${diff} |p: ${p} minDiff: ${minDiff} | `)
  }

  console.log(minDiff)
  return minDiff
}

// maxMin(3, [1,4,7,2])
// maxMin(3, [10, 100, 300, 200, 1000, 20, 30])
// maxMin(2, [1, 2, 1, 2, 1])
maxMin(2, [0,1,2,3,4,5])