"""
LeetCode: 2024 11 02 21.19.56 Accepted Runtime 3ms Memory 9.6MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

typedef struct {
    HashNode** table;
    int size;
} HashTable;

int hash(int key, int size) {
    return abs(key) % size;
}

HashTable* createTable(int size) {
    HashTable* newTable = (HashTable*)malloc(sizeof(HashTable));
    newTable->table = (HashNode**)malloc(sizeof(HashNode*) * size);
    newTable->size = size;
    for (int i = 0; i < size; i++) {
        newTable->table[i] = NULL;
    }
    return newTable;
}

void insert(HashTable* table, int key, int value) {
    int index = hash(key, table->size);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = table->table[index];
    table->table[index] = newNode;
}

int find(HashTable* table, int key) {
    int index = hash(key, table->size);
    HashNode* node = table->table[index];
    while (node != NULL) {
        if (node->key == key) return node->value;
        node = node->next;
    }
    return -1;
}

void freeTable(HashTable* table) {
    for (int i = 0; i < table->size; i++) {
        HashNode* node = table->table[i];
        while (node != NULL) {
            HashNode* temp = node;
            node = node->next;
            free(temp);
        }
    }
    free(table->table);
    free(table);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashTable* table = createTable(numsSize * 2);
    
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int complementIndex = find(table, complement);

        if (complementIndex != -1) {
            int* result = (int*)malloc(2 * sizeof(int));
            result[0] = complementIndex;
            result[1] = i;
            *returnSize = 2;
            freeTable(table);
            return result;
        }
        
        insert(table, nums[i], i);
    }

    *returnSize = 0;
    freeTable(table);
    return NULL;
}
