#include<stdio.h>

void function(){}

/*
	1
*/

int main()
{
	/*
		2
	*/
	char*s="#include<stdio.h>%1$c%1$cvoid function(){}%1$c%1$c/*%1$c%2$c1%1$c*/%1$c%1$cint main()%1$c{%1$c%2$c/*%1$c%2$c%2$c2%1$c%2$c*/%1$c%2$cchar*s=%3$c%s%3$c;%1$c%2$cfunction();%1$c%2$cprintf(s, 10, 9, 34, s);%1$c}";
	function();
	printf(s, 10, 9, 34, s);
}