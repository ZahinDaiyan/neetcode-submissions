class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> m;
        for (const string& s: strs){
            int a[26] = {0};
            for (char ch : s){
                a[ch - 'a']++;
            }
            string key = "";
            for (int i = 0; i < 26; ++i){
                key += to_string(a[i]) + "#";
            }
            m[key].push_back(s);
        }
        
        vector<vector<string>> res;
        for (auto pair : m){
            res.push_back(pair.second);
        }
        return res;
    }
};
