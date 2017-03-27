#include<stdio.h>
#include<stdlib.h>



int find_left_of_arr( int * arr, int length)
{
	int i;
	for ( i=1; i< length; i++)
	{
		if ( arr[i] <arr[i-1])
		{
			break;
	
		}
	}
	return i-1;
}

int find_right_of_arr( int * arr, int length)
{
	for ( int i=length-2;i>=0; i--)
	{
		if ( arr[i] > arr[i+1])
		{
			return i+1;
	
		}
	}
	return 0;	

}


int shrinkleft ( int * arr, int min, int findleft)
{

	int i;
	for (i = findleft; i>=0; i--)
	{
		if ( arr[i] <= arr[min])
		{
			break;
		}
		
	}
	
	return i+1;

}

int shrinkright ( int * arr, int max, int findright, int length)
{

	int i;
	for (i= findright; i< length; i++)
	{
		if ( arr[i] >= arr[max] )
		{
			break;
		}
		
	}
	return i-1;
		
}

int findsequence( int * arr, int length)
{


	int findleft;
	findleft = find_left_of_arr(arr,length);

	if ( findleft >= length-1 )
	{
		return 0;
	}

	int findright;
	findright = find_right_of_arr(arr,length);
	
	int min,max;
	
	min = findright;
	max = findleft;

	for ( int i = findleft +1; i< findright; i++)
	{
		if ( arr[i] < arr[min])
		{
			min = i;
		}
		if ( arr[i] > arr[max])
		{
			max = i;
		}
	}



	int finalleftindex;
	int finalrightindex;

	finalleftindex = shrinkleft(arr,min,findleft);
	finalrightindex= shrinkright(arr,max,findright,length);
	int max2 = arr[finalleftindex]>arr[max]?finalleftindex:max;
	int min2 = arr[finalrightindex]<arr[min]?finalrightindex:min;

	while(min2!=min || max2!=max){
		min2 = min;max2=max;
		finalleftindex = shrinkleft(arr,min,findleft);
		finalrightindex= shrinkright(arr,max,findright,length);
		max2 = arr[finalleftindex]>arr[max]?finalleftindex:max;
		min2 = arr[finalrightindex]<arr[min]?finalrightindex:min;
		
	}
	return (finalrightindex - finalleftindex);

}






int main()
{
		int ret;
		int array[8] = {1,2,6,11,6,5,18,19};

		int length = (sizeof(array)/sizeof(array[0]));
		ret = findsequence(array,length);
		printf("%d",ret);

		return 0 ;
}
	


