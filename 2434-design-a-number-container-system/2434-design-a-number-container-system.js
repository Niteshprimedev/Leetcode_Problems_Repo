
var NumberContainers = function() {
    // Pseudocode & Solution USING Hashamap + Array only;
    // Logic to work with the class type of Leetcode problems
    // Initialize the generic variables and methods inside the main class;
    // Write the methods logic inside the prototype.method() & return the required value
    // Create a numberSystemHashmap variable and initialize it to an empty hashmap
    // Create a indexSystemHashmap variable and initialize it to an empty hashmap
    // For change() method that takes two params index and number
    // Create a numHashKey variable and initialize it to number
    // Create a hashValues variable and initialize it to an empty array;
    // Update the numHashKey variable value with the number param
    // Create a isNumberToBeAdded variable and initialize it to the boolean result of whether a 
    // number is already added in the hashmap or needs to be added
    // Create a isNumberToBeReplaced variable and initialize it to the boolean result of whether an 
    // index is already has a value or not
    // Update the numberSystemHashmap with the numHashKey as its key & hashValues as its value
    // if the isNumberToBeAdded boolean variable is true

    // Do the following if isNumberToBeReplaced variable value is true
    // This is to remove the index for the previous number & updating the hashmap 
    // Create a newNumHashKey variable and initialize it to the value of index key in
    // the indexSystemHashmap variable
    // Update the hashValues value with the value of newNumHashKey key in the 
    // the numberSystemHashmap variable
    // Create a removingIdx variable and initialize it to the index value of the index
    // in the hashValues array
    // Remove the index value using the splice method from the hashValues for the newNumHashKey
    // Update the numberSystemHashmap with the newNumHashKey as its key & hashValues as its value
    // Adding the index for the number key in the numberSystemHashmap
    // & updating the number for the index key in the indexSystemHashmap
    // Update the hashValues value with the value of numHashKey key in the 
    // the numberSystemHashmap variable
    // Push the index value into the hashValues array 
    // Update the numberSystemHashmap with the numHashKey as its key & hashValues as its value
    // Update the indexSystemHashmap with the index as its key & number as its value

    // For find() method that takes one param index
    // Update the hashKey variable value with the number param
    // Create a smallestIdxEl variable and initialize it to -1
    // Create a isNumberNotFound varaible and initalize it to a boolean value true if the
    // number is not available in the numberSystemHashmap else it will be false
    // Return smallestIdxEl i.e -1 if the isNumberNotFound value is true
    // Else: continue to find the smallest index of the number
    // Create a indexValuesArrOfNum variable and initalize it to values array of this.hashKey key
    // Create a arrLoopLen variable and initialize it to the length value of the indexValuesArrOfNum
    // Run a for loop through the indexValuesArrOfNum from idxI = 0 to idxI < arrLoopLen value
    // Create a currIdxEl variable and initialize it to the index idxI value in the indexValuesArrOfNum
    // variable
    // Update the smallestIdxEl with the index 0 value in the indexValuesArrOfNum if the smallesIdxEl value
    // is equals to -1;
    // Update the smallestIdxEl value with the minimum value among the smallestIdxEl & the currIdxEl values
    // Return the smallesIdxEl value once the loop is over;
    // Finally, we would have compelted our design for the number container system that inserts or replaces
    // a number at the given index as well as returns the smallest index of the given number 


    // Just to initialize and make use of variables;
    this.numberSystemHashmap = new Map();
    this.indexSystemHashmap = new Map();

    return null;
};

/** 
 * @param {number} index 
 * @param {number} number
 * @return {void}
 */
NumberContainers.prototype.change = function(index, number) {
    // Just updates the container with the number at the given index
    let numHashKey = number;
    let hashValues = [];

    const isNumberToBeAdded = this.numberSystemHashmap.has(numHashKey) !== true;
    const isNumberToBeReplaced = this.indexSystemHashmap.has(index);

    // isNumberToBeAdded
    if(isNumberToBeAdded){
        this.numberSystemHashmap.set(numHashKey, hashValues);
    }

    // isNumberToBeReplaced
    if(isNumberToBeReplaced){
        const newNumHashKey = this.indexSystemHashmap.get(index);

        hashValues = this.numberSystemHashmap.get(newNumHashKey);
        const removingIdx = hashValues.indexOf(index);
        hashValues.splice(removingIdx, 1);
        this.numberSystemHashmap.set(newNumHashKey, hashValues);
    }

    hashValues = this.numberSystemHashmap.get(numHashKey);
    hashValues.push(index);
    // console.log('True NumberToBeAdded', hashValues);

    this.numberSystemHashmap.set(numHashKey, hashValues);
    this.indexSystemHashmap.set(index, number);

    return null;
};

/** 
 * @param {number} number
 * @return {number}
 */
NumberContainers.prototype.find = function(number) {
    // Returns the smallest index of the number in the container
    // console.log(this.numberSystemHashmap);

    let smallestIdxEl = -1;
    const isNumberNotFound = this.numberSystemHashmap.has(number) !== true;
    if(isNumberNotFound){
        return smallestIdxEl
    }

    // else;
    const indexValuesArrOfNum = this.numberSystemHashmap.get(number);
    const arrLoopLen = indexValuesArrOfNum.length;

    for(let idxI = 0; idxI < arrLoopLen; idxI++){
        let currIdxEl = indexValuesArrOfNum[idxI];
        
        if(smallestIdxEl === -1){
            smallestIdxEl = indexValuesArrOfNum[0];
        }
        smallestIdxEl = Math.min(smallestIdxEl, currIdxEl);
    }

    return smallestIdxEl;
};

/** 
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */