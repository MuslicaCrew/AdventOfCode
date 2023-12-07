#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define SIZE 1024

void printLine();

int main(int args, char **argv){
	/*Initializing variables*/
	FILE *file;
	char buffer[SIZE];
	int first;
	int last;
	int sum = 0;
	/*Opening file and if it cannot be opened return 1*/
	file = fopen(argv[1] ,"r");
	if (file == NULL){
		return 1;
	}
	/*Read the file line by line 1024 bytes at a time*/
	while (fgets(buffer, SIZE, file)!= NULL){
        first = 0;
        last = 0;
		/*If read the buffer (line) and if the character is a digit we make the digit the number*/
		for(int i = 0; i < strlen(buffer); i++){
			if(isdigit(buffer[i])){
				/*Subtracting '0' turn the char into an int*/
                if (first != 0){
					last = buffer[i] - '0';
                } else {
                    first = buffer[i] - '0';
                    last = buffer[i] - '0';
                }
		    }
	    }
        sum += (first * 10) + last;
    }
	printf("Sum: %d\n", sum);
	fclose(file);
	return 0;

}

void printLine(){
	printf(";---------------;\n");
}

