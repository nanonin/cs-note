package com.nanonin.design.structural.flyweight;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

// 享元模式
public class FlyweightPattern {
    public static void main(String[] args) {
        Obj objA = ObjFactory.getObj("A");
        Obj objA1 = ObjFactory.getObj("A");
        objA1.setType("22");
        System.out.println(objA.toString());
        System.out.println(objA == objA1);
        Obj objB = ObjFactory.getObj("B");
        objB.setType("33");
        System.out.println(objB.toString());
    }
}

class Obj {
    private String name;
    private String type;

    public Obj(String name) {
        this.name = name;
    }

    public void show() {
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        return "Obj{" +
                "name='" + name + '\'' +
                ", type='" + type + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

}

class ObjFactory {
    private static final Map<String, Obj> objCache = new ConcurrentHashMap<>();

    public static Obj getObj(String name) {
        Obj obj = objCache.get(name);
        if (obj == null) {
            obj = new Obj(name);
            objCache.put(name, obj);
            System.out.println("crate obj " + name);
        }
        return obj;
    }
}
