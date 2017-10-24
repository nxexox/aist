let string1 = 'opapq'.toLowerCase();
let string2 = 'oppaa'.toLowerCase();

let minString = '';
let maxString = '';

const N = string1.length;
const M = string2.length;

let matrix;

if (N > M) {
  matrix = initMatrix(createMatrix(M + 1), M + 1, N + 1);
  minString = string2;
  maxString = string1;
} else {
  matrix = initMatrix(createMatrix(N + 1), N + 1, M + 1);
  minString = string1;
  maxString = string2;
}

console.log('Расстояние между строками: ', knowSpacing(maxString, minString, matrix));

function knowSpacing(maxString, minString, matrix) {
  let i = 1;
  let j;

  for (; i <= minString.length; i++) {
    for (j = 1; j <= maxString.length; j++) {
      if (minString[i - 1] === maxString[j - 1]) {
        matrix[i][j] = matrix[i - 1][j - 1]; 
      } else if (minString[i - 1] === maxString[j] && minString[i] === maxString[j - 1]) {
        matrix[i][j] = matrix[i - 2][j - 2];
      } else {
        const del = matrix[i - 1][j];
        const paste = matrix[i][j - 1];
        const replace = matrix[i - 1][j - 1];
        const value = Math.min(del, paste, replace);

        matrix[i][j] = value + 1;
      }
    }
  }

  console.log(matrix);
  return matrix[minString.length][maxString.length];
}

function createMatrix(rows) {
  let matrix = [];
  let i = 0;
  let j = 0;

  for (; i < rows; i++) {
    matrix[i] = [];
  }

  return matrix;
}

function initMatrix(matrix, rows, cols) {
  let i = 0;
  let j = 0;

  for (; i < rows; i++) {
    matrix[i][0] = i;
  }

  for (; j < cols; j++) {
    matrix[0][j] = j;
  }

  return matrix;
}
