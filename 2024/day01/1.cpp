#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <bits/stdc++.h>

int main() {
    int totalDist = 0;
    int totalSimScore = 0;
    std::ifstream fin("1.txt");

    std::vector<int> column1;
    std::vector<int> column2;

    std::string line;
    while (std::getline(fin, line)) {
        std::istringstream iss(line);
        int col1, col2;

        if (iss >> col1 >> col2) {
            column1.push_back(col1);
            column2.push_back(col2);
        }
    }

    fin.close();


// ===============PART ONE=====================    

    sort(column1.begin(), column1.end());
    sort(column2.begin(), column2.end());    

    
    for (int i = 0; i < column1.size(); i++) {
        int tempDist = abs(column1[i] - column2[i]);
        totalDist += tempDist; 
    }

    std::cout << totalDist << std::endl;

// ===============PART TWO====================

    for (int i = 0; i < column1.size(); i++) {
        int tempVar = (std::count(column2.begin(), column2.end(), column1[i])) * column1[i];
        totalSimScore += tempVar;
    }

    std::cout <<totalSimScore << std::endl;


    return 0;
}