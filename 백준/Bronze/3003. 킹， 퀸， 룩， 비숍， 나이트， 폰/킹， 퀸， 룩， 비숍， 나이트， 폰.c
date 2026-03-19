#include <stdio.h>

int main(){
			int king;
			int queen;
			int rook;
			int bishop;
			int knight;
			int phone;
	
			scanf("%d %d %d %d %d %d",&king,&queen,&rook,&bishop,&knight,&phone);
			
			king=(1-king);
			queen=(1-queen);
			rook=(2-rook);
			bishop=(2-bishop);
			knight=(2-knight);
			phone=(8-phone);
		
			printf("%d %d %d %d %d %d",king,queen,rook,bishop,knight,phone);
			
			return 0;
}