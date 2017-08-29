// РАБОЧИЙ ПРИМЕР https://jsfiddle.net/Lxyrgmtv/2/

// рандомный текст
const str = 'Шла саша по шоссе и сосала сушку';

// что ищем
const strSearch = 'и со';

// не учитываем последний символ в подстроке
let i = strSearch.length-2;
let strTable = {};

// если подстрока всего из 1 символа
if (i<0) {
	strTable[strSearch] = 1;

} else {

  // строим таблицу стоп-слов
  while(i > -1) {
    if (!strTable[strSearch[i]]) {
    	strTable[strSearch[i]] = strSearch.length - i - 1;
    }
    i--;
  }

}

// сбрасываем указатель на ноль и используем его далее для основной строки текста
i=0;

while (i < (str.length-strSearch.length)) {
	let j = strSearch.length-1;

  while (j > -1) {
  	if (strSearch[j] !== str[i+j]) {
      i = i + (strTable[str[i+j]] || strSearch.length);
   		break;
    }
    j--;
  }

  // если проверили всю строку и дошли до начала
  // значит нашли подстроку в строке
  if (j < 0) {
  	break;
  }
}
