/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
const matrixReshape = function(mat, r, c) {
    // If the new matrix dimensions won't work with the old one, return the new one
    if((mat.length * mat[0].length) !== (r * c)) {
        return mat;
    }

    let elementContainer = [];

    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[i].length; j++) {
            elementContainer.push(mat[i][j])
        }
    }

    let containerCounter = 0;
    let newMatrix = []
    for (let k = 0; k < r; k++) {
        let newRow = [];
        for (let l = 0; l < c; l++) {
            newRow.push(elementContainer[containerCounter]);
            containerCounter++;
        }
        newMatrix.push(newRow);
    }

    return newMatrix;
};

console.log(matrixReshape([[1,2],[3,4]], 1, 4).toString());
console.log(matrixReshape([[1,2],[3,4]], 2, 4).toString());
console.log(matrixReshape([[1,2,3,4]], 2, 2).toString());