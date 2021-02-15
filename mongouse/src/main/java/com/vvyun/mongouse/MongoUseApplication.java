package com.vvyun.mongouse;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class MongoUseApplication {

    public static void main(String[] args) {
        SpringApplication.run(MongoUseApplication.class, args);
    }

}
