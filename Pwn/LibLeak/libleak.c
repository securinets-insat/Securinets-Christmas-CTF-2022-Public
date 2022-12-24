#include<stdio.h>
#include<stdlib.h>


void setup(){
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){

	setup();
	char buf[80];
	printf("Hum... Where is the win function?? Can you get the flag without a win function?\n");
	sleep(2);
	printf("How about I give you another gift ;) ?\n");
	sleep(2);
	printf("%p\n", &sleep);
	sleep(1);
	printf("Give me something useful: ");
	gets(buf);
	return 0;

}
