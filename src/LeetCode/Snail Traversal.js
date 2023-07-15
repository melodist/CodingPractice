/**
* https://leetcode.com/problems/snail-traversal
* Implementation Problem
*/
//1. My Solution (226ms)
/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) return [];
    
    let arr = Array.from(Array(rowsCount), () => new Array(colsCount))
    let r = 0
    let c = 0
    let dir = 1

    this.forEach((x, i) => {
        arr[r][c] = x
        if ((dir == 1 && r == rowsCount - 1) ||
        (dir == -1 && r == 0)) {
            if (c % 2 == 0) {
                r = rowsCount - 1
            } else {
                r = 0
            }
            dir *= -1
            c += 1
        } else {
            r += dir
        }  
    })

    return arr
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

//2. Other Solution
Array.prototype.snail = function(numRows, numCols) {
  if (numRows * numCols !== this.length) return [];
  let result = Array(numRows).fill().map(() => []);
  for (let row = 0; row < numCols; row++) {
    for (let col = 0; col < numRows; col++) {
      result[(row & 1) ? numRows - col - 1 : col].push(this[row * numRows + col]);
    }
  }
  return result;
}
