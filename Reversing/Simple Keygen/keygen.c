#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

// ##################
// Author => IronByte
// ##################

void welcome() {
    printf("    ##############################\n");
    printf("    ###### SIMPLE KEYGEN #########\n");
    printf("    ##############################\n");   
}

char* gen(char* username) {
    char* result = (char*)malloc(sizeof(char)*20);
    for(int i = 0; i < strlen(username); i++) {
        result[i] = (username[i] ^ 0x01) + i; 
    }
    result += '\x00'; 
    return result;
}

int main() {
    welcome();
    char username[20]; 
    char password[20]; 
    printf("\n      Username : "); 
    fgets(username, 20, stdin); 
    fflush(stdin);
    printf("\n      Password : "); 
    fgets(password, 20, stdin);
    if (strncmp(gen(username), password, 12) == 0)
        printf("\n Good Job you cracked it ! \n"); 
    else 
        printf("\n Nope, Keep trying ! \n");
    return 0;
}