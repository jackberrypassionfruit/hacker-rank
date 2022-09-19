function findMedian(arr) {
  // Write your code here
  for (let q in arr) {
    for (let i = 0; i < arr.length - 1; i++) {
      // console.log(typeof(i));
      if (arr[i] > arr[i + 1]) {
        let tmp = arr[i + 1];
        arr[i + 1] = arr[i];
        arr[i] = tmp;
        console.log(arr[i], arr[i + 1]);
      }
    }
  }
  return arr;
}

const arr = [5, 3, 1, 2, 4];

console.log(findMedian(arr));