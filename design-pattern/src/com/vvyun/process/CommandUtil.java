package com.vvyun.process;

import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class CommandUtil {

    public static void main(String[] args) {
        String res;
        try {
            res = CommandUtil.runs("C:\\Program Files\\Git\\bin\\bash","-c","ls");
            System.out.println(res);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String run(String command) throws IOException {
        Scanner input = null;
        String result = "";
        Process process = null;
        try {
            process = Runtime.getRuntime().exec(command);
            try {
                // 等待命令执行完成
                process.waitFor(10, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            InputStream is = process.getInputStream();
            input = new Scanner(is);
            while (input.hasNextLine()) {
                result += input.nextLine() + "\n";
            }
            result = command + "\n" + result; // 加上命令本身，打印出来
        } finally {
            if (input != null) {
                input.close();
            }
            if (process != null) {
                process.destroy();
            }
        }
        return result;
    }

    public static String runs(String... command) throws IOException {
        Scanner input = null;
        String result = "";
        Process process = null;
        try {
            process = Runtime.getRuntime().exec(command);
            try {
                // 等待命令执行完成
                process.waitFor(10, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            InputStream is = process.getInputStream();
            input = new Scanner(is);
            while (input.hasNextLine()) {
                result += input.nextLine() + "\n";
            }
            result = Arrays.toString(command) + "\n" + result; // 加上命令本身，打印出来
        } finally {
            if (input != null) {
                input.close();
            }
            if (process != null) {
                process.destroy();
            }
        }
        return result;
    }
}