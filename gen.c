#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_WORD_LENGTH 64
#define MAX_WORDS 128


int wordIndex;
char words[MAX_WORDS][MAX_WORD_LENGTH];

void loadWords(){
	FILE* f = fopen("words.txt", "r");
	char* buf =  malloc(MAX_WORD_LENGTH);
	wordIndex = 0;
	while (fgets(buf, MAX_WORD_LENGTH, f) != NULL){
		char* w = strtok(buf, "\n");
		printf("%i: %s at %p\n", wordIndex, w, &words[wordIndex]);
		strcpy(words[wordIndex], w);
		wordIndex++;
	}

}

int freeWords(){
	//free board
	for(int i =0; i < wordIndex; i++){
		free(words[i]);
	}
	free(words);
	return 1;
}

int printBoard(char** b, int n){
	printf("\n|");
	for(int i=0; i<n; i++){
		printf(" -");
	}
	printf(" |\n");

	for(int i=0; i<n; i++){
		printf("|");
		for(int j=0; j<n; j++){
			printf(" %c",b[i][j]);
		}
		printf(" |\n");
	}

	printf("|");
	for(int i=0; i<n; i++){
		printf(" -");
	}
	printf(" |\n\n");
	return 1;
}

char** loadBoard(int n){
	char** b = malloc(n*sizeof(char*));
	for(int i=0; i<n; i++){
		b[i] = malloc(n);
		for(int j=0;j<n; j++){
			b[i][j] = '0';
		}
	}
	return b;
}

int strcompare (const void * a, const void * b) {
    size_t fa = strlen((const char *)a);
    size_t fb = strlen((const char *)b);
    return (fa < fb) - (fa > fb);
}

int getValidPuts(char* w, char** b, int r, int c, int n){

	/*
	*	left to right 				00000001
	*	right to left 				00000010
	*	top to bottom 				00000100
	*	bottom to top 				00001000
	*	top-left to bottom-right 	00010000
	*	top-right to bottom-left 	00100000
	*	bottom-left to top-right	01000000
	*	bottom-right to top-left	10000000
	*/

	int v = 0b11111111;
	int len = (int) strlen(w);

	//if first character isnt possible, invalid
	if(b[r][c] != '0' && b[r][c] != w[0]){
		return 0;
	}
	//l-r space
	if(c + len > n){
		v -= 0b00000001;
	}
	//r-l space
	if(c - len < 0){
		v -= 0b00000010;
	}
	//t-b space
	if(r + len > n){
		v -= 0b00000100;
	}
	//b-t space
	if(r - len < 0){
		v -= 0b00001000;
	}
	//tl-br space
	if(c + len > n || r + len > n){
		v -= 0b00010000;
	}
	//tr-bl space
	if(c - len < 0 || r + len > n){
		v -= 0b00100000;
	}
	//bl-tr space
	if(r - len < 0 || c + len > n){
		v -= 0b01000000;
	}
	//br-tr space
	if(r - len < 0 || c - len < 0){
		v -= 0b10000000;
	}

	//if first letter is valid and there is space, check remaining letters in each direction
	for(int i=1; i< len; i++){

		//00000001
		if(v & 0b00000001 && b[r][c+i] != '0' && b[r][c+i] != w[i]){
			v -= 0b00000001;
		}
		//00000010
		if(v & 0b00000010 && b[r][c-i] != '0' && b[r][c-i] != w[i]){
			v -= 0b00000010;
		}
		//00000100
		if(v & 0b00000100 && b[r+i][c] != '0' && b[r+i][c] != w[i]){
			v -= 0b00000100;
		}
		//00001000
		if(v & 0b00001000 && b[r-i][c] != '0' && b[r-i][c] != w[i]){
			v -= 0b00001000;
		}
		//00010000
		if(v & 0b00010000 && b[r+i][c+i] != '0' && b[r+i][c+i] != w[i]){
			v -= 0b00010000;
		}
		//00100000
		if(v & 0b00100000 && b[r+i][c-i] != '0' && b[r+i][c-i] != w[i]){
			v -= 0b00100000;
		}
		//01000000
		if(v & 0b01000000 && b[r-i][c+i] != '0' && b[r-i][c+i] != w[i]){
			v -= 0b01000000;
		}
		//10000000
		if(v & 0b10000000 && b[r-i][c-i] != '0' && b[r-i][c-i] != w[i]){
			v -= 0b10000000;
		}
		if(v == 0){
			return 0;
		}
	}

	return v;
}

int placeWord(int l, int r, char** b, int n){

	

	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if(b[i][j] == '0'){

			}
		}
	}

	return 1;
}

int putWord(char** b){

	return 1;
}

int main(){
	clock_t start, end;
	double cpu_time_used;

	char wordlist[MAX_WORDS][MAX_WORD_LENGTH];
	loadWords();
	qsort(words, wordIndex, MAX_WORD_LENGTH, strcompare);

	int n = 5;

	char** board = loadBoard(n);

	int v = getValidPuts(words[2], board, 3, 3, n);
	int v2 = getValidPuts(words[0], board, 0, 0, n);
	printf("%s @ (%i, %i): %i\n", words[2], 0, 0, v);
	printf("%s @ (%i, %i): %i\n", words[0], 0, 0, v2);
	/*
	start = clock();
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("time: %f\n", cpu_time_used);
	*/

	
	printBoard(board, n);
	//freeBoard(board);
	//freeWords();
	
	return 1;
}