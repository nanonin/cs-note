package com.vvyun.creational.prototype;

public class Banana extends Fruits {

    public Banana(){
        setName("Banana");
    }

    @Override
    public void show() {
        System.out.println(toString());
    }
}
