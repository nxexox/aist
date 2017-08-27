function heapSort(arr) {
  var middle = Math.floor(arr.length/2)-1;
  var resultArr = [];
    
  function swap(index1, index2) {
    var temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;    
  }

  function sift(parent) {
    var left;
    var right;
    var max;

    while(true) {
      left = 2 * parent + 1;
      right = 2 * parent + 2;
      max = parent;

      if (left < arr.length && arr[left] > arr[max]) {
        max = left;
      }

      if (right < arr.length && arr[right] > arr[max])  {
        max = right;
      }
      
      if (max == parent) {
        break;
      }

      // В случае если потомок больше родителя, меняем их местами
      swap(parent, max);
      parent = max;
    }
  }


  // Формируем кучу
  // Начинаем с середины массива, так как в этом случае у элемента гарантированно есть потомки
  for (var i=middle; i >= 0; i--) {
    sift(i);
  }

  for (var i = arr.length-1; i >= 0; i--) {
    // Берем первый элемент так как он максимальный
    var root = arr.shift();
    resultArr.unshift(root);

    // На место первого элемента ставим последний, и просеиваем его через кучу
    arr.unshift(arr.pop());
    sift(0);
  }

  return resultArr;
}

var arr = [998, 645, 48, 689, 213, 15, 8, 16, 59, 11, 394, 43];
console.log(heapSort(arr));