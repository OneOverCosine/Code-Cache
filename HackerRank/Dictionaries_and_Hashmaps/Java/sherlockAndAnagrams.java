
public class sherlockAndAnagrams {
    public static void main(String[] args){
        /* This is setup for a the problem*/
        System.out.println("Starting...");

        String text = "1234567"; // test string

        int window;// the number of characters to consider during each pass

        // these loops simulate how I'd go about checking by hand
        for(window = 1; window < text.length(); window++){

            for(int i = 0; i < text.length() - window; i++){

                System.out.println("| " + text.substring(i, i + window) + " |");

                for(int j = i + 1; j < text.length() - window + 1; j++){
                    //print the text I'll be working with
                    System.out.println("    > " + text.substring(j, j + window));
                }
            }
            System.out.println();
        }
    }
}