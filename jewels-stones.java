class Solution {
public:
    int numJewelIsStones(string J, string S){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        unordered_map<char, int> mymap;
        for(int i = 0; j[i] != '\0'; i++)
            ++mymap[j[i]];

        int count = 0;
        for(int i=0;S[i]!='\0';++1)
            if(mymap.find(S[i])!=mymap.end())
                count+=1;

        return count;
    }
};

    

    
