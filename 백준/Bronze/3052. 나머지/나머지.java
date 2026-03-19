import java.util.Scanner;
import java.util.Arrays;
public class Main{
	public static void main(String args[]) {
		Scanner scan=new Scanner(System.in);
		int num[]=new int [10];
		int count=1;
		
		for(int i=0;i<10;i++) {
			num[i]=scan.nextInt()%42;
		}
		Arrays.sort(num);
		for(int a=0;a<num.length-1;a++) {
			if(num[a]!=num[a+1]) {
				count++;
			}
		}
		System.out.println(count);
	}
}
