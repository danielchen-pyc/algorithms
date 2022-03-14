#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

// int lengthOfLongestSubstring(string s) {
//     int i = 0, j = 1;
//     int found = 0, longest = 1;
//     string subs = "";
//     while (j <= s.length() - 1) {
//         subs = s.substr(i, j-i);
//         found = subs.find(s[j]);
//         cout << subs << " " << i << " " << j << endl;
        
//         if (found == -1) {
//             j++;
//         } else {
//             i += found + 1;
//             j = i + 1;
//         }

//         if (j-i > longest) {
//             longest = j-i;
//         } 

//         cout << "Updated: " << subs << " " << i << " " << j << " " << longest << endl;
//     }

//     return longest;
// }

int lengthOfLongestSubstring(string s) {
    int i = 0, j = 0;
    string subs = "";
    int longest = 0;
    vector<int> charMap(128);
    while (j < s.length()) {
        char right = s[j];
        charMap[right]++;
        while (charMap[right] > 1) {
            char left = s[i];
            charMap[left]--;
            i++;
        }
        longest = max(longest, j-i+1);
        j++;
    }

    return longest;
}


int main() {
    cout << lengthOfLongestSubstring("abcabcbb") << endl;
    return 0;
}