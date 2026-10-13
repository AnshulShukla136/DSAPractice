class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        for(int i = 0; i < n; i++){
            if(nums[i] < 0){
                nums[i] *= -1;
            }
        }
        Arrays.sort(nums);
        int n1 = n / 2;
        long total = 0;
        for(int i = 0; i < n1; i++){
            total -= nums[i] * nums[i]; 
        }
        for(int i = n1; i < n; i++){
            total += nums[i] * nums[i]; 
        }
        return total;
    }
}