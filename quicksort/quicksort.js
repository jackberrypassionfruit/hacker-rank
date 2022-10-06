const sort = (arr, low, hi) => {
  if (hi > low) {
    const pivot = arr[hi - 1]
    console.log(pivot)
    let big;
    console.log(arr)
    for (let i in arr.slice(low, hi)) {
      i = Number(i)
      console.log('i:', i)
      console.log('b: ', big)
      
      if (big === undefined && arr[i] > pivot) {
        big = i;
      }
      // swap arr[i] with arr[big] if we find a smaller num
      if (big !== undefined && arr[i] < pivot) {
        [arr[i], arr[big]] = [arr[big], arr[i]]
        console.log(arr[i], arr[big])
        // arr[i] += arr[big]
        // arr[big] = arr[i] - arr[big]
        // arr[i] -= arr[big]
        big += 1
      }
    }
    [arr[arr.length - 1], arr[big]] = [arr[big], arr[arr.length - 1]]
    console.log(arr)
    console.log(big)

    sort(arr, low, big)
    sort(arr, big, hi)
  }

}

const quickSort = (arr) => {
  sort(arr, 0, arr.length)
}

const arr = [8, 7, 6, 1, 0 ,9 ,2]
quickSort(arr)
console.log(arr)