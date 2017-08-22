const fastSort = (arr) => {
  const midIndex = Math.round(arr.length / 2);
  const center = [];
  let left = [];
  let right = [];

  arr.forEach((item) => {
    if (item < arr[midIndex]) {
      left.push(item);
    }
    if (item === arr[midIndex]) {
      center.push(item);
    }
    if (item > arr[midIndex]) {
      right.push(item);
    }
  });
  if (left.length > 1) {
    left = fastSort(left);
  }
  if (right.length > 1) {
    right = fastSort(right);
  }
  return left.concat(center, right);
};
