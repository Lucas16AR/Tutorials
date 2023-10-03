package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ConsoleInput {
    
    public static void main(String[] args) throws IOException {

        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        System.out.println("Type name: ");
        String name = reader.readLine();
        System.out.println("Hello "+name);
    }
}