public class LinkedList {
    class Node{
        int data;
        Node next;
    }
    private Node head;
    private Node tail;
    private int size;
    public void addFirst(int element){
        Node newList = new Node();
        newList.data=element;
        if (size==0){
            head = newList;
            tail =newList;
            size ++;
        }
        else {
            newList.next = head;
            head = newList;
            size ++;
        }
    }
    public void display(){
      Node nodetemp = head;
      while(nodetemp!=null){
      System.out.println(nodetemp.data);
      nodetemp = nodetemp.next;
      }
    }
}
