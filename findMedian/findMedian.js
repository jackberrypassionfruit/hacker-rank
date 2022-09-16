function findMedian(arr) {
  // Write your code here
  for (let q in [1,2,3,4,5]) {
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[Number(i) + 1]) {
        let tmp = arr[Number(i) + 1];
        arr[Number(i) + 1] = arr[i];
        arr[i] = tmp;
        console.log(arr[i], arr[Number(i) + 1]);
      }
    }
    console.log(q);
  }
  return arr;
}

const arr = [5, 3, 1, 2, 4];

console.log(findMedian(arr));