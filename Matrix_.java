import java.util.Scanner;
public class Matrix_ {
    
    public static void maze(int[][] maze,int r,int c){
        if(r<0||c<0||r>=maze.length||c>=maze[0].length||maze[r][c]=='1'){
          return;
        }
        if((r== maze.length-1) && (c ==maze[0].length-1)){
         System.out.println("reached destination");         
        }
        maze[r][c]='1';
        maze(maze, r+1, c);
        maze(maze, r, c+1);
        maze(maze, r-1, c);
        maze(maze, r, c-1);
        maze[r][c]='0';

    }
    public static void main(String[]args){
        int[][] array={{0,1,1},{0,0,1},{1,0,0}};
        maze(array, 0, 0);  
    }
}

