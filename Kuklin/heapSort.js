function heapSort(arr) {
  var middle = Math.floor(arr.length/2)-1;
  var length = arr.length;
    
  function swap(index1, index2) {
    var temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;    
  }

  function sift(parent, limit) {
    var left;
    var right;
    var max;

    while(true) {
      left = 2 * parent + 1;
      right = 2 * parent + 2;
      max = parent;

      if (left < limit && arr[left] > arr[max]) {
        max = left;
      }

      if (right < limit && arr[right] > arr[max])  {
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
    sift(i, length);
  }

  for (var i = arr.length-1; i >= 0; i--) {
    // На место первого элемента ставим последний
    swap(0, i);

    //Последний исключаем
    length -= 1;

    // Просеиваем первый через кучу
    sift(0, length);
  }

  return arr;
}

var arr = [998, 645, 48, 689, 213, 15, 8, 16, 16, 59, 11, 394, 1043];
console.log(heapSort(arr));