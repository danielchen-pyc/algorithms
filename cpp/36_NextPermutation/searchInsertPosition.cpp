#include <stdio.h>
#include <iostream>
#include <vector>


using namespace std;


/***
 * A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
 * 
 * For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
 * The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations 
 * of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the 
 * permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order 
 * (i.e., sorted in ascending order).
 * 
 * For example, the next permutation of arr = [1,2,3] is [1,3,2].
 * Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
 * While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
 * Given an array of integers nums, find the next permutation of nums.
 * 
 * The replacement must be in place and use only constant extra memory.
*/


void nextPermutation(vector<int>& nums) {
    int size = nums.size();
        int k = -1;
        for (int i=size-2; i>=0; i--) {
            // find last number that is smaller than its next number
            if (nums[i] < nums[i+1]) {
                k = i;
                break;
            }
        }

        if (k == -1) {
            sort(nums.begin(), nums.end());
            return;
        }

        int j = -1, nextVal = 101; // max number is 100
        for (int i=k+1; i<size; i++) {
            // find k'th number's next number (smallest number greater than k'th number)
            if (nums[i] > nums[k] && nextVal >= nums[i]) {
                nextVal = nums[i];
                j = i;
            }
        }

        swap(nums[j], nums[k]);
        for (int i=0; i<size; i++) {
            cout << nums[i] << " ";
        }

        reverse(nums.begin()+k+1, nums.end());
    }
}

int main() {
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(3);
    vec.push_back(5);
    vec.push_back(6);

    int target = 2;
    int ans;
    ans = nextPermutation(vec);
    cout << ans << endl;
}