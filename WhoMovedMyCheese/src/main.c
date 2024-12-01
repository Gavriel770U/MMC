#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
HINT: This comment would usually make no difference, but apparently it does.
*/

void* dword1;
void* dword2;

void allocate() {
	dword1 = malloc(16);
	dword2 = malloc(4);
}

void release() {
	free(dword1);
	free(dword2);
}

void init() {
	*((int*)dword1 + 0) = 0x6e69616d;
	*((int*)dword1 + 1) = 0x0000632e;
	*((int*)dword2 + 0) = 0x00000072;
	srand(time(NULL));
}

int bitsum(const void* buffer, int length) {
	int s = 0;
	for (int i = 0; i < length; i++)
		for (int j = 0; j < 8; j++)
			s += (*((const char*)buffer + i) >> j) & 1;
	return s;
}

void decode(void* buffer, char key) {
	for (char* c = (char*)buffer; *c; c++)
		*c ^= key;
}

int check_password(const char* password);

void generate_result(const char* password, int success) {
	FILE* f = fopen("result.txt", "w");
	int response = rand();
	if (success) {
		fputs("Congratulations, you've completed the challenge.\n", f);
		fputs("Though, the real treasure was the friends you made along the way.\n", f);
		fputs("MMC{", f);
		fputs(password, f);
		fputs("}", f);
	}
	else if (response == 0) { // GLaDOS
		fputs("I honestly, truly didn't think you'd fall for that trap.\n", f);
		fputs("In fact, I designed a much more elaborate trap further ahead for when you got through with this easy one.\n", f);
		fputs("If I'd known you'd let yourself get captured this easily, I'd have dangled a turkey leg on a rope from the ceiling.", f);
	}
	else if (response == 1) {
		fputs("You are a failure.", f);
	}
	else if (response == 2) {
		fputs("Would you please stop trying? It hurts your pride.", f);
	}
	else if (response == 3) {
		fputs("How very dissapointing.", f);
	}
	else if (response == 4) { // Winnie The Pooh
		fputs("On Wednesday, when the sky is blue,\n", f);
		fputs("And I have nothing else to do,\n", f);
		fputs("I sometimes wonder if it's true\n", f);
		fputs("That who is what and what is who.\n", f);
	}
	else if (response == 5) { // Madara
		fputs("Weakness disgusts me.", f);
	}
	else {
		fputs("You got it right! ...just kidding.", f);
	}
	fclose(f);
}

int main() {
	FILE* f;
	long length;
	void* buffer;
	char password[256], decoded[256], key;
	int i, n, c;
	allocate();
	init();
	f = fopen((const char*)dword1, (const char*)dword2);
	fseek(f, 0, SEEK_END);
	length = ftell(f);
	fseek(f, 0, SEEK_SET);
	buffer = malloc(length);
	for (i = 0, n = 0, c = fgetc(f); c != EOF && n < 105; i++, c = fgetc(f), n += ((char)c == '\n'))
		*((char*)buffer + i) = (char)c;
	*((char*)buffer + i) = 0;
	fclose(f);
	key = bitsum(buffer, i) & 0xFF;
	printf("PASSWORD: ");
	scanf("%[^\n]%*c", password);
	strcpy(decoded, password);
	srand(*password);
	decode(decoded, key);
	generate_result(password, check_password(decoded));
	printf("A result file has been generated, perhaps you ought to take a look.\n");
	release();
	system("pause");
	return 0;
}

int check_password(const char* password) {
	return
		*((char*)password + 0) == -6 &&
		*((char*)password + 1) == -123 &&
		*((char*)password + 2) == -120 &&
		*((char*)password + 3) == -8 &&
		*((char*)password + 4) == -101 &&
		*((char*)password + 5) == -97 &&
		*((char*)password + 6) == -6 &&
		*((char*)password + 7) == -5 &&
		*((char*)password + 8) == -123;
}
