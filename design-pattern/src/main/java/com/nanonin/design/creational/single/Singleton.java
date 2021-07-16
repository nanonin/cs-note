package com.nanonin.design.creational.single;

/**
 * 单例模式
 */
public class Singleton {

    public static void main(String[] args) {
        singletonLazy s1 = singletonLazy.INSTANCE();
        singletonLazy s2 = singletonLazy.INSTANCE();
        System.out.println(s1 == s2);

        singleLazySynThreadSafe ss1 = singleLazySynThreadSafe.INSTANCE();
        singleLazySynThreadSafe ss2 = singleLazySynThreadSafe.INSTANCE();
        System.out.println(ss1 == ss2);

        singleLazyVolThreadSafe ssv1 = singleLazyVolThreadSafe.INSTANCE();
        singleLazyVolThreadSafe ssv2 = singleLazyVolThreadSafe.INSTANCE();
        System.out.println(ssv1 == ssv2);

        singletonHungry sh1 = singletonHungry.INSTANCE();
        singletonHungry sh2 = singletonHungry.INSTANCE();
        System.out.println(sh1 == sh2);

        singletonInnerClass si1 = singletonInnerClass.INSTANCE();
        singletonInnerClass si2 = singletonInnerClass.INSTANCE();
        System.out.println(si1 == si2);

        singletonEnum se1 = singletonEnum.INSTANCE;
        singletonEnum se2 = singletonEnum.INSTANCE;
        System.out.println(se1.toString());
        se2.setName("hello");
        System.out.println(se1.toString());

    }

    // 懒汉模式
    public static class singletonLazy {
        private static singletonLazy single;

        private singletonLazy() {
        }

        public static singletonLazy INSTANCE() {
            if (single == null) {
                single = new singletonLazy();
            }
            return single;
        }
    }

    // 懒汉模式加锁
    public static class singleLazySynThreadSafe {
        private static singleLazySynThreadSafe single;

        private singleLazySynThreadSafe() {
        }

        public synchronized static singleLazySynThreadSafe INSTANCE() {
            if (single == null) {
                single = new singleLazySynThreadSafe();
            }
            return single;
        }
    }

    // 懒汉模式volatile
    public static class singleLazyVolThreadSafe {
        private static volatile singleLazyVolThreadSafe single;

        private singleLazyVolThreadSafe() {
        }

        public static singleLazyVolThreadSafe INSTANCE() {
            if (single == null)
                synchronized (singleLazyVolThreadSafe.class) {
                    if (single == null)
                        single = new singleLazyVolThreadSafe();
                }

            return single;
        }
    }

    public static class singletonHungry {

        private static singletonHungry single = new singletonHungry();

        private singletonHungry() {
        }

        public static singletonHungry INSTANCE() {
            return single;
        }
    }

    public static class singletonInnerClass {

        private singletonInnerClass() {
        }

        private static class singleHolder {
            public static singletonInnerClass instance = new singletonInnerClass();
        }

        public static singletonInnerClass INSTANCE() {
            return singleHolder.instance;
        }
    }

    public enum singletonEnum {
        INSTANCE;

        private String name = "";

        public void setName(String name) {
            this.name = name;
        }

        public String toString() {
            return "single " + name;
        }
    }

}
