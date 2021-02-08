public class Array2d_DS {
    // for the 2D Array - DS practice problem

    public static void main(String[] args){

        // some setup
        int[][] arr = {{1,1,1,0,0,0}, {0,1,0,0,0,0}, {1,1,1,0,0,0}, {0,0,2,4,4,0}, {0,0,0,2,0,0}, {0,0,1,2,4,0}};// in this problem, the array is always 6x6

        int largest = originalSolution(arr); // that is, the largest sum of the hourglasses

        System.out.println("Largest hourglass sum: " + largest);
    }

    static int originalSolution(int[][] arr){

        int[] hourglass = new int[7];

        int[] sums = new int[16];
        int sumCount = 0;

        for(int row = 0; row < arr.length ; row++){
            for(int col = 0; col < arr.length; col++){
                hourglass = getHourglass(arr, row, col);

                if(hourglass != null){

                    for(int i = 0; i < hourglass.length; i++){
                        sums[sumCount] = sums[sumCount] + hourglass[i];
                    }
                    sumCount++;
                }
            }
        }

        int largest = sums[0];
        for(int i = 1; i < sums.length; i++){

            if(largest < sums[i]){
                largest = sums[i];
            }
        }

        return largest;
    }

    static int[] getHourglass(int[][] arr, int row, int col){

        //will return null as soon as an index is out of range

        int[] hourglass = new int[7];
        int index = 0;

        for(int i = -1; i <= 1; i++){
            //for the rows
            for(int j = -1; j <= 1; j++){
                //for the columns
                if(row + i >= 0 && row + i < arr.length){
                    if(col + j >= 0 && col + j < arr.length){
                        //if the indecies are in range, add to the array
                        //if in range, make sure it's part of the hourglass
                        if(i == 0 && j != 0){
                            continue;// on row 0, only col 0 is part of the hourglass
                        }

                        hourglass[index] = arr[row + i][col + j];
                        index++;
                    }
                    else{
                        return null;
                    }
                }
                else{
                    return null;
                }
            }
        }
    
        return hourglass;
    }
}
