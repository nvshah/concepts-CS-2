package com.company.BasicJava;

public class ClassName {

    public static void main(String[] args) {
        int x = 5;
        System.out.println(((Object)x).getClass().getSimpleName()); // Integer

        boolean b = true;
        System.out.println(((Object)b).getClass().getSimpleName()); // Boolean

        String s = "csdsd";
        System.out.println(((Object)s).getClass().getSimpleName()); // String
    }
}
