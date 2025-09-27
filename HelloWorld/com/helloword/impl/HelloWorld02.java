package com.helloword.impl;

import com.helloword.HelloWorld;

public class HelloWorld02 implements HelloWorld {

    @Override
    public void print() {
        System.out.print("Hello "); //打印 Hello
        System.out.println("World"); //打印 World
    }
}
