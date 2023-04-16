package com.example.pizza;

public class VeggiePizza implements Pizza {
    public void prepare() {
        System.out.println("I prepare Veggie pizza");
    }

    public void bake() {
        System.out.println("I bake Veggie Pizza");
    }
}
