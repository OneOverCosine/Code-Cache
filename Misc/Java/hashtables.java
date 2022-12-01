import java.util.Hashtable;

public class hashtables {
    public static void main(String[] args){
        /* Messing around with hashtables to get comfortable using them
        this code doesn't do anything in particular */
        
        System.out.println("Working with Hashtables!");

        Hashtable<String, Integer> ageList = new Hashtable<>();

        ageList.put("Cringe Katalyst", 24);
        ageList.put("Bumblebee", 9);
        ageList.put("PioneerShark", 19);
        ageList.put("2ndSlate", 22);
        
        String name = "Cringe Katalyst";

        System.out.println(name + "'s age is " + ageList.get(name));

        String text = "I like to think that you and I are very similiar";
        String[] words = text.split(" ");

        Hashtable<String, Integer> wordList = new Hashtable<>();

        for(String word : words){
            if(wordList.get(word) == null){
                wordList.put(word, 1);
            }
            else{
                wordList.put(word, wordList.get(word) + 1);
            }
        }

        System.out.println(wordList);
    }
}
