import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int maxnum=-1000000;
		int minnum=1000000;
		int N=scan.nextInt();
		int []essence = new int [N];
		for(int i=0;i<N;i++) {
			essence[i]=scan.nextInt();
			//최댓값 구하기 
			if(essence[i]>maxnum) {
				maxnum=essence[i];
			}
			//최소값 구하기 
			if(essence[i]<minnum) {
				minnum=essence[i];
			}
			
		}
		System.out.println(minnum+" "+maxnum);
		

	}

}