package com.company;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("HAhahahaha");

        Integer i = 1000;
        Integer i2 =1000;
        int i3 = 1000;

        System.out.println(i.equals(i2)); //true
        System.out.println(i == i2);  //false

        System.out.println(i3 == i);  //Unboxing when compare to numeric type & compare then value wise
    }
}
