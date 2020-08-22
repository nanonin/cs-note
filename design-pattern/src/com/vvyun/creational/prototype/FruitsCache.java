package com.vvyun.creational.prototype;

import java.util.Hashtable;

public class FruitsCache {
    private static Hashtable<String,Fruits> fruitsHashtable = new Hashtable<>();

    public static Fruits getFruits(String key){
        Fruits fruits = fruitsHashtable.get(key);
        return (Fruits) fruits.clone();
    }

    public static void initFruilts(){
        Apple apple = new Apple();
        apple.setId("1");
        fruitsHashtable.put(apple.getId(),apple);
        Banana banana = new Banana();
        banana.setId("2");
        fruitsHashtable.put(banana.getId(),banana);
    }
}
