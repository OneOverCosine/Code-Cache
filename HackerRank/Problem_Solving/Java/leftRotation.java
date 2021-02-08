import java.util.*;

class leftRotation {
    public static void main(String[] args){
        System.out.println("Running...");

        List arr = Arrays.asList(1, 2, 3, 4, 5);
        int rotations = 3;

        List shifted = originalSolution(rotations, arr);

        for(int i = 0; i < shifted.size(); i++){
            System.out.printf(shifted.get(i) + " ");
        }
    }

    static List<Integer> originalSolution(int d, List<Integer> arr){
        List<Integer> shifted = new ArrayList<>(arr.size());// new empty list        

        for(int i = 0; i < arr.size(); i++){
           shifted.add(arr.get((i+d)%arr.size()));  
        }
    
        return shifted;
    }
}