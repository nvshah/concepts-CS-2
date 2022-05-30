package com.company.DoubtsMine;

import java.util.ArrayList;
import java.util.List;

public class amazing_doubts_poly_generics {

    public static void main(String[] args) {
        //Why String is allowed to be add to ArrayList of type integer at run time
        List l = new ArrayList<Integer>();
        l.add("sds");
        System.out.println(l);
        System.out.println(l.getClass().getName());

        int[] arr = new int[10];
        System.out.println(arr[3]);
    }
}
