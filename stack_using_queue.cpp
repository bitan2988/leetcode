// https://leetcode.com/problems/implement-stack-using-queues/solution/

#include<iostream>
#include<queue>
using namespace std;

class MyStack {
public:
    queue<int> q_real;
    queue<int> q_hold;
    MyStack() {
        
    }
    
    void push(int x) {
        q_hold.push(x);
        
        while(!q_real.empty()){
            q_hold.push(q_real.front());
            q_real.pop();
        }
        
        while(!q_hold.empty()){
            q_real.push(q_hold.front());
            q_hold.pop();
        }
    }
    
    int pop() {
        int temp = q_real.front();
        q_real.pop();
        return temp;
        
    }
    
    int top() {
        return q_real.front();
    }
    
    bool empty() {
        return q_real.empty();
    }
};

/*
The mentioned above two approaches have one weakness, they use two queues. 
This could be optimized as we use only one queue, instead of two.

Push
When we push an element into a queue, 
it will be stored at back of the queue due to queue's properties. 
But we need to implement a stack, 
where last inserted element should be in the front of the queue, not at the back. 
To achieve this we can invert the order of queue elements when pushing a new element.


We will add the element and then will keep on poping element and again pushing them
will size if equal to the size before insertion of this element
 */

void push(int x, queue<int> q){
    int s = q.size();
    q.push(x);

    // by this we are just pushing the previous element 
    // after the currently added element
    while(s>1){
        int temp = q.front();
        q.pop();
        q.push(temp);
        s--;
    }
}