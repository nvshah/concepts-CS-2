package com.company.Arrays;

import java.util.Arrays;
import java.util.Scanner;

public class MultiDimen {
    public static void main(String[] args) {
        /*
             1 2 3
             4 5 6
             7 8 9
        */
        Scanner in = new Scanner(System.in);

        int[][] arr = new int[3][3];
        System.out.println(arr.length); // no of rows
        // input

        for (int row = 0; row < arr.length; row++) {
            // for each col in every row
            for (int col = 0; col < arr[row].length; col++) {
                arr[row][col] = in.nextInt();
            }
        }

        for (int[] a : arr) {
            System.out.println(Arrays.toString(a));
        }

        int[][] arr2 = {
                {1, 2, 3},
                {4, 5},
                {6, 7, 8, 9}
        };

        for (int r = 0; r < arr2.length; r++) {
            for (int c = 0; c < arr2[r].length; c++) {
                System.out.println(arr2[r][c] + " ");
            }
        }

        for (int[] a : arr2) {
            System.out.println(Arrays.toString(a));
        }
    }
}
