package com.company.BasicJava;

import java.util.ArrayList;

public class EmojiConcept {
    private static String replaceChr(String str, String s, String t){
        int n = s.length();
        String ns = str;
        for(int i=0; i<n; i++){
            ns = ns.replace(s.charAt(i),t.charAt(i));
        }
        return ns;
    }

    private static String replaceStr(String str, String[] s, String[] t){
        int n = s.length;
        String ns = str;
        for(int i=0; i<n; i++){
            ns = ns.replace(s[i], t[i]);
        }
        return ns;
    }

    private static String addWSpaceToEnd(String s){
        int size = s.length();
        if(size > 0){
            char lastChar = s.charAt(size-1);
            if(!Character.isWhitespace(lastChar)){
                s += " ";
            }
        }
        return s;
    }

    public static void main(String[] args) {
        // Operator Overloading for `+`
        //NOTE :- `+` concatenation operation is only defined for primitve or altleast 1 operand is string

//        String s = "The⏩is the ⏩ true ⏩form↩Hola Noway";
//        System.out.println(s);
//        //Deecode
//        String d = replaceChr(s,"⏩↩", "\t\n");
//        System.out.println(d);
//        // Encode
//        String e = replaceChr(d, "\t\n", "⏩↩");
//        System.out.println(e);
        String s = "The\t";
        String j = addWSpaceToEnd(s);
        System.out.println(j + "...");

        //Deecode
//        String[] a1 = new String[]{"⏩", "↩"};
//        String[] a2 = new String[]{"\t", "\n"};
//
//        String d = replaceStr(s,a1, a2);
//        System.out.println(d);
//
//        String e = replaceStr(d, a2, a1);
//        System.out.println(e);

//        String t1 = "the \tis";
//        String t2 = "the    is";
//        System.out.println(t1);
//        System.out.println(t2);


    }
}
