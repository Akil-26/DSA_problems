class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        const mymap = new Array(26).fill(0);
        const base = 'a'.charCodeAt(0);
        
        for(let i=0; i<s.length;i++){
            mymap[s.charCodeAt(i)-base]++;
            mymap[t.charCodeAt(i)-base]--;
        }
        for(const k of mymap){
            if(k!==0){
                return false
            }
        }
        return true
    }
}
