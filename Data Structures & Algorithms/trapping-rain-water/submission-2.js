class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        var left = 0;
        var right = height.length - 1 ;

        var leftmax = height[left];
        var rightmax = height[right];

        var res = 0;

        while(left<right){
            if (leftmax<rightmax){
                left+=1
                leftmax = Math.max(leftmax,height[left]);
                res += leftmax - height[left];
            }else{
                right-=1
                rightmax = Math.max(rightmax,height[right]);
                res += rightmax - height[right];
            }
        }
        return res
    }
}
