#include<iostream>
#include<map>
#include<unordered_map>
#include<string>
#include<stdlib>
#include<utility>
using namespace std;


typedef struct tradeentry
{
	string traderName;
	bool isBuy;
	float currentPrice;
}tradeentry;


vector<string> findFraudolentTraders(vector<string> datafeed){

	map<int,string> flagged_trades;
	unordered_map<int, vector<tradeentry>> trades;
	float currentPrice = 0;

	vector<string>::iterator feed_itr;
	vector<string>::iterator trade_itr;	
	vector<string> vals;
	int i;
	for ( feed_itr = datafeed.begin(); feed_itr != datafeed.end(); feed_itr++)
	{
		i = 0;
		vals[i] = strtok(*feed_itr,"|");

		while ( vals[i++] != NULL )
		{
			vals[i] = strtok(NULL,"|");	
		}


		int day = atoi(vals[0]);
		if ( i == 2 )
		{
			currentPrice = atoi(vals[1]);
			for(int x=day-3;x<day;x++){
				if (trades.find(x)!=trades.end()){
					for(trade_itr = trades[x].begin(); trade_itr!=trades.end();trade_itr++){
						if(flagged_trades.find())
					}
				}
			}
		}

	}




}