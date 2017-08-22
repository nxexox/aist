const heap_sort = (initialArr) => {
  const result = [];
  const createHeap = (arr) => {
    const midIndex = Math.floor(arr.length / 2) - 1;

    for(let i = midIndex; i > -1; i--) {
      const leftIndex = (i * 2) + 1;
      const rightIndex = (i * 2) + 2;
      const maxElemIndex = arr[leftIndex] >= arr[rightIndex] ? leftIndex : rightIndex;

      if (arr[i] < arr[maxElemIndex]) {
        const buff = arr[i];
        arr[i] = arr[maxElemIndex]
        arr[maxElemIndex] = buff;
      }
    }
    result.unshift(arr.shift());
    if (arr.length !== 0) {
      createHeap(arr);
    }
  };
  createHeap(initialArr);
  return result;
};

const testArr = [2, 28, 172, 239, 21, 21, 932, 31, 90, 2, 1, 123, 32, 213];
console.log(heap_sort(testArr));
