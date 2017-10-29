function levenshtein(str1, str2) {
  var maxStr, minStr;
  if (str1.length > str2.length) {
    maxStr = str1;
    minStr = str2;
  } else {
    maxStr = str2;
    minStr = str1;
  }

  var matrix = createMatrix(minStr.length, maxStr.length);
  return getDistance(matrix, minStr, maxStr);

  function getDistance(matrix, rows, cols) {
    var cur_i, cur_j;
    for (i=1; i <= rows.length; i++) {
      cur_i = i-1;
      for (j=1; j <= cols.length; j++) {
        cur_j = j-1;
        if (rows[cur_i] === cols[cur_j]) {
          matrix[i][j] = matrix[i-1][j-1];
        } else {
          var metrics = [
            matrix[i-1][j], // Удаление
            matrix[i][j-1], // Вставка
            matrix[i-1][j-1] // Замена
          ];

          if (rows[cur_i-1] === cols[cur_j] && rows[cur_i] === cols[cur_j-1]) {
            metrics[3] = matrix[i-2][j-2]; // транспозиция
          }

          var min = Math.min.apply(null, metrics);
          matrix[i][j] = min + 1;
        }
      }
    }
    console.log(matrix);
    return matrix[rows.length][cols.length];
  }

  function createMatrix(rowsLength, colsLength) {
    var matrix = [];
    for (var i = 0; i < rowsLength+1; i++) {
      matrix[i] = [i];
    }

    for (var i = 0; i < colsLength+1; i++) {
      matrix[0][i] = i;
    }
    return matrix;
  }
}
console.log(levenshtein('oppaa', 'opapq'));