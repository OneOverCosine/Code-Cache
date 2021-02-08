public class arraysDS {
    public static void main(String[] args){
        /* the goal was to write code that would reverse an array */

        int[] a = {2, 4, 6, 8, 10};

        int[] b = originalSolution(a);
        //int[] c;

        System.out.println("Reversed array: ");
        for(int num : b){
            System.out.printf(num + " ");
        }
    }

    static int[] originalSolution(int[] a){
        
        int[] reversed = new int[a.length];
        int index = 0;

        for(int i = a.length - 1; i >= 0; i--){

            reversed[index] = a[i];
            index++;
        }

        return reversed;
    }
}