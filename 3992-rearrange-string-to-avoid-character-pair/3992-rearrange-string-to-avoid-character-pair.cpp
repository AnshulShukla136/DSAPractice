class Solution {
public:
    string rearrangeString(string s, char x, char y) {
        int n = s.size();
        string str = "";
        for(int i = 0; i < n; i++){
            if(s[i] != x){
                str.push_back(s[i]);
                s[i] = '.';
            }
        }
        for(int i = 0; i < n; i++){
            if(s[i] != '.'){
                str.push_back(s[i]);
            }
        }
        return str;
    }
};