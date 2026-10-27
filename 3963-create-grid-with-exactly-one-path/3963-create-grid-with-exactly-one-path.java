class Solution {
    public String[] createGrid(int m, int n) {
        ArrayList<String> ans = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++){
            sb.append('.');
        }
        ans.add(sb.toString());
        sb.setLength(0);
        for(int i = 1; i < m; i++){
            for(int j = 0; j < n; j++){
                if(j == n - 1){
                    sb.append('.');
                }
                else{
                    sb.append('#');
                }
            }
            ans.add(sb.toString());
            sb.setLength(0);
        }
        String[] arr = new String[ans.size()];

        for (int i = 0; i < ans.size(); i++) {
            arr[i] = ans.get(i);
        }

        return arr;
    }
}