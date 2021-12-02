#include <iostream>
#include <string>

using namespace std;

int main() {
    string dir;
    int mag;
    
    int pos = 0;
    int depth = 0;

    while (cin >> dir >> mag) {
        if (dir == "forward") {
            pos += mag;
        }
        if (dir == "up") {
            depth -= mag;
        }
        if (dir == "down") {
            depth += mag;
        }
    }

    cout << pos * depth << endl;
}
