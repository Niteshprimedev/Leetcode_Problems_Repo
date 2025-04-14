/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    // 3Sum Logic:
    let goodTripletsCount = 0;
    const arrLen = arr.length;

    for(let firstNumIdx = 0; firstNumIdx < arrLen - 2; firstNumIdx++){
        const firstNum = arr[firstNumIdx];
        
        // let secondNumIdx = firstNumIdx + 1;
        // let thirdNumIdx = secondNumIdx + 1;

        // while(secondNumIdx < thirdNumIdx && thirdNumIdx < arrLen){
            // const secondNum = arr[secondNumIdx];
            // const thirdNum = arr[thirdNumIdx];

            // // Condition to be checked;
            // const absFirstSecondDiff = Math.abs(firstNum - secondNum);
            // const absSecondThirdDiff = Math.abs(secondNum - thirdNum);
            // const absFirstThirdDiff = Math.abs(firstNum - thirdNum);

            // if(absFirstSecondDiff <= a && absSecondThirdDiff <= b && absFirstThirdDiff <= c){
            //     goodTripletsCount += 1;
            // }

        //     console.log(firstNum, secondNum, thirdNum);

        //     secondNumIdx += 1;
        //     thirdNumIdx += 1;
        // }

        for(let secondNumIdx = firstNumIdx + 1; secondNumIdx < arrLen - 1; secondNumIdx++){
            const secondNum = arr[secondNumIdx];

            const absFirstSecondDiff = Math.abs(firstNum - secondNum);
            if(absFirstSecondDiff > a){
                continue;
            }

            for(let thirdNumIdx = secondNumIdx + 1; thirdNumIdx < arrLen; thirdNumIdx++){
                const thirdNum = arr[thirdNumIdx];
                // Condition to be checked;
                const absSecondThirdDiff = Math.abs(secondNum - thirdNum);
                if(absSecondThirdDiff > b){
                    continue;
                }
                const absFirstThirdDiff = Math.abs(firstNum - thirdNum);

                if(absFirstThirdDiff <= c){
                    goodTripletsCount += 1;
                }
            }
        }
    }

    return goodTripletsCount;
};