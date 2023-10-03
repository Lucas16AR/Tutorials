package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AgeInput {
    
        public static void main(String[] args) throws IOException {

        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        
        System.out.println("Enter age: ");
        String strAge = reader.readLine();
        Integer age = Integer.parseInt(strAge);

        if (age >= 18) {
            System.out.println("Es mayor de edad");
        } else {    
            System.out.println("Es menor de edad");
        }
    }
}
