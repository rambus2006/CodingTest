import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();

        for (int t = 0;t<T;t++){
            String vpsString = sc.nextLine();
            Stack<Character> stack = new Stack<>();
            boolean isVPS = true;

            for (char ch:vpsString.toCharArray()){
                if (ch == '('){
                    stack.push(ch);
                }else if (ch==')'){
                    if(!stack.isEmpty()){
                        stack.pop();
                    }else{
                        System.out.println("NO");
                        isVPS = false;
                        break;
                    }
                }
            }
            if (isVPS){
                if(stack.isEmpty()){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
        sc.close();
    }
}