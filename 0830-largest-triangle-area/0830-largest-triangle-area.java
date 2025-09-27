class Solution {
    public double largestTriangleArea(int[][] points) {
        int maxX = -51;
        int maxY = -51;

        int n = points.length;

        double maxArea = Double.MIN_VALUE;

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                for(int k = j + 1; k < n; k++){
                    int x1 = points[i][0];
                    int x2 = points[j][0];
                    int x3 = points[k][0];

                    int y1 = points[i][1];
                    int y2 = points[j][1];
                    int y3 = points[k][1];

                    // System.out.println(maxArea);

                    double newMaxArea = 0.5 * Math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
                    maxArea = Math.max(maxArea, newMaxArea);
                }
            }
        }

        return maxArea;
    }
}