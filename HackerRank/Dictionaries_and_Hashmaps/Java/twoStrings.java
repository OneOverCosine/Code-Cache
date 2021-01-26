import java.util.Hashtable;

public class twoStrings {
    public static void main(String[] args){
        /* I attempted this problem in python first
        so my thoughts should be in twoStrings.py
        the code below is setup for the function */

        String s1 = "hello";
        String s2 = "world";

        System.out.println("Do " + s1 + " and " + s2 + " contain any common substrings?");
        System.out.println(twoStringsProblem(s1, s2));
    }

    // Complete the twoStrings function below.
    static String twoStringsProblem(String s1, String s2) {
        /* ntoes: */

        // create a hashtable to hold all the letters that appear in s1
        Hashtable<Character, Boolean> s1Hash = new Hashtable<>();

        for(int i = 0; i < s1.length(); i++){

            if(s1Hash.size() == 26){
                return "YES"; // if every letter in the alphabet is in s1, both strings must have a substring in common
            }

            s1Hash.putIfAbsent(s1.charAt(i), true); // true here just means that the letter is in s1
        }

        // check the letters s2
        for(int i = 0; i < s2.length(); i++){
            if(s1Hash.get(s2.charAt(i)) == true){
                // this part needs some work
                return "YES";
            }
        }

        return "NO"; // after going through the whole string, there weren't any matches
    }
}