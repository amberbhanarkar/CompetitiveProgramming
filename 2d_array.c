#include <stdio.h>

void matrix() {
  int i, j, num, a[6][6];
  for (i = 0; i < 6; i++) {
    for (j = 0; j < 6; j++) {
      scanf("%d", &num);
      a[i][j] = num;
    }
  }
  int jj = 0, maxsum = -1000;
  for (i = 0; i < 4; i++) {
    int sum = 0;
    for (j = jj; j < jj + 3; j++) {
      sum += a[i][j];
      if (j == jj) {
        sum += a[i + 1][jj + 1];
      }
      sum += a[i + 2][j];
    }
    jj = (jj < 3) ? jj + 1 : 0;
    if (maxsum < sum) {
      maxsum = sum;
    }
    if (jj != 0)
      i--;
  }
  printf("%d", maxsum);
}
int main() 
{ 
    matrix(); 
    return 0;}

