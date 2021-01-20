import java.util.Hashtable;

public class ransomNote {

    public static void main(String[] args){
        /* setup for challenge */
        System.out.println("== Ransom Note (Java) ==");

        String m = "Hello World";
        String n = "Hello world";

        String[] magazine = m.split(" ");
        String[] note = n.split(" ");

        checkMagazine(magazine, note);
    }

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {
        //since case is important, I don't need to do any conversions

        // first, create a hashtable for all the words in the magazine    
        Hashtable<String, Integer> magWordCount = new Hashtable<>();

        for(String word : magazine){
            if(magWordCount.get(word) == null){
                magWordCount.put(word, 1);// add the word to the hashtable if it's not there
            }
            else{
                magWordCount.put(word, magWordCount.get(word) + 1);// if the word's already there, add one to the count
            }
        }

        // now go through the note and see if it can be written from the magazine words
        
        int count = 0;

        for(String word : note){
            if(magWordCount.get(word) == null || magWordCount.get(word) == 0){
                // null is for if the word was never in the list. 0 is for if it was removed
                System.out.println("No");
                break;
            }
            else{
                magWordCount.put(word, magWordCount.get(word) - 1);
                count++;
            }
        }

        if(count == note.length){
            System.out.println("Yes");
        }
    }
}