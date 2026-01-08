"""
LeetCode: 2025 08 03 00.05.27 Accepted Runtime 47ms Memory 57.3MB

Algorithm:
Recursively compare two JSON objects. If they are identical, return empty object. If either is null or not an object, or if one is array and other is object, return [obj1, obj2]. Otherwise, iterate through keys in obj1. For each key that exists in obj2, recursively compute the difference of their values. If the sub-difference is non-empty, add it to the result object. Return the result object containing only keys with differences.

Time Complexity: O(?)
Space Complexity: O(?)
"""

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>

function objDiff(obj1: Obj, obj2: Obj): Obj {
    if (obj1 === obj2) return {};
    if (obj1 === null || obj2 === null) return [obj1, obj2];
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object') return [obj1, obj2];
    if (Array.isArray(obj1) !== Array.isArray(obj2)) return [obj1, obj2];

    const returnObject = {}
    for (const key in obj1) {
        if (key in obj2) {
            const subDiff = objDiff(obj1[key], obj2[key]);

            if (Object.keys(subDiff).length > 0) {
                returnObject[key] = subDiff
            }
        }
    }
    return returnObject
};