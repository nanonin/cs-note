package com.vvyun.mongouse.controller;

import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import com.vvyun.mongouse.entity.Users;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.BasicUpdate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author nuagesnoirs
 * test mongodb cuda example
 */
@RestController
@RequestMapping("/test")
public class TestController {

    private final MongoTemplate mongoTemplate;

    public TestController(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @RequestMapping("/t1")
    public void test() {
        try {

            // insert
            Users newUsers = new Users();
            newUsers.setName("kati");
            newUsers.setAge(20);
            newUsers.setLike("apple");
            Users userRes = mongoTemplate.insert(newUsers);
            System.out.println(userRes.toString());

            // update
            UpdateResult updateResult = mongoTemplate.updateFirst(
                    Query.query(Criteria.where("name").is("kati")),
                    BasicUpdate.update("age", 21),
                    Users.class);
            System.out.println("update result count" + updateResult.getMatchedCount());

            // query
            Query query = new Query(Criteria.where("name").is("kati"));
            Users user = mongoTemplate.findOne(query, Users.class);
            assert user != null;
            System.out.println(user.toString());

            // delete
            DeleteResult deleteResult = mongoTemplate.remove(query, Users.class);
            System.out.println("delete result count" + deleteResult.getDeletedCount());

            // query all
            List<Users> list = mongoTemplate.findAll(Users.class);
            list.forEach(users -> System.out.println("users:" + users.toString()));

        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }
    }
}
