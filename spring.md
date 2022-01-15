# spring

1. aop底层实现原理
   spring的aop是ioc容器的一个扩展功能，bean创建过程中有一个步骤可以对bean进行扩展，是在beanPostProcessor 的 后置处理器方法中进行实现的。 会进行代理对象的创建，通过jdk动态代理或者cglib生成代理对象，在执行方法调用时，会调用到生成的代理类中， 根据定义的通知生成拦截器链，从拦截器链中依次获取通知执行。

# spring boot

1. 与spring的区别
2. 自动配装原理
EnableAutoConfiguration; jar 包META-INFO 下的spring.factory;AutoConfig;ConditionsForClass;ConditionsMissBean'
3. 自动初始化web容器流程
SpringApplication.run(); onRefresh();createWebServer();获取ServletWebServerFactory工厂;getWebServer(); new tomcat();

