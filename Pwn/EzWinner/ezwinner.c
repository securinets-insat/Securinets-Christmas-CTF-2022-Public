#include<stdio.h>
#include<stdlib.h>

void setup(){
        setvbuf(stderr, NULL, _IONBF, 0);
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stdin, NULL, _IONBF, 0);
}

void win(){
	char c;
        FILE *fp=fopen("./flag.txt","r");
        if(fp){
                while( (c=getc(fp)) != EOF)
                        putchar(c);
                fclose(fp);
        }
}

int main(){

	setup();

	char buf[60];
	printf("Hello there, care for some easy pwn?\n");
	printf("Here is a gift, use it wisely: %p", &win);
	printf("\ninput: ");
	gets(buf);

	return 0;

}
