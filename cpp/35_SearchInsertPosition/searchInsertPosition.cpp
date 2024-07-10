#include <stdio.h>
#include <iostream>
#include <vector>


using namespace std;

/***
 * Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
 * You must write an algorithm with O(log n) runtime complexity.
 * nums = [1,3,5,6], target = 2
*/

int searchInsert(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        if (target <= nums[i])
            return i;
    }
    return nums.size();
}

int searchInsertBinary(vector<int>& nums, int target) {
    int low = 0;
    int high = nums.size();
    int mid = (low+high)/2;
    if (target > nums[high-1]) return high;
    while (low <= high) {
        cout << low << " " << mid << " " << high << endl;
        mid = (low+high)/2;
        if (target == nums[mid]) return mid;
        if (target < nums[mid])
            high = mid-1;
        else
            low = mid+1;
    }
    return low;
}

int main() {
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(3);
    vec.push_back(5);
    vec.push_back(6);

    int target = 2;
    int ans;
    ans = searchInsert(vec, target);
    cout << ans << endl;
}