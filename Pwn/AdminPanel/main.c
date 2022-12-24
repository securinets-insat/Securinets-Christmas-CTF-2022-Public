#include <stdio.h>

struct user{
    char username[25];
    char password[25];
    int isAdmin;
    int loggedIn;
};

int menu(){
    puts("1. Login.");
    puts("2. Change username.");
    puts("3. Access flag panel.");
    puts("4. Logout.");

    int tmp;
    printf("> ");
    scanf("%d", &tmp);
    fflush(stdin);
    return tmp;
}

void flagPanel(){
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

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){
    setup();
    
    struct user activeUser;
    activeUser.loggedIn = 0;
    activeUser.isAdmin = 0;

    int choice;
    do{
        choice = menu();
        switch (choice)
        {
            case 1:{
                printf("Username: ");
                scanf("%25s", activeUser.username);

                printf("Password: ");
                scanf("%25s", activeUser.password);

                activeUser.loggedIn = 1;
                break;
            }
            case 2:{
                if(activeUser.loggedIn != 1){
                    puts("You have to login!");
                    break;
                }

                printf("New username: ");
                read(0, activeUser.username, 70);
                break;
            }
            case 3:{
                if(activeUser.loggedIn != 1){
                    puts("You have to login!");
                    break;
                }
                if(activeUser.isAdmin != 1){
                    puts("Only admin can access the flag!");
                    break;
                }

                flagPanel();
                break;
            }
            default:
                break;
        }
    }while(choice != 4);
}