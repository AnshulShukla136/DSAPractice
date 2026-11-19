class Solution {
    public int minimizeSum(int[] nums) {
        int n = nums.length;
        if(n == 3) return 0;
        Arrays.sort(nums);
        int a = Math.abs(nums[2] - nums[n-1]);
        int b = Math.abs(nums[n - 3] - nums[0]);
        int c = Math.abs(nums[n - 2] - nums[1]);
        return Math.min(a, Math.min(b,c));
    }
}