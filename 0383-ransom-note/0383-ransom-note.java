class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int n = ransomNote.length();
        HashMap<Character, Integer> mp = new HashMap<>();
        for(int i = 0; i < n; i++){
            char c = ransomNote.charAt(i);
            mp.put(c, mp.getOrDefault(c,0) + 1);
        }
        for(int i = 0; i < magazine.length(); i++){
            char c = magazine.charAt(i);
            if(mp.containsKey(c)){
                mp.put(c, mp.getOrDefault(c,0) - 1);
                if(mp.get(c) == 0){
                    mp.remove(c);
                }
            }
        }
        if(mp.isEmpty()){
            return true;
        }
        return false;
    }
}