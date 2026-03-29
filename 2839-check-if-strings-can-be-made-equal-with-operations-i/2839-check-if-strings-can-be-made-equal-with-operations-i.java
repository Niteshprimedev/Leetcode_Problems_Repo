class Solution {
    public boolean canBeEqual(String s1, String s2) {
        if(s1.equals(s2)) return true;

        if(s1.charAt(0) != s2.charAt(0)){
            StringBuilder sbS3 = new StringBuilder("");

            sbS3.append(s1.charAt(2));
            sbS3.append(s1.charAt(1));
            sbS3.append(s1.charAt(0));
            sbS3.append(s1.charAt(3));

            s1 = sbS3.toString();
        }

        if(s1.equals(s2)) return true;

        System.out.println(s1);

        if(s1.charAt(1) != s2.charAt(1)){
            StringBuilder sbS3 = new StringBuilder("");

            sbS3.append(s1.charAt(0));
            sbS3.append(s1.charAt(3));
            sbS3.append(s1.charAt(2));
            sbS3.append(s1.charAt(1));

            s1 = sbS3.toString();
        }

        if(s1.equals(s2)) return true;

        return false;
    }
}