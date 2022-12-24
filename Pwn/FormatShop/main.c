#include <stdio.h>

unsigned int money = 1500;

int menu(){
    puts("1. Go shopping!");
    puts("2. Give feedback.");
    puts("3. Bye");

    int tmp;
    printf("> ");
    scanf("%d", &tmp);
    getchar();
    return tmp;
}

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void flag(){
	char c;
    FILE *fp=fopen("./flag.txt","r");
    if(fp){
        while( (c=getc(fp)) != EOF)
            putchar(c);
        fclose(fp);
    }else{
        puts("Flag file not found!");
    }
}

void shop(){
    unsigned int prices[5] = {69, 12, 322, 554, 0x1337};
    char* items[5] = {"Ice", "Fish", "Icecream", "Sugar", "flag"};

    for(int i=0; i<5; i++){
        printf("%d. %s:%d coins.\n", i+1, items[i], prices[i]);
    }

    printf("You have %u coins\n", money);
    int idx;
    printf("Item> ");
    scanf("%d", &idx);
    getchar();

    if(idx < 1 || idx > 5){
        puts("Invalid index.");
        return;
    }

    idx--; // To use as index
    if(prices[idx] > money){
        puts("Not enough money");
        return;
    }

    if(idx == 4){
        flag();
    }
    money -= prices[idx];
    puts("Item bought!");
}

void feedback(){
    char feedbackContent[250];
    printf("> ");
    int c = read(0, feedbackContent, 249);

    if(c == -1) return;
    feedbackContent[c] = '\0';
    
    printf(feedbackContent);
    puts("Thanks for the feedback!");
}

int main(){
    setup();

    int choice;
    do{
        choice = menu();
        switch (choice)
        {
        case 1:
            shop();
            break;
        case 2:
            feedback();
            break;
        default:
            break;
        }
    }while(choice != 3);

    return 0;
}