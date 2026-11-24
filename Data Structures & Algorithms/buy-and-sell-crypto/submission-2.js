class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0
        let r = 1
        let maxp = 0
        while (r<prices.length){
            if (prices[r]<prices[l]){
                l = r;
            }
            else{
            maxp = Math.max(maxp,prices[r]-prices[l])
            }
        r++
        }
        return maxp
    }
}
