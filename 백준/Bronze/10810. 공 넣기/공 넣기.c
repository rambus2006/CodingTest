#include <stdio.h>

int main() {
	int n, m;
	int arg[101] = { 0, };
	int a,b,c;
	
	scanf("%d %d", &n,&m);
	
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &a, &b, &c);
		for (int k = a; k <= b; k++) {
			arg[k] = c;
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", arg[i]);
	}
	return 0;
}