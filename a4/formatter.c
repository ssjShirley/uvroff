/*
 * UVic SENG 265, Summer 2018,  A#4
 *
 * This will contain the bulk of the work for the fourth assignment. It
 * provide similar functionality to the class written in Python for
 * assignment #3.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "formatter.h"

#define DEFAULT_BUFLEN 80
char **format_file(FILE *infile) {
	char line[DEFAULT_BUFLEN];
	int num_lines = 0;
	char **result = NULL;
	result = (char **)malloc(sizeof(char *) * 2);
	

	*result = calloc(1500, sizeof(char));
//	result[0] = (char *)malloc(sizeof(char)*2*1500);
	while (fgets(line, DEFAULT_BUFLEN, infile) != NULL){	
		result[num_lines] = (char *)malloc(sizeof(char) * DEFAULT_BUFLEN);
		if (result[num_lines] == NULL){
			return NULL;
		}
		strncpy(*(result+num_lines), line, DEFAULT_BUFLEN-1);
//		printf("%s",result[num_lines]);
		num_lines++;
	}
	return result;
}


char **format_lines(char **lines, int num_lines) {
	char **result = NULL;

#ifdef DEBUG
	result = (char **)malloc(sizeof(char *) * 2);
	if (result == NULL) {
		return NULL;
	}

	result[0] = (char *)malloc(sizeof(char) * DEFAULT_BUFLEN);
	if (result[0] == NULL) {
		return NULL;
	}
	strncpy(result[0], "(machine-like voice) STABLE GENIUS!", 
        DEFAULT_BUFLEN-1);

	result[1] = (char *)malloc(sizeof(char) * 2);
	if (result[1] == NULL) {
		return NULL;
	}
	result[1][0] = '\0';
#endif
	for(int i = 0; i < num_lines; i++){
		result[i] = (char *)malloc(sizeof(char) * DEFAULT_BUFLEN);
		if (result[i] == NULL) {
			return NULL;
		}
		strncpy(result[i], lines[i], DEFAULT_BUFLEN-1);
	}
	return result;
	free(result);
}



