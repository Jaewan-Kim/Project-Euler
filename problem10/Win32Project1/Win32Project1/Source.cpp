#include <iostream>
#include <vector>

using namespace std;

bool primecheck(vector<int>& vec, int x) {
	for (int p : vec) {
		if (x % p == 0) {
			return false;
		}
	}
	return true;
}


int main() {
	vector<int> primes;
	primes.push_back(3);
	int sum = 5;
	for (int x = 3; x < 1999999; x += 2) {
		if (primecheck(primes,x)) {
			primes.push_back(x);
			sum += x;
			cout << x << endl;
		}
	}
	cout << sum << endl;
}