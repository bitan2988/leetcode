// https://leetcode.com/problems/recover-binary-search-tree/

#include<iostream>
#include<vector>
using namespace std;


class node{
public:
    int data;
    node* left;
    node* right;

    node(int val){
        data = val;
        right = NULL;
        left = NULL;
    }
};

void node_swap(node* curr_node){

    if(curr_node == NULL)
        return;

    if (curr_node->left){
        if(curr_node->data < curr_node->left->data){
            int swap_data = curr_node->data;
            curr_node->data = curr_node->left->data;
            curr_node->left->data = swap_data;
        }
    }

    if (curr_node->right){
        if(curr_node->data > curr_node->right->data){
            int swap_data = curr_node->data;
            curr_node->data = curr_node->right->data;
            curr_node->right->data = swap_data;
        }
    }

    if(curr_node->left)
        node_swap(curr_node->left);
    if(curr_node->right)
        node_swap(curr_node->right);
}

int main(){
    vector<long> root;
    root = {1,2,3,NULL,4,5};

}