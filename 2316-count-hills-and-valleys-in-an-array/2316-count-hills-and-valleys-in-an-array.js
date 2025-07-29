/**
 * @param {number[]} nums
 * @return {number}
 */
var countHillValley = function(nums) {
    // Observation:
    // Both the non-equal neighbors should be smaller to be a hill
    // Both the non-equal neighbors should be larger to be a valley
    // Same hill or valley if value at adjacent indexes i & j are same i.e nums[i] === nums[j] 

    let totalHillValleyCount = 0;
    const numsArrLen = nums.length;

    const firstElIdx = 1;
    const lastElIdx = numsArrLen - 1;

    for(let idxI = firstElIdx; idxI < lastElIdx; idxI++){
        let nonDuplicateElIdx = idxI + 1;

        while(nonDuplicateElIdx < numsArrLen && nums[idxI] === nums[nonDuplicateElIdx]){
            nonDuplicateElIdx++;
        }

        if(nonDuplicateElIdx === numsArrLen){
            return totalHillValleyCount;
        }

        const prevNonDuplicateEl = nums[idxI - 1];
        const currEl = nums[idxI];
        const nextNonDuplicateEl = nums[nonDuplicateElIdx];

        // console.log(prevNonDuplicateEl, currEl, nextNonDuplicateEl)

        const isHillNeighborsSmaller = (currEl > prevNonDuplicateEl) && (currEl > nextNonDuplicateEl);
        const isValleyNeighborsLarger = (currEl < prevNonDuplicateEl) && (currEl < nextNonDuplicateEl);

        if(isHillNeighborsSmaller || isValleyNeighborsLarger){
            totalHillValleyCount++;
        }

        idxI = nonDuplicateElIdx - 1;
    }

    return totalHillValleyCount;
};