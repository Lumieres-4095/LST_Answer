#include <stdio.h>

int main(void) {
    int cnt = 0;

    for (int i = 1; i <= 3; i++){
        for (int j = 1; j <= 5; j++) {
            for (int k = 1; k <= 3; k++) {
                for (int l = 1; l <= 5; l++) {
                    if ((i == j) != (k == l)) {
                        cnt++;
                    }
                }
            }           
        }
    }

    printf(cnt);

    return 0;
}