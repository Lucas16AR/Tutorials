// Ejercicio de comparar 3 numeros con funcion y refactorizacion

package com.exercises;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CompareNumbersFunc {
    public static void main(String[] args) throws IOException {
        
        System.out.println("Ingrese numero 1: ");
        Integer num1 = inputNumber();

        System.out.println("Ingrese numero 2: ");
        Integer num2 = inputNumber();

        System.out.println("Ingrese numero 3: ");
        Integer num3 = inputNumber();
    
        calculeNumBigger(num1, num2, num3);
        calculeNumSmaller(num1, num2, num3);
    }

    private static Integer inputNumber() throws IOException{
        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        String strNum = reader.readLine();
        Integer num = Integer.parseInt(strNum);
        return num;
    }

    private static void calculeNumBigger(Integer num1, Integer num2, Integer num3){

        if (num1 > num2 && num1 > num3) {
            System.out.println("Numero 1 es el mas grande: " + num1);
        } else if (num2 > num1 && num2 > num3) {
            System.out.println("Numero 2 es el mas grande: " + num2);
        } else if (num3 > num1 && num3 > num2) {
            System.out.println("Numero 3 es el mas grande: " + num3);
        } else {    
            System.out.println("Hay igualdad");
        }
    }

    private static void calculeNumSmaller(Integer num1, Integer num2, Integer num3){
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