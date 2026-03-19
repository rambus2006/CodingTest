import java.util.Scanner;
public class Main{
	public static void main(String args[]){
		Scanner scan=new Scanner(System.in);
		
		//현재 시각
		//시
		int H= scan.nextInt();
		//분
		int M= scan.nextInt();
		//요리하는데 필요한 시간
		int CookingTime=scan.nextInt();
	
		//요리하는데 걸리는 시간(필요한 시간/60+1)
		H+=CookingTime/60;
		//요리하는데 걸리는 분(필요한 시간%60+1)
		M+=CookingTime%60;

		//분이 60 넘어가면 (시간+1)과 (60-분)
		if(M >= 60){
			H +=1;
			M-=60;
		}
		//시간이 24를 넘어가면 (시간-24) 진행
		if(H >= 24) H-= 24;
		
		System.out.println(H+" "+M);
		
	}
}