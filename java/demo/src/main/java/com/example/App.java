package com.example;

import com.example.factory.PizzaFactory;
import com.example.pizza.PizzaType;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {

        PizzaFactory pizzaFactory = new PizzaFactory();
        PizzaStore pizzaStore = new PizzaStore(pizzaFactory);

        try {
            pizzaStore.orderPizza(PizzaType.VEGGIE);
        } catch (Exception e) {
        }

    }
}
