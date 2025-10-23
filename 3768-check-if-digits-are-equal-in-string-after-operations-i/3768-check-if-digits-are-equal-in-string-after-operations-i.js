/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    const digitsStack = s.split('');

    while(digitsStack.length > 2){
        for(let idxI = 0; idxI < digitsStack.length - 1; idxI++){
            let currEl = digitsStack[idxI];
            let nextEl = digitsStack[idxI + 1];
    
            const newEl = (Number(currEl) + Number(nextEl)) % 10;
            digitsStack[idxI] = newEl;
        }
        digitsStack.pop();
    }

    // console.log(digitsStack);
    return digitsStack[0] === digitsStack[1];
};