1. java基本类型
int 32 short 16  float 32 long 64 double 64 char 16 byte 8 boolean 8 (1字节8位)
2. String能被继承吗？为什么？
不可以，String类是被final修饰的类，不可变，优化内存，重复的字符串只有一个实例。var1 = new String("str") 与 var2 = "str" 不相等，尽量避免使用new String进行String赋值。 
3. String StringBuilder StringBuffer区别
String final类，不可变，每次赋值会指向一个新地址
StringBulider  字符数组，可变长，可相加，toString会返回一个新String
StringBuffer（加了同步，线程安全）==是final类别，不可继承 toString会缓存对象。
4. ArrayList和LinkedList区别
ArrayList数组，查询快。 LinkedList链表 有前后指针，占用内存大 添加 修改 删除 操作快，查询慢。
5. 类初始化顺序
有父类先父类 父类静态变量 静态代码块 子类 静态变量 静态代码块 父类非静态变量，构造函数，子类非静态变量，构造器。
6. 有哪些Map类
HashMap（线程不安全）数组加链表|红黑树 LinkedHashMap TreeMap HashTable ConcurrentHashMap 
默认8，每次x2,
7. 有没有有顺序的 Map 实现类， 如果有， 他们是怎么保证有序的。
TreeMap（默认按升序排序，可重写比较方法）、LinkedHasnMap（链表记录插入顺序）
8. 抽象类和接口的区别，类可以继承多个类么，接口可以继承多个接口么,类可以实现多个接口么。
类不可以继承多个类，接口可以。抽象类可以有自己的变量，可以有方法实现，接口不行，只能声明方法。
抽象类被继承 接口被实现才可以用。abstruct修饰的方法不可实现。
接口可继承多个接口，类可以实现多个类，类不能继承多个类。
9. 继承和聚合
继承是子类继承父类extends，有明确依赖关系，子类可继承父类的属性和方法，并添加独有的特性；聚合关联关系的一种，体现整体与部分，包含的关系。
10. 讲讲你理解的 nio和 bio 的区别是啥，谈谈 reactor 模型。
IO(BIO)是面向流的，NIO是面向缓冲区的
BIO：Block IO 同步阻塞式 IO，就是我们平常使用的传统 IO，它的特点是模式简单使用方便，并发处理能力低。
NIO：New IO 同步非阻塞 IO，是传统 IO 的升级，客户端和服务器端通过 Channel（通道）通讯，实现了多路复用。
AIO：Asynchronous IO 是 NIO 的升级，也叫 NIO2，实现了异步非堵塞 IO ，异步 IO 的操作基于事件和回调机制。
11. 反射的原理，反射创建类实例的三种方式是什么
通过class的getDeclaredMethod,Methid.invoke 获取。
Class A = new ClassA().getClass();1
Class A = ClassA.class;2
Class A = Class.forName("ClassA");3

class = Class.forName("Test"); constructor = class.getConstructor()Test = constructor.newInstance;

