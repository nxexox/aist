const shuffle = (arr) => {
  const maxWhile = 10
  const swap = (index1, index2) => {
    const buff = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = buff;
  }

  const isSorted = (index, leftIndex, rightIndex) => {
    console.log('sorted')
    return arr[index] < arr[rightIndex] || arr[index] > arr[leftIndex];
  };

  for (let i = 0; i < arr.length; i++) {
    let newIndex = Math.floor(Math.random() * arr.length);
    let whileIteration = 0;
//     console.log(i, newIndex)
    while(isSorted(i, newIndex - 1, newIndex + 1) && whileIteration <= maxWhile) {
      whileIteration++;
//       console.log(i, '/', whileIteration);
      newIndex = Math.floor(Math.random() * arr.length);
    }
    if (whileIteration === maxWhile) {
//       console.log('suka')
    }
    swap(i, newIndex);
  }
  return arr;
};

const testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(shuffle(testArray));
