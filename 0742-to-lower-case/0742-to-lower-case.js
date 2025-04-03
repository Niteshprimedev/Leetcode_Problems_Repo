/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    // They want us to get the ASCII Values & convert them
    // into lower case ASCII values;
    // Lower Case Chars ASCII Values range (97, 123);
    // Upper Case Chars ASCII Values range (65, 91);

    // Better Soln:
    let lowerCaseStrS = '';

    let idxI = 0;
    for(let char of s){
        let lowerCaseChar = char;

        const charCode = s.charCodeAt(idxI);
        if(charCode >= 65 && charCode <= 90){
            const lowerCaseCharCode =  charCode + 32;
            lowerCaseChar = String.fromCharCode(lowerCaseCharCode);
        }

        lowerCaseStrS += lowerCaseChar;
        idxI++;
    }

    return lowerCaseStrS;

    /** 
    const lowerCaseAlphabets = "abcdefghijklmnopqrstuvwxyz";
    const lowerCaseCharsHashmap = new Map();

    for(let charIdx = 0; charIdx < 26; charIdx++){
        const hashKey = lowerCaseAlphabets[charIdx];
        const hashValue = charIdx + 97;

        lowerCaseCharsHashmap.set(hashValue, hashKey);
    }

    let lowerCaseStrS = '';

    let idxI = 0;
    for(let char of s){
        let lowerCaseChar = char;

        const charCode = s.charCodeAt(idxI);
        if(charCode >= 65 && charCode <= 90){
            const lowerCaseCharCode =  charCode + 32;
            lowerCaseChar = lowerCaseCharsHashmap.get(lowerCaseCharCode);
        }

        lowerCaseStrS += lowerCaseChar;
        idxI++;
    }
    console.log(s.charCodeAt(1));

    return lowerCaseStrS;
    // return s.toLowerCase();
    */
};