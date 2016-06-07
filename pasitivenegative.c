#include<stdio.h>
#include<conio.h>
void main()
{
int t;
clrscr();
scanf("%d",&t);
if(t>0)
printf("%d is positive",t);
else if(t==0)
printf("%d is zero",t);
else
printf("%d is negative",t);
getch();
}
