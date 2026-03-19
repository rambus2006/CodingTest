#include <stdio.h>

int main(void) {
	int n;
	int x;
	int temp = 0;
	int i;
	int h = 0;

	int arr[10001];

	scanf("%d %d", &n,&x);
	//입력
	for (i = 0; i < n; i++) {
		scanf("%d ", &arr[i]);
		if (0<arr[i]&& arr[i] < x) {
			printf("%d ", arr[i]);
		}
		
	}
	

	return 0;
}
