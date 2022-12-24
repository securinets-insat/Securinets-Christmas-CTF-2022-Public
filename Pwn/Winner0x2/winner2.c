#include<stdio.h>
#include<stdlib.h>

void setup(){
        setvbuf(stderr, NULL, _IONBF, 0);
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stdin, NULL, _IONBF, 0);
}

void win(int a, int b){
	char c;
	if (b == 0xf672ae02){
        	FILE *fp=fopen("./flag.txt","r");
        	if(fp){
                	while( (c=getc(fp)) != EOF)
                        	putchar(c);
                	fclose(fp);
        	}
	}
}

int main(){

	setup();

	char buf[100];
	puts("I'm sure you can solve this too!!");
	puts("give me your input: ");
	gets(buf);

	return 0;

}
