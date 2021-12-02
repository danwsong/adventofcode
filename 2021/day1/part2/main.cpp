#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> depths;
    int depth;
    while (cin >> depth) {
        depths.push_back(depth);
    }
    int increases = 0;
    for (int i = 3; i < depths.size(); ++i) {
        if (depths[i] > depths[i - 3]) {
            ++increases;
        }
    }
    cout << increases << endl;
}
