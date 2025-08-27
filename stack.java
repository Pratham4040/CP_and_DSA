import java.util.Stack;

public class stack {
    public static void stackempty(Stack <Integer> st,int Element){
       if(st.isEmpty()){
        st.push(Element);
        return;
       }
       int val = st.pop();
       stackempty(st,Element);
       st.push(val);
      
       
    }
    
    public static void main(String[] args) {
        Stack <Integer> st = new  Stack<>();
        st.push(10);
        st.push(20);
        st.push(30);
        st.push(40);
        st.push(50);
        int element =1000;
        stackempty(st,element);
        System.err.println(st);

         
    }
    
}
