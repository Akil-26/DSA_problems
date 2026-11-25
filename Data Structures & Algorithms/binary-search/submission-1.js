class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        var left = 0
        var right = nums.length - 1

        while (left <= right){
            let mid = left + (right-left) // 2
            if (target < nums[mid]){
                right = mid-1
            }
            else if(target > nums[mid]){
                left = mid + 1
            }else if (target == nums[mid]){
                return mid
            }
        }
        return -1
    }
}
