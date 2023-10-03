// Ejercicio de comparar 3 numeros sin funcion

package com.exercises;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CompareNumbers {
    public static void main(String[] args) throws IOException {
        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        
        System.out.println("Ingrese numero 1: ");
        String strNum1 = reader.readLine();
        Integer num1 = Integer.parseInt(strNum1);

        System.out.println("Ingrese numero 2: ");
        String strNum2 = reader.readLine();
        Integer num2 = Integer.parseInt(strNum2);

        System.out.println("Ingrese numero 3: ");
        String strNum3 = reader.readLine();
        Integer num3 = Integer.parseInt(strNum3);

        if (num1 > num2 && num1 > num3) {
            System.out.println("Numero 1 es el mas grande: " + num1);
        } else if (num2 > num1 && num2 > num3) {
            System.out.println("Numero 2 es el mas grande: " + num2);
        } else if (num3 > num1 && num3 > num2) {
            System.out.println("Numero 3 es el mas grande: " + num3);
        } else {    
            System.out.println("Hay igualdad");
        }

        if (num1 < num2 && num1 < num3) {
            System.out.println("Numero 1 es el mas chico: " + num1);
        } else if (num2 < num1 && num2 < num3) {
            System.out.println("Numerico 2 es el mas chico: " + num2);
        } else if (num3 < num1 && num3 < num2) {
            System.out.println("Numero 3 es el mas chico: " + num3);
        } else {
            System.out.println("Hay igualdad");
        }
    }
}