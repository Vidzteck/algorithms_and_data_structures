#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    // Базовый случай
    if (s.length() <= 1) {
        return s;
    }
    // Рекурсивный случай
    return s.back() + reverseString(s.substr(0, s.length() - 1));
}

int main() {
    string testStr = "helloWorld!";
    cout << "Оригинал: " << testStr << endl;
    cout << "Перевёрнутая: " << reverseString(testStr) << endl;
    return 0;
}

//Вывод:
//Оригинал: helloWorld!
//Перевёрнутая: !dlroWolleh
