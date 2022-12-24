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

	char buf[120];
	printf("No gifts for you this time, but.. still easy\n");
	printf("input: ");
	gets(buf);

	return 0;

}
