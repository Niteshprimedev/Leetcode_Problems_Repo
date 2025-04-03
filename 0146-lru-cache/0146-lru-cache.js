/**
 * @param {number} capacity
 */

class DLLNode{
    constructor(key, value){
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoublyList{
    constructor(){
        this.head = new DLLNode(-1, -1);
        this.tail = new DLLNode(-1, -1);
        
        // Connecting the head & the tail node;
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    // Add node to the doubly list;
    addNode(newNode){
        const nextNode = this.head.next;

        this.head.next = newNode;
        newNode.prev = this.head;

        newNode.next = nextNode;
        nextNode.prev = newNode;
        return true;
    }

    // Delete node from the doubly list;
    deleteNode(oldNode){
        const oldNodeNextNode = oldNode.next;
        const oldNodePrevNode = oldNode.prev;

        oldNodePrevNode.next = oldNodeNextNode;
        oldNodeNextNode.prev = oldNodePrevNode;
        return true;
    }
}
var LRUCache = function(capacity) {
    this.lruCacheSize = capacity;
    this.doublyList = new DoublyList();
    this.lruCacheHashmap = new Map();
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    const isKeyPresent = this.lruCacheHashmap.has(key) === true;
    if(isKeyPresent){
        // We are making this node as the most recently used node;
        // so delete the old ref & old node from hashmap;
        const mruOldNode = this.lruCacheHashmap.get(key);
        const nodeVal = mruOldNode.value;

        this.lruCacheHashmap.delete(key);
        this.doublyList.deleteNode(mruOldNode);

        this.doublyList.addNode(mruOldNode);
        this.lruCacheHashmap.set(key, mruOldNode);

        return nodeVal;
    }
    else{
        return -1;
    }    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    const isKeyPresent = this.lruCacheHashmap.has(key) === true;
    if(isKeyPresent){
        // We are updating the key, so we can delete the prevNode,
        // and add the newNode to make it most recently used + its value to be updated;
        const mruOldNode = this.lruCacheHashmap.get(key);

        this.lruCacheHashmap.delete(key);
        this.doublyList.deleteNode(mruOldNode);
    }
    // If the cache size is reached then delete the node,
    // and Add the new node;
    else if(this.lruCacheSize === this.lruCacheHashmap.size){
        const lruNode = this.doublyList.tail.prev;

        this.lruCacheHashmap.delete(lruNode.key);
        this.doublyList.deleteNode(lruNode);
    }

    // Then ADD THE new Node or Update the node value + ref;
    const mruNewNode = new DLLNode(key, value);
    this.doublyList.addNode(mruNewNode);
    this.lruCacheHashmap.set(key, mruNewNode);

    return null;
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

 /** 
 
// Brute Force Solution, using the searching, Deleting, and Adding to front technique
var LRUCache = function(capacity) {
    this.lruCacheSize = capacity;
    this.lruCacheHashmap = new Map();
    this.lruCacheData = [];
};

LRUCache.prototype.get = function(key) {
    const isKeyPresent = this.lruCacheHashmap.has(key) === true;
    if(isKeyPresent){
        let keyIdx = -1;
        this.lruCacheData.forEach((data, idx) => {
            if(data[0] === key){
                keyIdx = idx;
            }
        });

        this.lruCacheData = [this.lruCacheData[keyIdx], ...this.lruCacheData.slice(0, keyIdx), ...this.lruCacheData.slice(keyIdx + 1)];
        return this.lruCacheData[0][1];
    }
    else{
        return -1;
    }
};

LRUCache.prototype.put = function(key, value) {
    // If the key already exist;
    const isKeyPresent = this.lruCacheHashmap.has(key) === true;
    if(isKeyPresent){
        let keyIdx = -1;
        this.lruCacheData.forEach((data, idx) => {
            if(data[0] === key){
                keyIdx = idx;
            }
        });

        this.lruCacheData = [[key, value], ...this.lruCacheData.slice(0, keyIdx), ...this.lruCacheData.slice(keyIdx + 1)];
    }
    // If the cache size is reached;
    else if(this.lruCacheSize === this.lruCacheData.length){
        const [oldKey, value] = this.lruCacheData.pop();
        this.lruCacheHashmap.delete(oldKey);
    }

    this.lruCacheData.unshift([key, value]);
    this.lruCacheHashmap.set(key, true);
    return null;
};
 */