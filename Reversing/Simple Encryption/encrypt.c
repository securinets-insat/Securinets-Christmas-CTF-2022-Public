#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

// ##################
// Author => IronByte
// ##################

void welcome() {
    printf("    ##############################\n");
    printf("    ###### SIMPLE ENCRYPTION #####\n");
    printf("    ##############################\n");   
    printf("\n  flag : ");
}

const char key[] = "\x23\x60\xdc\xab";
const char enc_flag[] = "\x70\x5\xbf\xde\x51\x9\xb2\xce\x57\x13\xa7\x9e\x12\xd\xac\x9a\x10\x3f\xe8\x9e\x7c\x54\xed\xdc\x17\x19\xe9\xc5\x10\x18\xeb\xd6";

int checker(const char * input) {
    for(int i = 0; i < sizeof(enc_flag) - 1; i++) {
        char byte = key[i % (sizeof(key)-1)] ^ input[i];
        if (byte != enc_flag[i] && (int)(input[i]) != 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char flag[32];
    welcome();
    fgets(flag, 32, stdin);
    if (checker(flag))
        printf("\n  Good Job You can Validate with that flag ! \n"); 
    else 
        printf("\n  Nope, Keep Trying ! \n"); 
    
    return 0;
}