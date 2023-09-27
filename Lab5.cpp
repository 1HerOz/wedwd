#include <iostream>
using namespace std;

int main() {

// QUESTION 1 

	int a, b;
	char op;
	
	cout << "Enter first number: " << endl;
	cin >> a;
	
	cout << "Enter second number: " << endl;
	cin >> b;
	
	cout << "Enter operation (+, -, *, /): " << endl;
	cin >> op;
	
	switch(op) {
		
		case '+':
			cout << "The sum of a, b: " << a + b;
			break;
		case '-':
			cout << "The minus of a, b: " << a - b;
			break;
		case '*':
			cout << "The multi of a, b: " << a * b;
			break;
		case '/':
			if (b == 0) {
				cout << "The division by 0, ERROR!" << endl;
			}
			else
				cout << "The division of a, b: " << a / b;
				break;
		default:
			cout << "Enter a wrong operation";
	}

// ---------------------------------------------------------------

// QUESTION 2

	int months;
	
	cout << "Enter a month number" << endl;
	cin >> months;
	
	switch(months) {
		
		case 1:
		case 3:
		case 4:
		case 5:
		case 6:
		case 7:
		case 8:
		case 9:
		case 10:
		case 11:
		case 12:
			cout << "31 days" << endl;
			break;
		case 2:
			cout << "28/29 days" << endl;
			break;
		default:
			cout << "There is not month more than 12, ERROR!" << endl;
	}
	
// ---------------------------------------------------------------------------

// QUESTION 3

	int ID, age, seats;
	char classes;
	
	cout << "Enter your ID: " << endl;
	cin >> ID;
	
	cout << "Enter your age" << endl;
	cin >> age;
	
	if (age >= 18) {
		
		cout << "Choose a class (A, B, C): ";
		cin >> classes;
		
		switch(classes) {
			
			case 'A':
				cout << "The price is 100$" << endl;
				cout << "How many seats you want" << endl;
				cin >> seats;
				cout << seats * 100 << '$' << endl;
				break;
			case 'B':
				cout << "The price is 750$" << endl;
				cout << "How many seats you want" << endl;
				cin >> seats;
				cout << seats * 75 << '$' << endl;
				break;
			case 'C':
				cout << "The price is 50$" << endl;
				cout << "How many seats you want" << endl;
				cin >> seats;
				cout << seats * 50 << '$' << endl;
				break;
			default:
				cout << "You didnt choose correctly A, B, C";	
		}	
	}
	
	else {
		cout << "Sorry" << endl;
	}
	
// ---------------------------------------------------------

// QUESTION 4

	int num;
	cout << "Enter a number: " << endl;
	cin >> num;
	
	switch(num%2) {
		
		case 0:
			cout << "Even!";
			break;
		default:
			cout << "Odd";
			break;	
	}

// ----------------------------------------------------------

// QUESTION 5

	int memberShip;
	double reward;
	double monPur;
	
	cout << "Enter a membership type \n";
	cout << "1. Standard \n";
	cout << "2. Plus \n";
	cout << "3. Premium \n";
	cin >> memberShip;
	
	cout << "Enter the monthly purchased" << endl;
	cin >> monPur;
	
	switch(memberShip) {
		
		case 1:
			if (monPur < 75) {
				// 5% of the total monthly purchase
				reward = 0.05 * monPur;
			}
			else if (monPur >= 75 && monPur <= 149.99) {
				// 7.5% of the total monthly purchase
				reward = 0.075 * monPur;
			}
			else {
				// 10% of the total monthly purchase
				reward = 0.1 * monPur;
			}
			cout << "Reward points: " << reward << endl;
			break;
		case 2:
			if (monPur < 150) {
				// 6% of the total monthly purchase
				reward = 0.06 * monPur;
			}
			else {
				// 13% of the total monthly purchase
				reward = 0.13 * monPur;
			}
			cout << "Reward points: " << reward << endl;
			break;
		case 3:
			if (monPur < 200) {
				// 4% of the total monthly purchase
				reward = 0.04 * monPur;
			}
			else {
				// 15% of the total monthly purchase
				reward = 0.15 * monPur;
			}
			cout << "Reward points: " << reward << endl;
			break;
		default:
			cout << "Error, you did not enter a membership type" << endl;
		
	}
}
