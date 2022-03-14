#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

// int countBit(int n);

// vector<int> countBits(int n) {
//     vector<int> vec = {};
//     for (int i = 0; i <= n; i++) {
//         vec.push_back(countBit(i));
//     }
//     return vec;
// }

// int countBit(int n) {
//     int remainder = 0, count = 0;
//     while (n > 0) {
//         remainder = n % 2;
//         n /= 2;
//         // cout << n << " " << remainder << endl;
//         if (remainder == 1) count++;
//     }
//     return count;
// }

// vector<int> countBits(int n) {
//     vector<int> vec(n+1, -1);
//     for (int i = 0; i <= n; i++) {
//         int remainder = 0, count = 0;
//         int num = i;
//         while (i > 0) {
//             if (vec[i] != -1) {
//                 count += vec[i];
//                 break;
//             }
//             if (i % 2 == 1) count++;
//             i /= 2;
//         }
//         // cout << num << " " << count << endl;
//         vec[num] = count;
//     }
//     return vec;
// }

vector<int> countBits(int n) {
    vector<int> vec(n+1);
    vec[0] = 0;
    for(int i = 1; i<=n; ++i)
        vec[i] = vec[i/2] + i%2;
    return vec;
}

int main() {
    for (auto i: countBits(5)) {
        cout << i << endl;
    }
    return 0;
}