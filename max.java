public class max {
    public static void main(String[] args) {
                    
               
                int[] arr = {12,64,70,80,78,76};
                int max = arr[0];
                int max2= arr[0];
                for(int i = 0; i < arr.length; i++){
                    if(arr[i]>max){
                        max = arr[i];
                        }
                    }
                    System.out.println(max);

                for(int k=0;k<(arr.length);k++){
                    if(arr[k]>max2){
                        if(arr[k] != max){
                        max2 = arr[k];
                        }
                    }
                       
                }
                System.out.println(max2);
                           
}
}

