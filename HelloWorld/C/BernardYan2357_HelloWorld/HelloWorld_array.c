#include <stdio.h>
#include <string.h>
int main(){
    int i = 0;
    char str[100] = "Hello,World!";
    for(;;){
        if (str[i] == '\0') {
            break;
        }
        printf("%c", str[i]);
        i++;

    }
    return 0;
}
