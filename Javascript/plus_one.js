/**
 * You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
 * The digits are ordered from most significant to least significant in left-to-right order.
 * The large integer does not contain any leading 0's.
 * Increment the large integer by one and return the resulting array of digits.
 *
 * Constraints:
 * 1 <= digits.length <= 100
 * 0 <= digits[i] <= 9
 * digits does not contain any leading 0's.
 *
 */


/**
 * @param {number[]} digits
 * @return {number[]}
 */
const plusOne = function(digits) {
    // convert array to a string equal to expected number:
    const arrayString = digits.join('');
    // increment by one. Use BigInt incase of large number:
    const arrayBigNumber = BigInt(arrayString) + BigInt(1);
    // return to a number array:
    digits = Array.from(String(arrayBigNumber), Number);
    return digits;
};

console.log(plusOne([1,2,3]).toString());
console.log(plusOne([4,3,2,1]).toString());
console.log(plusOne([9]).toString());
console.log(plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]).toString());