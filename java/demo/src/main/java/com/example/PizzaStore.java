package com.example;

import com.example.factory.PizzaFactory;
import com.example.pizza.Pizza;
import com.example.pizza.PizzaType;

public class PizzaStore {

    private PizzaFactory pizzaFactory;

    public PizzaStore(PizzaFactory pizzaFactory) {
        this.pizzaFactory = pizzaFactory;
    }

    public Pizza orderPizza(PizzaType pizzaType) {
        Pizza pizza = this.pizzaFactory.createPizza(pizzaType);

        pizza.prepare();
        pizza.bake();

        return pizza;
    }

    public void setPizzaFactory(PizzaFactory pizzaFactory) {
        this.pizzaFactory = pizzaFactory;
    }
}
