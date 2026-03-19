import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int num[]=new int[9];
		int number=0;
		int max=0;
		for(int i=0;i<9;i++) {
			num[i]=scan.nextInt();
			if(num[i]>max) {
				max=num[i];
				number=i+1;
			}
		}
		System.out.println(max);
		System.out.println(number);
		

	}

}
