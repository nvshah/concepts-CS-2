package com.company.algos.search;

public class Search {

    /**
     * Oder Agnostic Binary Search
     *
     * @param arr    -> Array of (sorted) numbers
     * @param target -> to be search in array
     * @return index of target found otherwise -1
     */
    int binarySearch(int[] arr, int target) {
        if (arr.length == 0) {
            throw new RuntimeException("array is empty");
        }
        int last_index = arr.length - 1;
        if (arr[0] == arr[last_index]) {
            return arr[0] == target ? 0 : -1;
        }
        var isIncreasingOrder = arr[0] < arr[last_index];
        if (isIncreasingOrder) {
            int start = 0, end = arr.length - 1;
            while (start <= end) {
                int m = start + (end - start) / 2;
                if (target > arr[m]) {
                    //Search in right part
                    start = m + 1;
                } else if (target < arr[m]) {
                    //Search in left part
                    end = m - 1;
                } else {
                    return m;
                }
            }
        } else {
            int start = 0, end = arr.length - 1;
            while (start <= end) {
                int m = start + (end - start) / 2;
                if (target > arr[m]) {
                    //Search in left part
                    end = m - 1;
                } else if (target < arr[m]) {
                    //Search in Right part
                    start = m + 1;
                } else {
                    return m;
                }
            }
        }
        return -1;
    }
}
