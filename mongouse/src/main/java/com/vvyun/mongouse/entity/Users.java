package com.vvyun.mongouse.entity;

/**
 * @author nuagesnoirs
 */
public class Users {

    private String name;
    private Integer age;
    private String like;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getLike() {
        return like;
    }

    public void setLike(String like) {
        this.like = like;
    }

    @Override
    public String toString() {
        return "Users{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", like='" + like + '\'' +
                '}';
    }
}
