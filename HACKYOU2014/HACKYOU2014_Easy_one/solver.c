#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int mod_up(int p){
    int x = p;
    while(x < 0){
        x += 256;
    }
    return x;
}
void getKey(){
    FILE* input  = fopen("msg001", "rb");
    FILE* output = fopen("msg001.enc" , "rb");
    char k[100] = "";
    char c, p, t = 0;
	int i = 0;
    while ((p = fgetc(input)) != EOF) {
        c = fgetc(output);
        c -= (i * i + (int)p);
        c = c % 256;
        c ^= t;
        k[i] = c;
		t = p;
		i++;
	}
    printf("%s" , k);
    //key = VeryLongKeyYouWillNeverGuessVe
}
void getFlag(){
    char k[] = "VeryLongKeyYouWillNeverGuess";
    FILE* input = fopen("msg002.enc" , "rb");
    char c, t = 0;
	int i = 0;
    while ((c = fgetc(input)) != EOF) {
        
        int x = c;
        int p = 0 , flag = 0;
        x = mod_up(x);
        // printf("%d" , x);
        for(p = 0 ; p <= 255 ;p ++){
            if(x == ((p + (k[i % strlen(k)] ^ t) + i*i) & 0xff)){
                printf("%c" , p);
                t = p;
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            printf("%d" , i);
        }
		// t = p;
		i++;
    }
    printf("\n");
}
int main(){
    // getKey();
    // int k = 0 ;
    // for(k = 0; k <= 255 ; k++){
    //     char s[] = "VeryLongKeyYouWillNeverGuess";
    //     s[29] = k;
    //     getFlag(s);
    // }
    getFlag();
    return 0;
}