class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        int maxx = 0;
        int counts[26] = {0};
        for (int r = 0; r < s.length(); ++r){
            counts[s[r] - 'A']++;
            int curr = 0;
            for(int i = 0 ; i < 26; ++i){
                curr = max(curr,counts[i]);
            } 
            while(r-l+1 - curr > k){
                counts[s[l] - 'A']--;
                l++;
                curr = 0;
                for(int i = 0; i<26; ++i){
                    curr = max(curr,counts[i]);
                }
            }
            
            maxx = max(maxx , r-l+1);
        }

        return maxx;
    }
};
