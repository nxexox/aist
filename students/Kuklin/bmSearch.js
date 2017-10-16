function getShiftTable(search) {
  var table = {};
  var length = search.length;
  
  for (var i = 0; i <= length - 2; i++) {
    table[search[i]] = length - i - 1;
  }

  return table;
}

function bmSearch(search, str) {
  var resultIndex;
  // Получаем таблицу смещения
  var shiftTable = getShiftTable(search);
  var searchLength = search.length;
  var strLength = str.length;
  var strIndex = searchLength - 1;

  while (strIndex < strLength) {
    var searchIndex = 0;

    while (searchIndex < searchLength) {
      if (search[searchLength - 1 - searchIndex] === str[strIndex - searchIndex]) {
        searchIndex++;
      } else {
        break;
      }
    }
    
    if (searchIndex == searchLength) {
      //При совпадении символов возвращаем результат
      resultIndex = strIndex - (searchLength-1);
      break;
    } else if (searchIndex == 0) {
      //При несовпадении берем сщещение из таблицы
      var shift = shiftTable[str[strIndex - searchIndex]] || searchLength;
      strIndex += shift;
    } else {
      //При ряде совпадений и последующим несовпадении берем сщещение из таблицы, но на этот раз по последнему символу искомой строки
      var shift = shiftTable[search[searchLength-1]] || searchLength;
      strIndex += shift;
    }
  }

  return resultIndex;
}

var str = 'Lorem ipsum dtlor sit dolor, consectetur adipiscing elpt';
var search = 'dolo';

console.log(bmSearch(search, str));