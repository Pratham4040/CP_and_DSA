public class palindrome {
    public static void main(String[] args) {
        String input ="raceacar";
        int st = 0;
        int  end = input.length()-1; 
                while(st<end){
                    if(input.charAt(st)!=input.charAt(end)){
                        System.out.println("False");
                    }
                    else{
                        System.out.println("TRue");
                    }
                    st += st;
                    end-= end;
                    
                }}}
    
                class Solution {
                    public boolean isPalindrome(String s) {
                        String a ="";
                        for(int i=0;i<s.length();i++){
                            if('a'<=s.charAt(i)&&s.charAt(i)<='b'){
                               a = a+s.charAt(i);
                            }
                        }
                        String lower = a.toLowerCase();
                        int st = 0;
                        int  end = lower.length()-1; 
                                while(st<=end){
                                    if(lower.charAt(st)!=lower.charAt(end)){
                                        return false;
                                    }
                                    st += st;
                                    end-= end;
                                    
                                }
                                return true;
                
                    }
                }

