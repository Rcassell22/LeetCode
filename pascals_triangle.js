/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = function(numRows) {
    let result = []

    for (let i = 0; i < numRows; i++) {
        // First row is always [1]
        const row = [1];

        // Skip for the first row by intializing index at 1
        for (let j = 1; j < i; j++) {
            row.push(result[i - 1][j - 1] + result[i - 1][j]);
        }

        // Always add 1 at the end as long as it's not the first row
        if (i > 0) {
            row.push(1);
        }

        result.push(row);
    }

    return result;
};

console.log(generate(1).toString());
console.log(generate(2).toString());
console.log(generate(3).toString());
console.log(generate(5).toString());