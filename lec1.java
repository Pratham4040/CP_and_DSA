import java.io.*;
import java.util.*;

class lec1{
    public static int fact(int n) {
        if(n==1||n==0){
            return 1;
        }
        return n*fact(n-1);
    }
    public static void main(String[] args) {
        int num=4;
        System.out.println(fact(num));
    }
}