#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

bool isPrime(int num) {
	if (std::find(primes.begin(), primes.end(), num) != primes.end()) {
		return true;
	}
	for(int i = 2; i < (num-1); i++){
		if(num%i == 0){
			return false;
		}
	}
	primes.push_back(num);
	return true;
}

vector<int> getPrimeFactorization(int num, vector<int> startVector) {
	vector<int> returnVector = startVector;

	for (int i = 0; i < primes.size(); i++) {
		if (num%primes[i]==0) {
			returnVector.push_back(primes[i]);
			num = num/primes[i];
			if (isPrime(num)) {
				returnVector.push_back(num);
				return returnVector;
			} else {
				getPrimeFactorization(num, returnVector);
			}
		}
	}

	for (int i = (num-1); i >= 2; i--) {
		if (num%i == 0) {
			returnVector.push_back(num/i);
			num = i;
			if (isPrime(num)) {
				returnVector.push_back(num);
				return returnVector;
			} else {
				getPrimeFactorization(num, returnVector);
			}
		}
	}
}

void printPrimeFactorization(vector<int> primeNumbers) {
	ofstream outFile;
 	outFile.open("primeFactor.res");
	vector< vector<int> > numPower;
	for(int i = 0; i < primeNumbers.size(); i++){
		bool needToCreateVector = true;
		for( int z = 0; z < numPower.size(); z++){
			if(primeNumbers[i] == numPower[z][0]) {
				numPower[z][1]++;
				needToCreateVector = false;
			}
		}
		if (needToCreateVector) {
			vector<int> tmpVector;
			tmpVector.push_back(primeNumbers[i]);
			tmpVector.push_back(1);
			numPower.push_back(tmpVector);
		}
	}

	for (int i = 0; i < numPower.size(); i++) {
		if (i != 0) {
			cout << "*";
			outFile << "*";
		}
		cout << numPower[i][0];
		outFile << numPower[i][0];
		if(numPower[i][1] != 1){
			cout << "^" << numPower[i][1];
			outFile << "^" << numPower[i][1];
		}
	}
	cout << "\n";
	outFile << "\n";
	outFile.close();
}

int main() {
	vector<int> dataVector;

	std::ifstream t("data.dat");
	std::string fileText((std::istreambuf_iterator<char>(t)),
	std::istreambuf_iterator<char>());

	stringstream ssin(fileText);

	while (ssin.good()) {
		string tmp;
		ssin >> tmp;
		dataVector.push_back(atoi(tmp.c_str()));
	}

	dataVector.erase(dataVector.end() - 1); // Fix bug where EOF == 0

	ofstream outFile;
	outFile.open("primefactor.res");


	for (int i = 0; i < dataVector.size(); i++) {
		if (isPrime(dataVector[i])) {
			//printf("The given number %i is prime\n", dataVector[i]);
		} else {
			//cout << "The prime factorization is " << dataVector[i] << " = ";
			vector<int> tmpVector;
			//printPrimeFactorization(getPrimeFactorization(dataVector[i], tmpVector));

			vector<int> t = getPrimeFactorization(dataVector[i], tmpVector);
			for (int z = 0; z < t.size(); z++) {
				if (z!=0) {
					outFile << "*";
				}
				outFile << t[z];
			}
			outFile << " = " << dataVector[i];
			outFile << "\n";

		}
	}
	outFile.close();
}