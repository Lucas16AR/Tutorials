// Ejercicio de comparar 3 numeros y sacar el promedio

package com.exercises;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BooleanNumber {
    public static void main(String[] args) throws IOException {
        
        System.out.println("Ingrese un numero: ");
        Integer num = inputNumber();

        Boolean isPar = (num % 2) == 0;

        if (isPar) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
    }
}
    private static Integer inputNumber() throws IOException{
        InputStreamReader captureKeyboard = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(captureKeyboard);
        String strNum = reader.readLine();
        Integer num = Integer.parseInt(strNum);
        return num;
    }
}