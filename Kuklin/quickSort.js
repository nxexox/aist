function quickSort(arr) {
  if (arr.length <= 1) return arr; 
  
  var middleIndex = Math.round(arr.length/2);
  var middle = arr[middleIndex];
  var left = [];
  var right = [];
  var center = [];
      
  arr.forEach(function(item) {
    if (item < middle) {
      left.push(item);
    } else if (item > middle) {
      right.push(item);
    } else {
      center.push(middle);
    }
  });
  
  return quickSort(left).concat(center, quickSort(right));
}

var arr = [998, 645, 48, 689, 213, 15, 15, 8, 16, 59, 11, 394, 43];
console.log(quickSort(arr));