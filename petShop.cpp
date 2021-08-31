#include <iostream>

using namespace std;

int main() {
	double priceForDogs = 2.50;
	double proceForOther = 4.00;

	int dogs, otherAnimal;

	cin >> dogs >> otherAnimal;

	double totalPrice = dogs * priceForDogs + otherAnimal * proceForOther;

	cout.setf(ios::fixed);
	cout.precision(2);
	cout << totalPrice << " lv." << endl;

	return 0;
}