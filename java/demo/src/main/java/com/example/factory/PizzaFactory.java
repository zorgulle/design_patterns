package com.example.factory;

import com.example.pizza.CheesePizza;
import com.example.pizza.Pizza;
import com.example.pizza.PizzaType;
import com.example.pizza.VeggiePizza;

public class PizzaFactory {
    public PizzaFactory() {
    }

    public Pizza createPizza(PizzaType pizzaType) {
        Pizza pizza = null;
        switch (pizzaType) {
            case VEGGIE:
                pizza = new VeggiePizza();
                break;
            case CHEESE:
                pizza = new CheesePizza();
                break;
            default:
                break;
        }
        return pizza;
    }
}
