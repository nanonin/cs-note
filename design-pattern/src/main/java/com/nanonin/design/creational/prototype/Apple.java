package com.nanonin.design.creational.prototype;

public class Apple extends Fruits {

    public Apple() {
        setName("Apple");
    }

    @Override
    public void show() {
        System.out.println(toString());
    }
}
