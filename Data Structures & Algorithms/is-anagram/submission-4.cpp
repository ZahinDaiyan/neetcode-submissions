class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        int count[26] = {0};
        bool flag = true;
        
        for(char ch : s){
            count[ch - 'a']++;
        }
        for(char ch : t) {
            count[ch - 'a']--;
        }

        for (int n: count){
            if (n != 0){
                flag = false;
            }
        }
        return flag;

    }
};