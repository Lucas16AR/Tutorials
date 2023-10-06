package com.exercises;

public class NumPri {
    public static void main(String[] args) {
       String result = "";
       
       int counter = 0;
       int number = 1;
       while(counter < 100) {
           if (esPrimo(number)) {
               result += number + ", ";
               counter++;
           }
           number++;
       }
       System.out.println("Los primeros 100 números primos son: " + result);
    }
    
    private static Boolean esPrimo(Integer number) {
        Boolean isNumPrim = true;
        
        for (int i = 2; i < number; i++) {
            
            if (number % i == 0) {
                isNumPrim = false;
            }
        }
       return isNumPrim;
    }
}