package com.example;

public class Introduction {
    public static void main(String[] args) {
        
        String name = "Lucas";
        Integer followersInstagram = 555;
        Integer followersYoutube = 1500;
        String phrase = "Hola, mi nombre es " + name + ", con " + (followersInstagram + followersYoutube) + " seguidores en las redes sociales.";
        System.out.println(phrase);

    }
}