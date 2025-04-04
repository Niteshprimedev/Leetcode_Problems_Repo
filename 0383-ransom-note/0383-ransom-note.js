/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const ransomNoteCharsFreqHashmap = new Map();

    let loopLen = ransomNote.length;
    for(let idxI = 0; idxI < loopLen; idxI++){
        const hashKey = ransomNote[idxI];
        const hashValue = (ransomNoteCharsFreqHashmap.get(hashKey) || 0) + 1;

        ransomNoteCharsFreqHashmap.set(hashKey, hashValue);
    }

    // console.log(ransomNoteCharsFreqHashmap);

    for(let magazineChar of magazine){
        const hashKey = magazineChar;

        const isMagazineCharPresent = ransomNoteCharsFreqHashmap.has(hashKey);
        if(isMagazineCharPresent){
            const hashValue = ransomNoteCharsFreqHashmap.get(hashKey);

            if(hashValue - 1 === 0){
                ransomNoteCharsFreqHashmap.delete(hashKey);
            }
            else{
                ransomNoteCharsFreqHashmap.set(hashKey, hashValue - 1);
            }
        }
    }

    // console.log(ransomNoteCharsFreqHashmap);
    
    const canRansomNoteBeConstructed = ransomNoteCharsFreqHashmap.size === 0 ? true : false;
    return canRansomNoteBeConstructed;

    /**
    // Brute Force Solution;
    let canRansomNoteBeConstructed = true;
    for(let ransomNoteChar of ransomNote){
        const firstIdx = magazine.indexOf(ransomNoteChar);

        if(firstIdx === -1){
            canRansomNoteBeConstructed = false;
            break;
        }
        else{
            magazine = magazine.replace(ransomNoteChar, '');
        }
        // console.log(firstIdx);
    }

    return canRansomNoteBeConstructed;
    */
};