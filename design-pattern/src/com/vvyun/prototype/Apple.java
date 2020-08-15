package com.vvyun.prototype;

public class Apple extends Fruits {

    public Apple() {
        setName("Apple");
    }

    @Override
    public void show() {
        System.out.println(toString());
    }
}
