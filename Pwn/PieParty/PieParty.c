#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void GetPie() {

	char type[60];
	char flavor[60];

	puts("We have many types of pie to choose from:");
	puts("-Double-crust fruit pie");
	puts("-Cream pie");
	puts("-Custard pie");
	puts("-Chiffon pie");
	puts("-Ice cream pie");

	puts("What do you choose? ");
	read(0,type,60);
	puts("Your choice: ");
	printf(type);

	puts("\nNow choose a flavor: ");
	puts("-Apple");
	puts("-Blueberry");
	puts("-Lemon");
	puts("-Banana");

    puts("What do you choose? ");
    read(0,flavor,60);
    puts("Your choice: ");
    printf(flavor);

	puts("\nBon appetit!");

}

void BakePie() {
	
	char pie[60];
	puts("Hello chef! What type of pie will you bake?");
	read(0,pie,150);
	puts("Okayy, do your magic!!");

}

int main() {

	int choice;

	setup();
	puts("\nWelcome to the party!!! Its nice to have you here, make a choice: \n");

	while (1) {
	    puts("\n1. Get some pie");
	    puts("2. Bake a pie");
	    puts("3. Go home\n");
		puts("Choice:");
		scanf("%d",&choice);
		switch (choice) {
			case 1:
				GetPie();
				break;
			case 2:
				BakePie();
				break;
			case 3:
				exit(0);
			default:
				puts("There's no fourth choice!\n");
		}
	}
}
