class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = -1;
        if(k == 1){
           vector<int>temp = nums;
           sort(temp.begin(), temp.end());
           if(temp[n-1] != temp[n-2]){
            return temp[n-1];
           }
           if(temp[0] != temp[1]){
            ans = temp[0];
           }
           for(int i = n-2; i > 0; i--){
                if(temp[i] != temp[i-1] && temp[i] != temp[i+1]){
                    return temp[i];
                }
           }
        }else if(k == n){
            ans = *max_element(nums.begin(), nums.end());
        }
        else{
            bool isFirst = true;
            for(int i = 1; i < n; i++){
                if(nums[i] == nums[0]){
                    isFirst = false;
                    break;
                }
            }
            int i = n-2;
            bool isLast = true;
            while(i >= 0){
                if(nums[i] == nums[n - 1]){
                    isLast = false;
                    break;
                }
                i--;
            }
            if(!isFirst && !isLast){
                return -1;
            }
            else if(!isFirst && isLast){
                return nums[n - 1];
            }
            else if(isFirst && !isLast){
                return nums[0];
            }
            else{
                return max(nums[0], nums[n - 1]);
            }
        }
        return ans;
    }
};