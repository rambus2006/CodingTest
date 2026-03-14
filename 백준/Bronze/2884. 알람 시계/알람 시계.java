import java.util.Scanner;
public class Main{
	public static void main(String args[]){
		Scanner scan=new Scanner(System.in);
		int H=scan.nextInt();        //시간변수 입력 및 선언
		int M=scan.nextInt();        //분 변수 입력 및 선언

         //분이 45보다 크면 시간은 놔두고 분에만 45를 빼서 계산한다.
		if(M>=45) System.out.println(H+" "+(M-45));    
        //분이 45보다 작다면
		else{
            //만약 시간이 0시간이면 24시간으로 지정
			if(H==0) H=24;
                //24시간에서 1시간을 뺀 후 분에 60을 더한 후 45분을 뺀다.
				System.out.println((H-1)+" "+(60+M-45));
		}
	}
}