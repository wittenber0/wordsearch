#include <stdio.h>
#include <stdlib.h>

int d = 0xff;
int c = 0b11111101;

int main(){
	if(c & 0b00000010){
		printf("true\n");
	}else{
		printf("false\n");
	}
	
	return 1;
}
