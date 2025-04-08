/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const repeatedNumberMap = new Map();
    repeatedNumberMap.set(n, 'seen');

    while(n !== 1){
        let digit = n % 10;
        let digitsSq = Math.pow(digit, 2);
        n = Math.floor(n / 10);

        while(n > 0){
            digit = n % 10;
            digitsSq += Math.pow(digit, 2);
            n = Math.floor(n / 10);
        }

        console.log(digit, digitsSq, n);
        n = digitsSq;

        const isNumberRepeated = repeatedNumberMap.has(n) === true;
        if(isNumberRepeated){
            return false;
        }
        else{
            repeatedNumberMap.set(n, 'seen');
        }
    }

    return n === 1;
};