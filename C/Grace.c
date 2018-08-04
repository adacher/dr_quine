#include <stdio.h>

#define A
#define B

#define FUNCTION int main(){char*a="#include <stdio.h>%1$c%1$c#define A%1$c#define B%1$c%1$c#define FUNCTION int main(){char*a=%2$c%s%2$c;FILE*f=fopen(%2$cGrace_kid.c%2$c,%2$cw+%2$c);/*je suis un commentaire*/fprintf(f, a, 10, 34, a);fclose(f);}%1$cFUNCTION";FILE*f=fopen("Grace_kid.c","w+");/*je suis un commentaire*/fprintf(f, a, 10, 34, a);fclose(f);}
FUNCTION