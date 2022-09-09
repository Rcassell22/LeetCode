/**
 * @param {string} s guarenteed to container a word
 * @return {number} the length of the last word in the original string
 */
const lengthOfLastWord = function(s) {
    let lastElementLength = 0;

    // Split string into array of substrings:
    const splitString = s.split(/(\s+)/);

    /**
     * Loop through the array from the end to check element length.
     * If it's whitespace or an empty string, remove it and start again.
     * Otherwise, set lastElementLength and exit the loop.
     */
    while(lastElementLength === 0) {
        if (splitString[splitString.length -1 ].includes(' ') || !splitString[splitString.length -1 ]) {
            splitString.splice(splitString.length - 1, 1);
        } else {
            lastElementLength = splitString[splitString.length - 1].length;
        }
    }

    return lastElementLength;
};


lengthOfLastWord("Hello World");
lengthOfLastWord("   fly me   to   the moon  ");
lengthOfLastWord("luffy is still joyboy");