#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string> 

using namespace std;

int main() {
    int money;
    cout << "Enter your money: ";
    cin >> money;

    cout << "Your money " << money << "$" << endl;

    while (money > 0) {
        int bet;
        cout << "Enter your bet: ";
        cin >> bet;

        string card[] = { "HEARTS", "DIAMONDS", "CLUBS", "SPADES" };
        string number[] = { "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" };

        string youCard = card[rand() % 4];
        string youNumber = number[rand() % 13];

        string dealerCard = card[rand() % 4];
        string dealerNumber = number[rand() % 13];

        int yourTotal = 0;
        int dealerTotal = 0;

        if (youNumber == "A") {
            if (yourTotal <= 11) {
                yourTotal += 11;
            }
            else {
                yourTotal += 1;
            }
        }
        else if (youNumber == "K" || youNumber == "Q" || youNumber == "J" || youNumber == "10") {
            yourTotal += 10;
        }
        else {
            yourTotal += stoi(youNumber);
        }

        if (dealerNumber == "A") {
            if (dealerTotal <= 11) {
                dealerTotal += 11;
            }
            else {
                dealerTotal += 1;
            }
        }
        else if (dealerNumber == "K" || dealerNumber == "Q" || dealerNumber == "J" || dealerNumber == "10") {
            dealerTotal += 10;
        }
        else {
            dealerTotal += stoi(dealerNumber);
        }

        cout << "Your hand " << youCard << " " << youNumber << ", Total: " << yourTotal << endl;
        cout << "Dealer hand " << dealerCard << " " << dealerNumber << ", Total: " << dealerTotal << endl;

        while (yourTotal < 21 && dealerTotal < 17) {
            int select;
            cout << "1: HIT or 2: STAY\n:";
            cin >> select;

            if (select == 1) {
                youCard = card[rand() % 4];
                youNumber = number[rand() % 13];

                if (youNumber == "A") {
                    if (yourTotal <= 11) {
                        yourTotal += 11;
                    }
                    else {
                        yourTotal += 1;
                    }
                }
                else if (youNumber == "K" || youNumber == "Q" || youNumber == "J" || youNumber == "10") {
                    yourTotal += 10;
                }
                else {
                    yourTotal += stoi(youNumber);
                }
            }
            else if (select == 2) {
                while (dealerTotal < 17) {
                    dealerCard = card[rand() % 4];
                    dealerNumber = number[rand() % 13];

                    if (dealerNumber == "A") {
                        if (dealerTotal <= 11) {
                            dealerTotal += 11;
                        }
                        else {
                            dealerTotal += 1;
                        }
                    }
                    else if (dealerNumber == "K" || dealerNumber == "Q" || dealerNumber == "J" || dealerNumber == "10") {
                        dealerTotal += 10;
                    }
                    else {
                        dealerTotal += stoi(dealerNumber);
                    }
                }
            }
            cout << "Your hand " << youCard << " " << youNumber << " Your total " << yourTotal << endl;
        }

        cout << "Your total " << yourTotal << ", Dealer total " << dealerTotal << endl;

        if (yourTotal <= 21 && dealerTotal <= 21) {
            if (dealerTotal == 21) {
                cout << "Blackjack! Dealer win!" << endl;
                money -= bet;
            }
            else if (yourTotal == 21) {
                cout << "Blackjack! You win!" << endl;
                money += bet;
            }
            else if (yourTotal > dealerTotal) {
                cout << "Dealer lost! You win!" << endl;
                money += bet;
            }
            else if (yourTotal < dealerTotal) {
                cout << "You lost! Dealer win!" << endl;
                money -= bet;
            }
        }
        else if (yourTotal > 21) {
            cout << "You bust! Dealer win!" << endl;
            money -= bet;
        }
        else if (dealerTotal > 21) {
            cout << "Dealer bust! You win!" << endl;
            money += bet;
        }

        cout << "Your money " << money << "$" << endl;

        if (money > 0) {
            int select_coe;
            cout << "1.Continue or 2.End: ";
            cin >> select_coe;
            if (select_coe == 1) {
                continue;
            }
            else if (select_coe == 2) {
                cout << "Your last money is " << money << "$" << endl;
                break;
            }
        }
        else {
            break;
        }
    }

    if (money <= 0) {
        cout << "You sank!" << endl;
    }

    return 0;
}
