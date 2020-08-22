package com.vvyun.structural.bridge;

/**
 * 桥接模式
 */
public class BridgePattern {
    public static void main(String[] args) {
        Draw draw = new CustomDraw(new RedColor(), new DefaultSharp());
        draw.draw();
        Draw draw1 = new CustomDraw(new BlackColor(), new DefaultSharp());
        draw1.draw();
    }
}

interface Sharp {
    void show();
}

interface Color {
    void show();
}

abstract class Draw {
    Draw(Color color, Sharp sharp) {
        this.color = color;
        this.sharp = sharp;
    }

    protected Color color;

    protected Sharp sharp;

    abstract void draw();
}

class RedColor implements Color {
    @Override
    public void show() {
        System.out.print("Color->RedColor");
    }
}

class BlackColor implements Color {
    @Override
    public void show() {
        System.out.print("Color->BlackColor");
    }
}

class DefaultSharp implements Sharp {
    @Override
    public void show() {
        System.out.print("sharp->DefaultSharp");
    }
}

class CustomDraw extends Draw {

    CustomDraw(Color color, Sharp sharp) {
        super(color, sharp);
    }

    @Override
    void draw() {
        System.out.println("start draw ...");
        this.sharp.show();
        this.color.show();
    }
}
