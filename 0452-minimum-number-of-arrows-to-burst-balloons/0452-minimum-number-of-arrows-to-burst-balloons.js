/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    // Solution using mergedIntervals logic: This fails
    // And the observation here is that no need to merged
    // the points when they overlap, instead keep the first one
    // and keep changing for the remaining ones.
    // Sort the points based on the start val and if
    // multiple points have same start val then sort by end val
    
    // Solution using mergedIntervals logic: This Works
    // And the observation here is that no need to merged
    // the points when they overlap, instead keep the first one
    // and keep changing for the remaining ones.
    // Sort the points based on the end val and if
    // multiple points have same end val then sort by start val

    points.sort((pointA, pointB) => {
        if (pointA[1] === pointB[1]){
            return pointA[0] - pointB[0];
        }
        return pointA[1] - pointB[1]
    });

    // console.log(points);

    let minNumOfArrowsShot = 1;
    let prevPoint = points[0];

    for(let idxI = 1; idxI < points.length; idxI++){
        const currPoint = points[idxI];
        if(prevPoint[1] >= currPoint[1] || prevPoint[1] >= currPoint[0]){
            continue;
        }
        else{
            prevPoint = currPoint;
            minNumOfArrowsShot += 1;
        }
    }

    return minNumOfArrowsShot;
};