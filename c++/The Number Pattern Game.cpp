/*This program is a game where you must guess the next number in the sequence.
Author: Lauren White
Assignment: Final Project, EET 122
*/
#include <iostream>
#include <cmath>
using namespace std;

//Declare round functions
void win_state (bool round);
bool round_1(int random_num);
bool round_2 (int random_num);
bool round_3(int random_num);
bool round_4 (int random_num);
bool round_5(int random_num);

int main() {
    char user_answer;
    srand(time(0));
    int random_number = rand() % 8 + 2; // Gets number from 2 to 9
    //Asks user to start the game.
    cout<<"Welcome to The Number Pattern Game. Are you ready to begin? (y/n) ";
    cin>>user_answer;
    //Determines if the user starts
    if (tolower(user_answer) == 'y'){
        // Round 1
        bool level_1 = round_1(random_number);
        win_state(level_1);
        // Round 2
        bool level_2 = round_2(random_number);
        win_state(level_2);
        //Round 3
        bool level_3 = round_3(random_number);
        win_state(level_3);
        //Round 4
        bool level_4 = round_4(random_number);
        win_state(level_4);
        // Round 5
        bool level_5 = round_5(random_number);
        if (level_5 == true){
            cout<<"Congratulations! You won!";
        } else {
            cout<<"Incorrect. Game Over.";
        }

    } else if (user_answer == 'n'){
        cout<<"Goodbye.";
    } else {
        cout<<"Invalid input. Program terminated.";
    }
    
    return 0;
}

// Determines if the user has won or lost
void win_state(bool round){
if (round == true) {
            cout<<"Correct! New round starting..."<<endl;
        } else {
            cout<<"Incorrect. Game over.";
            exit(0);
        }
}

// Round 1 Function
bool round_1(int random_num) {
    int user_answer_1;
    // Instructions and welcome message
     cout<< "Welcome to round 1. Figure out the next number in the sequence: "<<endl;
        cout<<random_num<<" ";
        int question_1 = random_num;
        // Adds the first number to the current number in the sequence
        for (int i = 0; i < 3; i++) {
            question_1 = question_1+random_num;
            cout<<question_1<<" ";
        }
        cout<<endl<<"Answer: ";
        cin>>user_answer_1;
        if (user_answer_1 == question_1+random_num) {
            return true;
        } else {
            return false;
        }

}

//Round 2
bool round_2(int random_num){
    int user_answer_2;
    // Instructions and welcome message
     cout<< "Welcome to round 2. Figure out the next number in the sequence: "<<endl;
        cout<<random_num<<" ";
        int question_2= random_num;
        // Adds random_num to the next number in the sequence and then increases it by 1
        for (int i = 0; i < 3; i++) {
            random_num++;
            question_2 = question_2+random_num;
            cout<<question_2<<" ";
        }
        random_num++;
        cout<<endl<<"Answer: ";
        cin>>user_answer_2;
        // Checks if the user is correct
        if (user_answer_2 == question_2+random_num) {
            return true;
        } else {
            return false;
        }
}

//Round 3
bool round_3(int random_num){
    int user_answer_3;
    // Welcome message and instructions
     cout<<"You may need a calculator for the next rounds. Welcome to round 3."<<endl;
     cout<<"Figure out the next number in the sequence: "<<endl;
        cout<<random_num<<" ";
        int question_3 = random_num;
        // Multiplies the next number by random_num
        for (int i = 0; i < 3; i++) {
            question_3 = question_3*random_num;
            cout<<question_3<<" ";
        }
        cout<<endl<<"Answer: ";
        cin>>user_answer_3;
        // Checks if the user is correct
        if (user_answer_3 == question_3*random_num) {
            return true;
        } else {
            return false;
        }
}

//Round 4 Function
bool round_4(int random_num){
    int user_answer_4;
     cout<< "Welcome to round 4. Figure out the next number in the sequence: "<<endl;
        cout<<random_num<<" ";
        int question_4= random_num;
        // Adds the next number to random_num squared
        for (int i = 0; i < 3; i++) {
            question_4 = question_4+pow(random_num,2);
            cout<<question_4<<" ";
        }
        cout<<endl<<"Answer: ";
        cin>>user_answer_4;
        // Checks if the user is correct
        if (user_answer_4 == question_4+pow(random_num,2)) {
            return true;
        } else {
            return false;
        }
}

// Round 5
bool round_5 (int random_num) {
    int user_answer_5;
     cout<< "Welcome to round 5. Figure out the next number in the sequence: "<<endl;
        cout<<random_num<<" ";
        int question_5 = random_num;
        // Multiplies the next number by random_num, which increases by 1 each time
        for (int i = 0; i < 3; i++) {
            random_num++;
            question_5 = question_5*random_num;
            cout<<question_5<<" ";
        }
        random_num++;
        cout<<endl<<"Answer: ";
        cin>>user_answer_5;
        // Checks if the user is correct
        if (user_answer_5 == question_5*random_num) {
            return true;
        } else {
            return false;
        }
};