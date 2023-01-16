/**
 * Given a non-negative integer x, compute and return the square root of x.
 * Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
 * Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
 *
 * Constraints:
 *
 * 0 <= x <= 231 - 1
 */

/**
 * @param {number} x
 * @return {number}
 */
const mySqrt = function(x) {
    let i = 0;
    let sqrt = 0;
    let sqrtFound = false

    while (!sqrtFound) {
        if (i * i === x) { // If x is a perfect square, return the number
            sqrt = i;
            sqrtFound = true;
        } else if (i * i > x){ // If we've gone past the number, return the last number since we don't care about the remainder
            sqrt = i - 1;
            sqrtFound = true;
        }
        i++;
    }

    return sqrt;
};

console.log(mySqrt(4));
console.log(mySqrt(8));
console.log(mySqrt(0));