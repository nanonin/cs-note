# spring

## Spring IOC，原理与实现

控制反转 原先对象及依赖由使用者进行控制的，现在有容器进行管理。 依赖注入DI，对象的依赖，属性，值由容器进行注入管路，可以通过注解，xml（populateBean）配置等进行
容器 map 存储bean，singletonObjects bean 存在三级缓存中。c

容器原理，创建过程 beanFactory DefaultListableBeanFactory

## bean的生命周期

实例化bean对象（反射生产对象）->
populateBean 设置对象属性（循环依赖问题 三级缓存）->
检查aware及相关接口并设置依赖->BeanPostProcessor前置处理器->检查是否是initializingBean以及决定是否调用afterPropertiesSet方法->检查是否有自定义的init-method -> BeanPostProcessor 后置处理器- -> 注册Desturction相关回调接口->使用中->是否是实现DisposableBean接口   是否配置有自定义destroy方法
