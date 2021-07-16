package com.nanonin.design.structural.facade;

// 外观模式
public class FacadePattern {
    public static void main(String[] args) {
        Facade facade = new Facade();
        facade.dance();
        facade.sing();
        facade.study();
    }
}

class Facade {
    private Dance dance;
    private Sing sing;
    private Study study;

    public Facade() {
        this.dance = new Dance();
        this.sing = new Sing();
        this.study = new Study();
    }

    public void study() {
        study.show();
    }

    public void sing() {
        sing.show();
    }

    public void dance() {
        dance.show();
    }
}

class Dance {
    void show() {
        System.out.println("DANCE");
    }
}

class Sing {
    void show() {
        System.out.println("SING");
    }
}

class Study {
    void show() {
        System.out.println("STUDY");
    }
}
