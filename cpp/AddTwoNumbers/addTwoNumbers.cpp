#include <iostream>
#include <stdio.h>

using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int carry = 0;
    ListNode* ans = new ListNode(0, nullptr);
    ListNode* next = ans;
    while (l1 != NULL && l2 != NULL) {
        next->val = (l1->val + l2->val + carry) % 10;
        carry = (l1->val + l2->val + carry) / 10;
        if (l1->next == NULL && l2->next == NULL) {
            if (carry != 0) {
                next->next = new ListNode(carry, nullptr);
            } else {
                next->next = NULL;
            }
        } else {
            if (l1->next == NULL && l2->next != NULL) {
                next->next = addTwoNumbers(l2->next, new ListNode(carry, nullptr));
                return ans;
            } else if (l1->next != NULL && l2->next == NULL) {
                next->next = addTwoNumbers(l1->next, new ListNode(carry, nullptr));
                return ans;
            }
            next->next = new ListNode();
        }

        next = next->next;
        l1 = l1->next;
        l2 = l2->next;
    }
    return ans;
}

ListNode* generateList(int list[], int index, int size) {
    if (index == size) return nullptr;
    ListNode* head = new ListNode();
    head->val = list[index];
    head->next = generateList(list, ++index, size);
    return head;
}

int main() {
    int l1[] = {1, 4, 5, 9, 9};
    int l2[] = {1, 6, 4};

    ListNode* head1 = generateList(l1, 0, sizeof(l1)/sizeof(int));
    ListNode* head2 = generateList(l2, 0, sizeof(l2)/sizeof(int));

    ListNode* res = addTwoNumbers(head1, head2);
    ListNode* next = res;
    
    while (next != NULL) {
        cout << next->val << endl;
        next = next->next;
    }
    return 0;
}