12. 反射中，Class.forName 和 ClassLoader 区别。
Class.forName(className)方法,目标对象的 static块代码已经被执行，static参数也已经被初始化
ClassLoader.loadClass(className) 只装载，不进行链接，不执行静态代码块
13. 描述动态代理的几种实现方式，分别说出相应的优缺点。
Jdk cglib 
jdk底层是利用反射机制，需要基于接口方式，这是由于
```Java
Proxy.newProxyInstance(target.getClass().getClassLoader(),
target.getClass().getInterfaces(), this);
```
Cglib则是基于asm框架，实现了无反射机制进行代理，利用空间来换取了时间，代理效率高于jdk
同上（jdk invocationHandler  cglib methodInterceptor）
15. final 的用途
类、变量、方法
final 修饰的类叫最终类，该类不能被继承。
final 修饰的方法不能被重写。
final 修饰的变量叫常量，常量必须初始化，初始化之后值就不能被修改。
16. 写出三种单例模式实现。
懒汉，饿汉，双重检测，静态内部类，枚举
17. 如何在父类中为子类自动完成所有的 hashcode 和 equals 实现？这么做有何优劣。
同时复写hashcode和equals方法，优势可以添加自定义逻辑，且不必调用超类的实现。
优点，我们不用自己去写
但缺点就是有时父类的equals和hashcode不满足我们自己的要求，我们需要重新去重写。
18.请结合 OO 设计理念，谈谈访问修饰符 public、private、protected、default 在应用设计中的作用。
public所有 private尽自己 protect本包内及子类 default包内
19. 深拷贝和浅拷贝区别。
深拷贝 复制所有值 浅拷贝 只复制引用
20. 数组和链表数据结构描述，各自的时间复杂度
Java.lang.ArithmeticException
Java.lang.ArrayStoreExcetpion
Java.lang.ClassCastException
Java.lang.IndexOutOfBoundsException
Java.lang.NullPointerException
33. String 类的常用方法都有那些？
indexOf()：返回指定字符的索引。
charAt()：返回指定索引处的字符。
replace()：字符串替换。
trim()：去除字符串两端空白。
split()：分割字符串，返回一个分割后的字符串数组。
getBytes()：返回字符串的 byte 类型数组。
length()：返回字符串长度。
toLowerCase()：将字符串转成小写字母。
toUpperCase()：将字符串转成大写字符。
substring()：截取字符串。
equals()：字符串比较。
34. 抽象类必须要有抽象方法吗？
不需要，抽象类不一定非要有抽象方法。
35. java 中 IO 流分为几种？
按功能来分：输入流（input）、输出流（output）。

按类型来分：字节流和字符流。

字节流和字符流的区别是：字节流按 8 位传输以字节为单位输入输出数据，字符流按 16 位传输以字符为单位输入输出数据。
36. Files的常用方法都有哪些？
Files.exists()：检测文件路径是否存在。
Files.createFile()：创建文件。
Files.createDirectory()：创建文件夹。
Files.delete()：删除一个文件或目录。
Files.copy()：复制文件。
Files.move()：移动文件。
Files.size()：查看文件个数。
Files.read()：读取文件。
Files.write()：写入文件。
38. 如何实现数组和 List 之间的转换？ 
List转换成为数组：调用ArrayList的toArray方法。
数组转换成为List：调用Arrays的asList方法

41.在 Queue 中 poll()和 remove()有什么区别？
poll() 和 remove() 都是从队列中取出一个元素，但是 poll() 在获取元素失败的时候会返回空，但是 remove() 失败的时候会抛出异常。
42. 哪些集合类是线程安全的？
vector：就比arraylist多了个同步化机制（线程安全），因为效率较低，现在已经不太建议使用。在web应用中，特别是前台页面，往往效率（页面响应速度）是优先考虑的。
statck：堆栈类，先进后出。
hashtable：就比hashmap多了个线程安全。
enumeration：枚举，相当于迭代器。
43. 迭代器 Iterator 是什么？
迭代器是一种设计模式，它是一个对象，它可以遍历并选择序列中的对象，而开发人员不需要了解该序列的底层结构。迭代器通常被称为“轻量级”对象，因为创建它的代价小。
44. Iterator 怎么使用？有什么特点？
Java中的Iterator功能比较简单，并且只能单向移动：

(1) 使用方法iterator()要求容器返回一个Iterator。第一次调用Iterator的next()方法时，它返回序列的第一个元素。注意：iterator()方法是java.lang.Iterable接口,公共基类Collection提供iterator()方法。

(2) 使用next()获得序列中的下一个元素。

(3) 使用hasNext()检查序列中是否还有元素。

(4) 使用remove()将迭代器新返回的元素删除。

Iterator是Java迭代器最简单的实现，为List设计的ListIterator具有更多的功能，它可以从两个方向遍历List，也可以从List中插入和删除元素。
46. synchronized 和 volatile 的区别是什么？
volatile本质是在告诉jvm当前变量在寄存器（工作内存）中的值是不确定的，需要从主存中读取； synchronized则是锁定当前变量，只有当前线程可以访问该变量，其他线程被阻塞住。
volatile仅能使用在变量级别；synchronized则可以使用在变量、方法、和类级别的。
volatile仅能实现变量的修改可见性，不能保证原子性；而synchronized则可以保证变量的修改可见性和原子性。
volatile不会造成线程的阻塞；synchronized可能会造成线程的阻塞。
volatile标记的变量不会被编译器优化；synchronized标记的变量可以被编译器优化。