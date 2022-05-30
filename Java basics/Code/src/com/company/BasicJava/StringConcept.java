package com.company.BasicJava;

import java.util.ArrayList;

public class StringConcept {
    public static void main(String[] args) {
        // Operator Overloading for `+`
        //NOTE :- `+` concatenation operation is only defined for primitve or altleast 1 operand is string

        //1. Auto-Boxing of int to Integer Wrapper classes
        System.out.println("Int gets Wrapped " + 10); // Int gets Wrapped 10
        System.out.println(new Integer(10) + "" + new ArrayList<Integer>());  // 10[]
    }
}
