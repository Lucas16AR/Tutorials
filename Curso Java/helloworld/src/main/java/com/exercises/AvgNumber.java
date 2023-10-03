// Ejercicio de comparar 3 numeros y sacar el promedio

package com.exercises;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AvgNumber {
    public static void main(String[] args) throws IOException {
        
        System.out.println("Ingrese numero 1: ");
        Integer num1 = inputNumber();

        System.out.println("Ingrese numero 2: ");
        Integer num2 = inputNumber();

        System.out.println("Ingrese numero 3: ");
        Integer num3 = inputNumber();
    
        Integer total = num1 + num2 + num3;
        Double numAvg = Double.valueOf(total)/3;
        System.out.println("El promedio es de : " + numAvg);
    }

    private static Integer inputNumber() throws IOException{
        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        String strNum = reader.readLine();
        Integer num = Integer.parseInt(strNum);
        return num;
    }
}