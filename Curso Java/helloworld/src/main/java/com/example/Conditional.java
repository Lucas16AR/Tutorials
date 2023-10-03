package com.example;

public class Conditional {
    public static void main(String[] args){

        Integer age = 20;
        Boolean isOlder = age >= 18;

        if (isOlder) {
            System.out.println("Es mayor de edad");
        } else {    
            System.out.println("Es menor de edad");
        }
    }   
}