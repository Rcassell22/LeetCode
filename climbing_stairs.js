/*
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?

    (basically return the nth number of the Fibonacci sequence)

    Constraints:
        1 <= n <= 45
*/

/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = function(n) {
    const startingArray =[1 , 1];
    if (n > 1) { // If n is one just skip the loop
        for (let i = 2; i <= n ; i++) {
            // Add a new element equal to sum of last 2 elements:
            startingArray[i] = startingArray[i - 1] + startingArray[i - 2];
        }
    };
    return startingArray[startingArray.length - 1];
};

console.log(climbStairs(2));
console.log(climbStairs(3));