import java.util.Hashtable;

public class hashtables {
    public static void main(String[] args){
        /* Messing around with hashtables to gt comfortable using them
        this code doesn't do anything in particular */
        
        System.out.println("Working with Hashtables!");

        Hashtable<String, Integer> ageList = new Hashtable<>();

        ageList.put("Cringe Katalyst", 22);
        ageList.put("Bumblebee", 7);
        ageList.put("PioneerShark", 18);
        ageList.put("2ndSlate", 20);
        
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
