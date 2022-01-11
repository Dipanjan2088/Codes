#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define max 10
void selection(int *,int);
void insertion(int *,int);
void di(int *,int ,int ,int );
void merge_sort(int *,int ,int );
int partition(int *,int ,int );
void quick_sort(int *,int ,int );
int main()
{
	int i,arr[max],n,choice;
	printf("\n1.Choice-1 Sorting array using Selection sort.");
	printf("\n2.Choice-2 Sorting array using Insertion sort.");
	printf("\n3.Choice-3 Sorting array using Merge sort.");
	printf("\n4.Choice-4 Sorting array using Quick sort.");
	printf("\n5.Choice-5 Exit.");
	while(1)
	{
		printf("\n Enter the number of the array:");
		scanf("%d",&n);
    	printf("\n Enter the elements:\n");
		for(i=0;i<=n-1;i++)
			scanf("%d",&arr[i]);
		printf("\n Before calling displaying the array:");
		for(i=0;i<=n-1;i++)
			printf("\t %d",arr[i]);
		printf("\n Enter your choice: ");
	    scanf("%d",&choice);
	    switch(choice)
	    {
	    	case 1:
	    	    selection(&arr[0],n);
	    	    printf("\n After sorting the array using selection sort is:");
                for(i=0;i<=n-1;i++)
                	printf("\t %d",arr[i]);
	    		break;
	    	case 2:
	    		insertion(&arr[0],n);
	    		printf("\n After sorting the array using insertion sort is:");
                for(i=0;i<=n-1;i++)
                	printf("\t %d",arr[i]); 
	    		break;
	    	case 3:
	    		merge_sort(&arr[0],0,n-1);
	    		printf("\n After sorting the array using merge sort is:");
                for(i=0;i<=n-1;i++)
                	printf("\t %d",arr[i]);
	    		break;
	    	case 4:
	    		quick_sort(&arr[0],0,n-1);
	    		printf("\n After sorting the array using quick sort is:");
                for(i=0;i<=n-1;i++)
                	printf("\t %d",arr[i]);
	    		break;
	    	case 5:
	    		exit(1);
		}
	}
	return 0;
}
void selection(int *sel,int nn)
{
	int i,j,k,min,temp=0;
	for(i=0;i<nn-1;i++)
	{
		min=*(sel+i);
		k=i;
		for(j=i+1;j<=nn-1;j++)
		{
			if(min>*(sel+j))
			{
				min=*(sel+j);
				k=j;
			}
			if(i!=k)
			{
				temp=*(sel+i);
				*(sel+i)=*(sel+k);
				*(sel+k)=temp;
			}
		}
	}
}
void insertion(int *ins,int nn)
{
	int i,j,temp=0;
	for(i=1;i<=nn-1;i++)
	{
		temp=*(ins+i);
		j=i-1;
		while(j>=0 && *(ins+j)>temp)
		{
			*(ins+(j+1))=*(ins+j);
			j=j-1;
		}
		*(ins+(j+1))=temp;
	}
}
void merge_sort(int *mer,int low,int high)
{
	int mid;
	if(low<high)
	{
		mid=((low+high)/2);
		merge_sort(mer,low,mid);
		merge_sort(mer,mid+1,high);
		di(mer,low,mid,high);
	}
}
void di(int *k,int low,int mid,int high)
{
	int i,j,r,m[max];
	i=low;
	j=mid+1;
	r=low;
	while(i<=mid && j<=high)
    {
      	if(*(k+i)<*(k+j))
      	{
        	*(m+r)=*(k+i);
        	r=r+1;
        	i=i+1;
      	}
      	else
      	{
       	 	*(m+r)=*(k+j);
        	r=r+1;
        	j=j+1;
      	}
    }  
    while(i<=mid)
    {
        *(m+r)=*(k+i);
        r=r+1;
        i=i+1;
    }
    while(j<=high)
    {
	    *(m+r)=*(k+j);
	    r=r+1;
	    j=j+1;
    }
    for(r=low;r<=high;r++)
    {
        *(k+r)=*(m+r);
    }      
}
void quick_sort(int *qui,int p,int r)
{
	int q;
	if(p<r)
	{
		q=partition(qui,p,r);
		quick_sort(qui,p,q-1);
		quick_sort(qui,q+1,r);
	}
} 
int partition(int *qui,int p,int r)
{
	int i,j,k,x,temp=0;
	x=*(qui+p);
    i=p;
    j=r;
    while(i<j)
	{
	    while(*(qui+i)<=x)
	        i=i+1;
        while(*(qui+j)>x)
            j=j-1;
        if(i<j)
        {
            temp=*(qui+i);
            *(qui+i)=*(qui+j);
            *(qui+j)=temp;
        }
	}
    *(qui+p)=*(qui+j);
    *(qui+j)=x; 
    return j;
}
