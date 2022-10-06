const mergeSort = (arr) => {
  // Divide
  // Conquer
  // Combine

  if (arr.length > 1) {
    const mid = Math.floor(arr.length / 2)
    const L = arr.slice(0, mid)
    const R = arr.slice(mid)
    
    mergeSort(L)
    mergeSort(R)
    
    console.log(R);
    
    let i = 0, j = 0, k = 0

    console.log(arr)
    
    while (i < L.length && j < R.length) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++
      } else if (L[i] > R[j]) {
        arr[k] = R[j];
        j++;
      }
      console.log(k)
      k++
    }

    console.log(arr)
    
    while (i < L.length) {
      arr[k] = L[i];
      i++;
      k++
    }
    
    while (j < R.length) {
      arr[k] = R[j];
      j++;
      k++;
    }
    // console.log(L)
    // console.log(R)

  }


}

const arr = [4,3,5,1,7, 2, 6, -2342]
mergeSort(arr)
console.log(arr)