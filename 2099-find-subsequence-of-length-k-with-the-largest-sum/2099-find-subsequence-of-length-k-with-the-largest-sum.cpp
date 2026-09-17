class Solution {
public:
    void solve(vector<int>&temp){
        int idx = 0;
        int mini = INT_MAX;
        for(int i = 0; i < temp.size(); i++){
            if(temp[i] < mini){
                mini = temp[i];
                idx = i;
            }
        }
        temp[idx] = INT_MAX;
    }
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<int>temp = nums;
        int n = nums.size();
        int diff = n - k;
        while(diff > 0){
            solve(temp);
            diff--;
        }
        vector<int>ans;
        for(int x : temp){
            if(x != INT_MAX){
                ans.push_back(x);
            }
        }
        return ans;
    }
};