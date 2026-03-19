#include <stdio.h>

int main(void) {
	int n;
	int arr[101];
	int v = 0;
	int count=0;

	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	scanf("%d", &v);
	for (int i = (n - 1); i >= 0; i--) {
		if (arr[i] == v) {
			count++;
		}
	}
	printf("%d", count);

	return 0;
}
