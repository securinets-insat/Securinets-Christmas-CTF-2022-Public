#include <stdio.h>

void correct(){
	char c;
    FILE *fp=fopen("./flag.txt","r");
    if(fp){
        while( (c=getc(fp)) != EOF)
            putchar(c);
        fclose(fp);
    }
    else{
        puts("Flag file not found!");
    }
}

int check(int x){
    return x == 0;
}

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void main(){
    setup();

    puts("How about a riddle?");
    puts("What can be not a 0 & a 0 at the same time?");

    unsigned long x = 0;
    do{
        puts("Give a non zero positive number:");
        scanf("%lu", &x);
    } while(x <= 0);

    if(check(x)){
        correct();
    } else{
        puts("Wrong answer!");
    }
}