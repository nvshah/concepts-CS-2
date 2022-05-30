package com.company.algos.search.Questions;

public class RotatedBinarySearch {

    public static void main(String[] args) {
//        int[] arr = {4,5,6,7,0,1,2};
//        System.out.println(countRotations(arr));
        //int[] arr1 = {7, 8, 9, 1,2,3, 5, 6 };  //Odd length causing issue
        //int[] arr1 = {4,5,6,7,0,1,2};
        int[] arr2 = {5,5,5,5,6,6};
        int[] arr3 = {5,5,1,2,5,5,5,5};
        int[] arr4 = {1, 2, 3, 4, 5};
        int[] arr5 = {2,9,2,2,2,2,2};

        int[] arr1 = {1,2,3,4,5,6,7};  //Odd length causing issue
        int pivot2 = findPivotWithDuplicates(arr1);
        //int pivot3 = findPivot(arr5);
        System.out.println(pivot2);
    }

    private static int countRotations(int[] arr) {
        int pivot = findPivot(arr);
        return pivot + 1;


    }

    // use this for non duplicates
    static int findPivot(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            // 4 cases over here
            if (mid < end && arr[mid] > arr[mid + 1]) {
                return mid;
            }
            if (mid > start && arr[mid] < arr[mid - 1]) {
                return mid-1;
            }
            if (arr[mid] < arr[start]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }

    // use this when arr contains duplicates
    static int findPivotWithDuplicates(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            // 4 cases over here
            if (mid < end && arr[mid] > arr[mid + 1]) {
                return mid;
            }
            if (mid > start && arr[mid] < arr[mid - 1]) {
                return mid-1;
            }

            // if elements at middle, start, end are equal then just skip the duplicates
            if (arr[mid] == arr[start] && arr[mid] == arr[end]) {
                // skip the duplicates
                // NOTE: what if these elements at start and end were the pivot??
                // check if start is pivot
                if (arr[start] > arr[start + 1]) {
                    return start;
                }
                start++;

                // check whether end is pivot
                if (arr[end] < arr[end - 1]) {
                    return end - 1;
                }
                end--;
            }
            // left side is sorted, so pivot should be in right
            //else if(arr[start] < arr[mid] || (arr[start] == arr[mid] && arr[mid] > arr[end])) {
            else if(arr[start] <= arr[mid]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
}
