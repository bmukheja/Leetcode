#include <unordered_map>
/*
 * Complete the function below.
 */
string findFirstRepeatingChar(string infix) {
	// your code goes here
	typedef std::unordered_map< char, int> hashmap;
	hashmap counts;
	cin>>infix;
	for(unsigned int i = 0; i<infix.length(); i++) {
    	hashmap::const_iterator got = counts.find(infix[i]);
    	if(got==counts.end())
    		counts[infix[i]]=0;
    	counts[infix[i]]++;
    	}
	for(unsigned int i = 0; i<infix.length(); i++) {
		if(counts[infix[i]]>1){return string(1,infix[i]);}
	}
     return NULL;
}

