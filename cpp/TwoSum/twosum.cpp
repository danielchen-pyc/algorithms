#include <stdio.h>
#include <iostream>
#include <vector>


using namespace std;

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        // if (nums[i] > target) continue;
        for (int j = i+1; j < nums.size(); j++) {
            if (nums[j] == target - nums[i]) {
                vector<int> ans = {i, j};
                return ans;
            }
        }
    }
    vector<int> vec = {0, 1};
    return vec;
}

int main() {
    vector<int> vec;
    vec.push_back(-1);
    vec.push_back(-2);
    vec.push_back(-3);
    vec.push_back(-4);
    vec.push_back(-5);

    int target = -8;
    vector<int> ans;
    ans = twoSum(vec, target);
    for (auto i: twoSum(vec, target))
        cout << i << ' ';
}