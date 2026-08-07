class Solution {
public:
    int countValidPrefixes(string s) {
        int count = 0;
        int ones = 0;
        int zeroes = 0;
        for(char c: s){
            if(c == '0'){
                zeroes++;
            }else{
                ones++;
            }
            if(abs(ones - zeroes) == 0 || abs(ones - zeroes) == 1)count++;
        }
        return count;
    }
};