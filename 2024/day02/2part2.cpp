#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <bits/stdc++.h>

bool comp(int a, int b) {
    return a > b;
}

int main() {
    int numSafe = 0;
    std::ifstream fin("2.txt");
    std::string line;

    while (std::getline(fin, line)) {
        std::istringstream iss(line);
        std::vector<int> level;
        int numRead;

        while (iss >> numRead) {
            level.push_back(numRead);
        }        

        bool wereGood = false;

        for (int i = 0; i < level.size() - 1; i++) {
            
            int badLevels = 0;
            if ((abs(level[i+1] - level[i]) <= 3 && abs(level[i+1] - level[i]) > 0) && ((is_sorted(level.begin(), level.end())) || (is_sorted(level.begin(), level.end(), comp)))) {
                wereGood = true;
            }
            else {
                wereGood = false;
                break;
            }
        }
        if (wereGood) {
            numSafe++;
        }
    }

    std::cout << numSafe << std::endl;
    return 0;
}

