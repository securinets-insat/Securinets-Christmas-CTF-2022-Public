#include <stdio.h> 
#include <string.h> 

// ##################
// Author => IronByte
// ##################

void welcome() {
    printf("    ##############################\n");
    printf("    ######## SIMPLE CHECK ########\n");
    printf("    ##############################\n");   
    printf("\n flag : ");
}


int main() {
    char flag[29];
    welcome();
    scanf("%29s", flag);
    if (strncmp("Securinets{51mp13_ch3ck_n3x7}", flag, 29) == 0)
        printf("\n Good Job You can Validate with that flag ! \n"); 
    else 
        printf("\n Nope, keep trying ! \n");
    return 0;
}