// РАБОТАЮЩИЙ ПРИМЕР - https://jsfiddle.net/3Lcrwk0v/3/

// свап элементов массива arr с левого leftIndex на правый rightIndex
let swap = (arr, leftIndex, rightIndex) => {
	let tempElem = arr[leftIndex];
  arr[leftIndex] = arr[rightIndex];
  arr[rightIndex] = tempElem;
}

// рандомный массив
const arr = [123,71,6,9367,1,2,567,1,1234,8213,87,1238,196,9,2,685,281,50,1,98,1054];

// финальный отсортированный массив
let resultArr = [];
// пока массив имеет длинну, строим кучу
while(arr.length>1) {

	// берем массив из середины -1 элемент
  // округляем в бОльшую сторону, если кол-во элементов нечетное
	let curIndex = Math.floor(arr.length/2-1);
  while(curIndex>-1) {

    // если индекс 0 делаем поправку на +1
    let shift = 0;
    if (curIndex==0) {
    	shift = 1;
    }

    // сравниваем текущий элемент массива с i*2 и i*2+1
    // и свапаем в случае необходимости
    if (arr[curIndex*2+shift]>arr[curIndex*2+1+shift] && arr[curIndex]<arr[curIndex*2+shift]) {
    	swap(arr, curIndex, curIndex*2+shift);
    }
    else if (arr[curIndex*2+1+shift]>arr[curIndex*2+shift] && arr[curIndex]<arr[curIndex*2+1+shift]) {
     	swap(arr, curIndex, curIndex*2+1+shift);
    }

    // сдвигаем указатель на 1 влево
  	curIndex--;
  }

  // удаляем первый элемент из исходного массива
  // и добавляем его в начало нового, отсортированного
  resultArr.unshift(arr.shift());
}
