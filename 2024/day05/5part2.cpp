#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <algorithm>

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

vector<int> reorderUpdate(const vector<int>& update, const vector<pair<int, int>>& rules) {
    // Build the graph
    unordered_map<int, vector<int>> graph;
    unordered_map<int, int> inDegree;
    unordered_set<int> updateSet(update.begin(), update.end());

    for (const auto& rule : rules) {
        int first = rule.first;
        int second = rule.second;

        if (updateSet.count(first) && updateSet.count(second)) {
            graph[first].push_back(second);
            inDegree[second]++;
            inDegree[first]; // Ensure every node exists in inDegree
        }
    }

    // Debug: Print the graph and in-degrees
    cout << "Graph for update: ";
    for (const auto& [key, value] : graph) {
        cout << key << " -> {";
        for (int v : value) cout << v << " ";
        cout << "} ";
    }
    cout << endl;

    cout << "In-degrees: ";
    for (const auto& [key, value] : inDegree) {
        cout << key << ":" << value << " ";
    }
    cout << endl;

    // Topological sort using Kahn's Algorithm
    queue<int> q;
    for (int page : update) {
        if (inDegree[page] == 0) {
            q.push(page);
        }
    }

    vector<int> sortedUpdate;
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        sortedUpdate.push_back(current);

        for (int neighbor : graph[current]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // Debug: Print the sorted update
    cout << "Sorted update: ";
    for (int page : sortedUpdate) cout << page << " ";
    cout << endl;

    return sortedUpdate;
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

    // Reorder incorrect updates and compute sum of middle pages
    int sumOfMiddlePages = 0;
for (auto& update : updates) {
    if (!isCorrectOrder(update, rules)) {
        cout << "Incorrect update before reordering: ";
        for (int page : update) cout << page << " ";
        cout << endl;

        update = reorderUpdate(update, rules);

        cout << "Reordered update: ";
        for (int page : update) cout << page << " ";
        cout << endl;

        // Find the middle page
        int middleIndex = update.size() / 2;
        sumOfMiddlePages += update[middleIndex];

        cout << "Middle page added: " << update[middleIndex] << endl;
    }
}

cout << "Final sum of middle pages: " << sumOfMiddlePages << endl;

    return 0;
}
