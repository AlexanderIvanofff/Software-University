#include <iostream>

using namespace std;


int main() {
	string projectName;
	int countProject;

	cin >> projectName;
	cin >> countProject;


	int countProjecrtPerDay = countProject * 3;

	cout << "The architect " << projectName << " will need " << countProjecrtPerDay << " hours to complete " << countProject << " project / s.";
	return 0;

}
