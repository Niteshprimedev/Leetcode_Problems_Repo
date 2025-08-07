
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}
var MinStack = function() {
    // const newNode = new Node(null);
    this.stackTop = null;
    this.length = 0;
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    const newNode = new Node(val);
    if(this.stackTop === null){
        this.stackTop = newNode;
    }
    else{
        newNode.next = this.stackTop;
        this.stackTop = newNode;
    }
    this.length++;
    return null;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if(this.stackTop){
        let currNode = this.stackTop;
        this.stackTop = currNode.next;
        currNode.next = null;
        this.length--;
    }
    return null;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if(this.stackTop === null) return null;
    return this.stackTop.val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    if(this.stackTop){
        let currNode = this.stackTop;
        let minVal = currNode.val;
        
        while(currNode){
            currNode = currNode.next;
            if(currNode){
                let newMinVal = currNode.val;
                if(newMinVal < minVal){
                    minVal = newMinVal;
                }
            }
        }
        return minVal;
    }
    return null;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */