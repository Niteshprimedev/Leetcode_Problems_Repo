/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    // Sort the array first to use two pointers technique
    nums.sort((a, b) => a - b);

    const allUniqueQuadruples = [];

    // Logic, fix your var a and then use 3Sum logic
    // to find var b, var c, var d values to have one quadruplet

    for(let firstNumIdx = 0; firstNumIdx < (nums.length - 3); firstNumIdx++){
        const firstNum = nums[firstNumIdx];

        if(firstNumIdx > 0 && nums[firstNumIdx - 1] === firstNum){
            continue;
        }
        
        // 3Sum Logic
        for(let secondNumIdx = firstNumIdx + 1; secondNumIdx < (nums.length - 2); secondNumIdx++){
            const secondNum = nums[secondNumIdx];
            if(secondNumIdx > (firstNumIdx + 1) && nums[secondNumIdx - 1] === secondNum){
                continue;
            }

            let thirdNumIdx = secondNumIdx + 1;
            let forthNumIdx = nums.length - 1;

            while(thirdNumIdx < forthNumIdx){
                const thirdNum = nums[thirdNumIdx];
                const forthNum = nums[forthNumIdx];

                const quadrupletSum = firstNum + secondNum + thirdNum + forthNum;

                if(quadrupletSum === target){
                    allUniqueQuadruples.push([firstNum, secondNum, thirdNum, forthNum]);

                    thirdNumIdx += 1;
                    forthNumIdx -= 1;

                    while (thirdNumIdx < forthNumIdx && nums[thirdNumIdx] === thirdNum){
                        thirdNumIdx += 1;
                    }
                }
                else if(quadrupletSum < target){
                    thirdNumIdx += 1;
                }
                else if(quadrupletSum > target){
                    forthNumIdx -= 1;
                }
            }
        }
    }
    return allUniqueQuadruples;
};