#include <iostream>
#include <stdio.h>
#include <vector>
#include <limits.h>

using namespace std;

int maxSubArray(vector<int>& nums) {
    int sum = 0;
    int res = INT_MIN;
    int i = 0;
    while (i < nums.size()) {
        if (sum < 0) {
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        res = max(res, sum);
        i++;
    }
    return res;
}

int main() {
    vector<int> nums{1,2};
    cout << maxSubArray(nums) << endl;
    return 0;
}