# spring boot

## spring boot工程发布到weblogic

pom.xml修改打包方式为war

```Xml
    <packaging>war</packaging>
    <!--<packaging>jar</packaging>-->
```

添加依赖

```Xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-tomcat</artifactId>
        <scope>provided</scope>
    </dependency>
```

修改启动类

```Java
@SpringBootApplication
public class XxxApplication  extends SpringBootServletInitializer implements WebApplicationInitializer {

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(XxxApplication.class);
    }

    public static void main(String[] args) {
        SpringApplication.run(XxxApplication.class, args);
    }

}
```

打包

```Shell
mvn package
```

添加weblogic.xml到war包的WEB-INF文件夹下

```Xml
<?xml version="1.0" encoding="UTF-8"?>
<wls:weblogic-web-app
    xmlns:wls="http://xmlns.oracle.com/weblogic/weblogic-web-app"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
        http://java.sun.com/xml/ns/javaee/ejb-jar_3_0.xsd
        http://xmlns.oracle.com/weblogic/weblogic-web-app
        http://xmlns.oracle.com/weblogic/weblogic-web-app/1.4/weblogic-web-app.xsd">
    <wls:container-descriptor>
        <wls:prefer-application-packages>
            <wls:package-name>org.slf4j</wls:package-name>
        </wls:prefer-application-packages>
    </wls:container-descriptor>
     <wls:context-root>/</wls:context-root>
</wls:weblogic-web-app>
```
