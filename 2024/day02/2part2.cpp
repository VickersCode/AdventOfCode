#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <bits/stdc++.h>

bool checkLevel(const std::vector<int>& level);
bool comp(int a, int b);


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

    if (checkLevel(level)) {
        numSafe++;
    } else {
        bool canBeSafe = false;
        for (int i = 0; i < level.size(); i++) {
            std::vector<int> tempLevel = level;
            tempLevel.erase(tempLevel.begin() + i);
            if (checkLevel(tempLevel)) {
                canBeSafe = true;
                break;
            }
        }
        if (canBeSafe) numSafe++;
    }
}

    std::cout << numSafe << std::endl;
    return 0;
}

bool checkLevel(const std::vector<int>& level) {
    if (level.size() < 2) return true;
    bool increasing = level[1] > level[0];
    for (int i = 1; i < level.size(); i++) {
        int diff = level[i] - level[i-1];
        if (increasing && (diff <= 0 || diff > 3)) return false;
        if (!increasing && (diff >= 0 || diff < -3)) return false;
    }
    return true;
}

bool comp(int a, int b) {
    return a > b;
}