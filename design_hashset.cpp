//https://leetcode.com/problems/design-hashset/submissions/


#include<iostream>
#include<vector>
#include<string>
using namespace std;

class MyHashSet_optimised {
public:
    int size = 1000000; // 10e6
    int Node[1000000];
    int hash(int key) {
        return key%size;
    }
    MyHashSet_optimised() {
        
    }
    
    void add(int key) {
        Node[hash(key)] = 1;
        
    }
    
    void remove(int key) {
        Node[hash(key)] = 0;
    }
    
    bool contains(int key) {
        return Node[hash(key)] == 1;
    }
};


class MyHashSet {
public:
        vector<bool> ans;
    MyHashSet() {
        ans.resize(1e6+1,false);
    }
    
    void add(int key) {
        ans[key]=true;
    }
    
    void remove(int key) {
        ans[key]=false;
    }
    
    bool contains(int key) {
        return ans[key];
    }
};

int main(){
    std::vector<std::string> operations {"MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"};
    //[[], [1], [2], [1], [3], [2], [2], [2], [2]]

}