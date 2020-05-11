#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFLEN 1000


void LWcmd(FILE *data_fp, int width);
void nochange(FILE *data_fp, int width);

int main (int argc, char *argv[]){
	char* com;
	char* word;
	char buffer[BUFLEN];

	if (argc < 2) {
		fprintf(stderr, "You must provide a filename\n");
		exit(1);
	}

	FILE *data_fp = fopen(argv[1], "r");

	if (data_fp == NULL){
		fprintf(stderr, "unable to open %s\n", argv[1]);
		exit(1);
	}

	
	int width = 0;
	
	while((word = fgets(buffer, sizeof(char) * BUFLEN, data_fp))){
		com = strtok(word, " \n	");
		while (com != NULL){
		
			if(strcmp(com, ".LW") == 0){	
				width = atoi(com + 4);
				LWcmd(data_fp, width);
				break;
			} else {
				printf("%s\n",buffer);
				nochange(data_fp, width);
				break;
			}
			com = strtok(NULL," \n	");
		}
	}	
	fclose(data_fp);
	return 0;
	
}	
void LWcmd(FILE *data_fp, int width){ 
	char b[BUFLEN];
	char *word;
	int num_ch_line = 0;
	char *w;
	int linespace = 0;
	int left = 0;
	while ((w = fgets(b, sizeof(char) * BUFLEN, data_fp))){
		
		if (strcmp(w, "\n") == 0){
			for(int i = linespace ; i> 0 ; i--){ printf("\n"); }
			printf("\n\n");
			for(int i = linespace ; i> 0 ; i--){ printf("\n"); }
			for(int k = left; k > 0 ;k--){
				printf(" ");
			}
			
			num_ch_line = 0;
			continue;
		}

		word = strtok(b, " \n	");
		while (word != NULL){
			if(strcmp(w, ".FT") == 0 && strcmp(w+4, "off")){
				nochange(data_fp, width);
				return;
			}		
			if (strcmp(word, ".LM") == 0){		
				left = atoi(word + 4);
				for (int k = left; k>0; k--){
					printf(" ");
				}
				break;
			}
			if (strcmp(word, ".LS") == 0){
				linespace = atoi(word + 4);
				break;
			}
			
			num_ch_line = 1 + num_ch_line + strlen(word);

			if (num_ch_line - 1 > width - left){
			
				for (int i = linespace; i >= 0; i--){
					printf("\n");
				}
				
				for (int j = left; j > 0; j--){
					printf(" ");
				}

				num_ch_line = 1 + strlen(word);
			}
			if ((num_ch_line - 1) > strlen(word)){
				printf(" ");
			}
			printf("%s", word);
			word = strtok(NULL, " \n	");
		}
	}
	printf("\n");		

}

void nochange(FILE *data_fp, int width){
	char bu[BUFLEN];

	while (fgets(bu, sizeof(char) * BUFLEN, data_fp)){ 
		if (strcmp(bu, ".FT on") == 0){
			LWcmd(data_fp,width);
			break;
		}
		printf("%s", bu);
	}

}





