class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        PriorityQueue<Integer>pq = new PriorityQueue<>();
        for(int i = 0; i < n; i++){
            if(nums[i] < 0){
                nums[i] *= -1;
            }
            pq.add(nums[i]);
        }
        int n1 = n / 2;
        int n2 = n - n1;
        long total = 0;
        while(n1 > 0){
            total -= pq.peek() * pq.peek();
            pq.poll();
            n1--;
        }
        while(n2 > 0){
            total += pq.peek() * pq.peek();
            pq.poll();
            n2--;
        }       
        return total;
    }
}