#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

// Function to check if a given update is in the correct order
bool isCorrectOrder(const vector<int>& update, const vector<pair<int, int>>& rules) {
    unordered_map<int, int> positions;
    for (int i = 0; i < update.size(); i++) {
        positions[update[i]] = i;
    }

    for (const auto& rule : rules) {
        int first = rule.first;
        int second = rule.second;
        if (positions.count(first) && positions.count(second)) {
            if (positions[first] >= positions[second]) {
                return false; // Rule violated
            }
        }
    }
    return true; // All rules respected
}

int main() {
    ifstream file("input.txt");
    string line;

    vector<pair<int, int>> rules;
    vector<vector<int>> updates;

    // Read rules
    while (getline(file, line)) {
        if (line.empty()) break;
        stringstream ss(line);
        string token;
        int first, second;
        getline(ss, token, '|');
        first = stoi(token);
        getline(ss, token, '|');
        second = stoi(token);
        rules.push_back({first, second});
    }

    // Read updates
    while (getline(file, line)) {
        stringstream ss(line);
        vector<int> update;
        int page;
        while (ss >> page) {
            update.push_back(page);
            if (ss.peek() == ',') ss.ignore();
        }
        updates.push_back(update);
    }

    // Verify updates
    int sumOfMiddlePages = 0;
    for (const auto& update : updates) {
        if (isCorrectOrder(update, rules)) {
            // Find the middle page
            int middleIndex = update.size() / 2;
            sumOfMiddlePages += update[middleIndex];
        }
    }

    cout << "Sum of middle pages in correct updates: " << sumOfMiddlePages << endl;

    return 0;
}
