package com.company.Questions;

import java.util.Scanner;

public class SolveTask {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        //int n = in.nextInt();
        //boolean ans = isPrime(n);
        //System.out.println(ans);

        for (int i = 100; i < 1000; i++) {
            if (isArmstrong(i)) {
                System.out.print(i + " ");
            }
        }
    }

    // print all the 3 digits armstrong numbers
    static boolean isArmstrong(int n) {
        int original = n;
        int sum = 0;

        while (n > 0) {
            int rem = n % 10;
            n = n / 10;
            sum = sum + rem*rem*rem;
        }

        return sum == original;
    }

    static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        int c = 2;
        while (c * c <= n) {
            if (n % c == 0) {
                return false;
            }
            c++;
        }
        return c * c > n;
    }

    //Check If no. contains even digits or not
    static boolean evenDigits(int num) {
        int numberOfDigits = getDigitsCount_logA(num);
        return numberOfDigits % 2 == 0;
    }

    // count number of digits in a number
    static int getDigitsCount_logA(int num) {
        if (num < 0) {
            num = num * -1;
        }
        return (int)(Math.log10(num)) + 1;
    }

    // count number of digits in a number
    static int getDigitsCount_naiveA(int num) {

        if (num < 0) {
            num = num * -1;
        }

        if (num == 0) {
            return 1;
        }

        int count = 0;
        while (num > 0) {
            count++;
            num = num / 10; // num /= 10
        }

        return count;
    }

    // check if given num is palindrome or not
    static boolean isPalindrome(int num){
        if(num < 0) return false;
        int r_num = 0, t_num = num;
        while(t_num > 0){
            t_num = t_num / 10;
            int remainder = t_num % num;
            r_num = r_num * 10 + remainder;
        }
        return r_num == num;
    }

}
