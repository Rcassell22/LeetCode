/**
 *
 * Given two binary strings a and b, return their sum as a binary string.
 *
 *
 * Constraints:
 *
 * 1 <= a.length, b.length <= 104
 * a and b consist only of '0' or '1' characters.
 * Each string does not contain leading zeros except for the zero itself.
 *
 */

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
const addBinary = function(a, b) {
    // Constants:
    const binRadix = 2;

    // Convert binary strings to BigInts:
    const numA = BigInt('0b' + a);
    const numB = BigInt('0b' + b);

    // Get the sum:
    const numSum = numA + numB;

    return numSum.toString(binRadix);
};

console.log(addBinary("11", "1"));
console.log(addBinary("1010", "1011"));
console.log(addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
"110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"));

