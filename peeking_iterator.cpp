// https://leetcode.com/problems/peeking-iterator/
#include<iostream>
#include<vector>
using namespace std;

class Iterator {
 		struct Data;
 		Data* data;
  public:
 		Iterator(const vector<int>& nums);
 		Iterator(const Iterator& iter);
 
 		// Returns the next element in the iteration.
 		int next();
 
 		// Returns true if the iteration has more elements.
 		bool hasNext() const;
};	

class PeekingIterator : public Iterator {
    int nextVal;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        nextVal = Iterator::next();
    }
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return nextVal;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface. Override them if needed.
	int next() {
        int temp = nextVal;
        if (Iterator::hasNext())
            nextVal = Iterator::next();
        else
            nextVal = NULL;
	    return temp;
	}
	
	bool hasNext() const {
	    return (nextVal != NULL);
	}
};

/*
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = self.iterator.next() if self.iterator.hasNext() else None        

    def peek(self):
        return self.current
        
    def next(self):
        value = self.current
        self.current = self.iterator.next() if self.iterator.hasNext() else None       
        return value
            
    def hasNext(self):
        return self.current is not None
*/