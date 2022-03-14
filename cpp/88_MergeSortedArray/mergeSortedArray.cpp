#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    if (n == 0) return;
    int j = 0;
    for (int i = 0; i < nums1.size() && j < n; i++) {
        if (nums1[i] > nums2[j]) {
            int k = m + j;
            while (k > i) {
                // cout << "swap " << nums1[k] << " " << nums1[k-1] << endl;
                swap(nums1[k], nums1[k-1]);
                k--;
            }
            // cout << "swap2 " << nums2[j] << " " << nums1[i] << endl;
            swap(nums2[j], nums1[i]);
            j++;
        }
        // cout << i << " ";
        if (i >= m + j) {
            swap(nums2[j], nums1[i]);
            j++;
        }
    }
    return;
}

int main() {
    vector<int> nums1{0,1,2,8,0,0};
    vector<int> nums2{0,2};
    merge(nums1, 4, nums2, 2);
    for (auto i: nums1) {
        cout << i << " ";
    }
    return 0;
}