class Solution {
    public boolean isValid(String s) {
        StringBuilder sb = new StringBuilder(s);
        Stack <Character> st = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(sb.charAt(i) == '(' || sb.charAt(i) == '[' || sb.charAt(i) == '{'){
                st.push(sb.charAt(i));
            }
            else{
                if(!st.isEmpty() &&  (sb.charAt(i) == ')' && st.peek() == '(' || sb.charAt(i) == ']' && st.peek() == '[' || sb.charAt(i) == '}' && st.peek() == '{') ){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        if(st.isEmpty()){
            return true;
        }
        return false;
    }
}