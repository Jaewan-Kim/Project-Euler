#include <iostream>
#include <map>

using namespace std;

int isPrime(int x) {
	for (int i = 2; i <x; i++) {
		if (x%i == 0)
			return false;
	}
	return true;
}

int main() {
	int n = 2000000;
	int sum = 0;
	map<int,bool> m;
	m[2] = true;
	for (int x = 3; x <=n; x +=2) {
		m[x] = true;
		cout << x << endl;
	}

	for (map<int, bool>::iterator i = ++m.begin(); i !=m.end(); i++) {
		if (i->second&& isPrime(i->first)) {
			int y = i->first;
			while (y < n) {
				m[y] = false;
				y += i->first;
				cout << y << endl;
			}
			cout << i->first << endl;
			sum += i->first;
		}
		else {
			i->second = false;
		}
	}
	cout << sum << endl;
}
