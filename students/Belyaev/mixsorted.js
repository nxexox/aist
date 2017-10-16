// РАБОТАЮЩИЙ ПРИМЕР - https://jsfiddle.net/w5kdenps/

// перекидывает элементы массива с индексами min и max в начало массива arr
// перед этим удалив их из массива
let moveElemsToStart = (arr, min, max) => {
	let tempElems = [arr[min], arr[max]];

  if (min > max) {
  	arr.splice(min,1);
    arr.splice(max,1);
  } else {
  	arr.splice(max,1);
    arr.splice(min,1);
  }

  arr.unshift(tempElems[1]);
  arr.unshift(tempElems[0]);
};

// рандомный массив
const arr = [1,1,1,1,2,2,6,9,50,71,87,98,123,196,196,196,196,196,1234,1238,8213,9367];

// указатель в 0 позицию
let i=0;

// пока указатель не дошел до конца
while(i < arr.length) {

  // определяем дефолтно 2 значения min и max
  // и их порядковые номера в массиве arr
  let min = [arr[i], i];
  let max = [arr[i], i];

  // устанавливаем новый указатель j на следующую за i позицию
  let j = i+1;

  // итерируем по всему массиву правее j и находим min и max
  while (j < arr.length) {
  	if (min[0] > arr[j]) {
    	min = [arr[j], j]
    }

    if (max[0] < arr[j]) {
    	max = [arr[j], j];
    }

    j++;
  }

  // перемещаем нужные элементы в начало
  moveElemsToStart(arr, min[1], max[1]);

  // т.к. мы устанавливаем по 2 элемента, сдвигаем указатель на 2 вправо
  i = i+2;
}
