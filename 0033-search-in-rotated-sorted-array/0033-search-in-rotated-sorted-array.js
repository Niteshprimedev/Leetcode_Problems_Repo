/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // Logic: if the middle idx val is greater than the right most
    // value then the pivot idx exists to the right of middle idx
    // If the middle idx val is smaller than the right most value
    // value then the pivot idx exists to the left of middle idx
    // Figured out a way to find the pivot idx after spending a good 
    // amount of time and then solved it using pivot idx & 2 binary searches
    // First binary search in first sorted array and second binary search
    // in the array which is after pivot idx i.e pivot idx + 1;

/**
#### Quick Revision Notes:

- Solution Thought Process: Assuming that array is just sorted then apply the binary search to find the target. But If the sorted array is also rotated then we know that the largest element will lie somewhere in the middle and we consider it the pivotIdx. 
- One way: If we can figure out the `pivotIdx` in this rotated sorted array then, we know there are two sorted arrays: one ending at `pivotIdx` and another one starting from `pivotIdx + 1`! So we can run binary search two times in two sorted arrays to find the target;
- Another way: If we can figure out which side is `sorted` then it would be easy to find the target in the sorted array right? So what do we do? We start off with binary search and figure out is left part sorted? by checking (elAtLeftIdx <= elAtMiddleIdx) if it is true? then we check whether the target lies within the range[leftEl, middleEl] if not
- Then move to the right side and discard the left side, else we keep looking at the left part! And if the left part is not
sorted then the rightPart is sorted so we check is right part sorted? by checking (elAtMiddleIdx <= elAtRightIdx)
This way we can apply binary search?
 */
 
    const numsLen = nums.length;

    function findPivotIdx(nums, target){
        let leftIdx = 0;
        let rightIdx = numsLen - 1;
        let pivotIdx = -1;

        while(leftIdx <= rightIdx){
            const middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

            if(nums[middleIdx] > target){
                pivotIdx = middleIdx;
                leftIdx = middleIdx + 1;
            }
            else if(nums[middleIdx] < target){
                rightIdx = middleIdx - 1;
            }
            else if(nums[middleIdx] === target){
                break;
            }
        }

        return pivotIdx;
    }

    const pivotIdx = findPivotIdx(nums, nums[numsLen - 1]);

    function findElement(leftIdx, rightIdx, target){
        if(leftIdx < 0 || leftIdx === numsLen || rightIdx < 0 || rightIdx === numsLen ){
            return -1;
        }

        while(leftIdx <= rightIdx){
            const middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

            if(nums[middleIdx] === target){
                return middleIdx;
            }
            else if(nums[middleIdx] > target){
                rightIdx = middleIdx - 1;
            }
            else{
                leftIdx = middleIdx + 1;
            }
        }

        return -1;
    }

    // console.log(pivotIdx);
    let isElPresent = -1;
    if(pivotIdx !== -1){
        const firstPivotSearch = findElement(0, pivotIdx, target);
        const nextPivotSearch = findElement(pivotIdx + 1, numsLen - 1, target);

        // console.log(firstPivotSearch, nextPivotSearch);
        if(firstPivotSearch !== -1){
            isElPresent = firstPivotSearch;
        }
        else if(nextPivotSearch !== -1){
            isElPresent = nextPivotSearch;
        }
    }
    else{
        isElPresent = findElement(0, numsLen - 1, target);
    }
    
    return isElPresent;
    
    /** 
    // Logic: Binary Search with some sorting concept;
    // if the middle idx val is greater than or equal to the left idx val
    // that means all the numbers between left idx and middle idx are sorted
    // so if they are sorted and the target is present then we can try
    // checking whether the target val is greater than or equal to the 
    // val at left_idx and the target val is smaller than or equal to 
    // the val at middle_idx: if this is true then we move the right_idx
    // to the middle_idx - 1 cause we already checked for the middle idx
    // if nums[leftIdx] <= target <= nums[middleIdx] is not true
    // then we move the leftIdx to the middleIdx + 1 cause we already checked
    // for the middleIdx
    // Again we check which side is sorted and move the leftIdx and rightIdx 
    // to search in the given array;

    // Note: The one half of the array (either the left or the right) will always
    // be sorted (boom!);
    // If the search value is less than the value at the midIdx then narrow the
    // interval or array to the lower half otherwise narror it to the upper
    // half;

    // Revision: After DSA Session 5 on May 17:
    // This same logic was discussed in the class;

    const numsLen = nums.length;
    let targetElIdx = -1;

    let leftIdx = 0;
    let rightIdx = numsLen - 1;

    while(leftIdx <= rightIdx){
        const middleIdx = leftIdx + Math.floor((rightIdx - leftIdx) / 2);

        // The target is found at middle idx?
        if(nums[middleIdx] === target){
            targetElIdx = middleIdx;
            break;
        }
        // is the left part is sorted? and the target is present in it?
        else if(nums[leftIdx] <= nums[middleIdx]){
            // Is the target present to the left side of array;
            if(nums[leftIdx] <= target && target <= nums[middleIdx]){
                // move rightIdx to check the left to middleIdx cause target is present;
                rightIdx = middleIdx - 1;
            }
            else{
                // move the leftIdx to check the right to middleIdx
                leftIdx = middleIdx + 1;
            }
        }
        else{
            // Is the target present to the side of array;
            if(nums[middleIdx] <= target && target <= nums[rightIdx]){
                // move the leftIdx to check the right to middleIdx cause target is present;
                leftIdx = middleIdx + 1;
            }
            else{
                // move rightIdx to check the left to middleIdx
                rightIdx = middleIdx - 1;
            }
        }
    }

    return targetElIdx;
    */
};