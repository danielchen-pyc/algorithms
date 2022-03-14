#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

bool containsDuplicate(vector<int>& nums) {
    map<int, int> counter = {};
    for (int num: nums) {
        if (counter.find(num) == counter.end()) {
            counter[num] = 1;
        } else return true;
    }
    return false;
}

int main() {
    vector<int> nums{1,2,3,4};
    cout << containsDuplicate(nums) << endl;
    return 0;
}