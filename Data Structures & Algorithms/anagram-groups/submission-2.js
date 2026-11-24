class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const mymap = new Map();
        for(const word of strs){
            var counter = new Array(26).fill(0);
            for(let ch of word){
                counter[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++
            }
            const key = counter.join(",")
            if (!mymap.has(key)){
                mymap.set(key,[]);
            }
            mymap.get(key).push(word)
        }
        return Array.from(mymap.values())
    }
}
