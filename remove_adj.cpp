// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


// We can store the chars in a stack and at every point pop elelemnts is the current element is 
// equal to the top element
// Since we remove in grp of k, if there are n same chars adjacent then n%k wont be able to form grps

#include<iostream>
#include<string.h>
#include<stack>
#include<vector>
using namespace std;

class Solution {
public:
    string removeDuplicates(string s, int k) {
        stack<char> st;
        
        for(int i=0; i < s.length(); i++){
            if(st.empty()){
                st.push(s[i]);
            }
            else if(st.top() != s[i])
                st.push(s[i]);
            else{
                int count = 0;
                while(!st.empty() or st.top() != s[i]){
                    count++;
                    st.pop();
                }
                for(int i=0; i<((count+1)%k); i++)
                    st.push(s[i]);
            }
        }
        
        string res = "";
        stack<char> rev_st;
        while(!st.empty()){
            rev_st.push(st.top());
            st.pop();
        }
        
        while(!rev_st.empty()){
            res += rev_st.top();
            rev_st.pop();
        }
        return res;
    }
};


// another approach can be to keep track of count of all elements
// we can maintain aother stack having that count









// DISCUSSION SOLUTION
class Solution {
public:
    string removeDuplicates(string s, int k) {
        
        int n = s.length();
        vector<int> continousFreqCount(n, 1);
        stack<int> st;
        string ans;
        
        st.push(0);
        
        for(int i = 1; i < n ; i++){            
            if(!st.empty()){
                if(s[st.top()]==s[i]) 
                    continousFreqCount[i] = continousFreqCount[st.top()] + 1;
            }
            
            st.push(i);
            
            if(continousFreqCount[st.top()] == k){
                for(int i = 0 ; i < k ; i++){
                    st.pop();
                }
            }   
        }
        
        while(!st.empty()){          
            ans += s[st.top()];
            st.pop();    
        }
        
        reverse(ans.begin(), ans.end());
        
        return ans;
        
    }
};