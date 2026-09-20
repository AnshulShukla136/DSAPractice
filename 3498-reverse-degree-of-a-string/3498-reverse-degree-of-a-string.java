class Solution {
    public int reverseDegree(String s) {
        StringBuilder sb = new StringBuilder(s);
        int n = s.length();
        int sum = 0;
        for(int i = 0; i < n; i++){
            int num = 26 - (sb.charAt(i) - 'a');
            int prod = num * (i + 1);
            sum += prod;
        }
        return sum;
    }
}