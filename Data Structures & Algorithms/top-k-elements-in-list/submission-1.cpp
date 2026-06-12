class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        // Make the frequent count array 
        unordered_map<int , int> counts;
        for (int n : nums){
            counts[n]++;
        }

        vector<vector<int>> buckets(nums.size()+1);
        for(auto pair : counts){
            int n = pair.first;
            int f = pair.second;
            buckets[f].push_back(n);
        }
         vector<int> res;
        for (int i = buckets.size()-1; i >= 0; --i){
            for(int n: buckets[i]){
                res.push_back(n);
                if(res.size() == k){
                    return res;
                }
            }
        }
        return res;
    }
};
