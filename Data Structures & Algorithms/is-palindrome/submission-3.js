class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const cleantext = s.replace(/[^a-zA-Z0-9]/g,"").toLowerCase();
        return cleantext === cleantext.split("").reverse().join("")
    }
}
