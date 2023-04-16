package com.example.pizza;

public class CheesePizza implements Pizza {

    @Override
    public void prepare() {
        System.out.println("I prepare Cheese Pizza");
    }

    @Override
    public void bake() {
        System.out.println("I bake cheese Pizza");
    }

}
