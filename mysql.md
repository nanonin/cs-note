## 安全相关

### 账户不具备唯一性。未配置口令复杂度策略和口令有效期策略。

[https://www.jb51.net/article/79347.htm]

可以在MySQL的配置文件中设置一个默认值，这会使得所有MySQL用户的密码过期时间都为90天，MySQL会从启动时开始计算时间。my.cnf配置如下：
```
[mysqld]
default_password_lifetime=90
```
如果要设置密码永不过期的全局策略，可以这样：（注意这是默认值，配置文件中可以不声明）
```
[mysqld]
default_password_lifetime=0
```
在MySQL运行时可以使用超级权限修改此配置：
```
mysql> SET GLOBAL default_password_lifetime = 90;
Query OK, 0 rows affected (0.00 sec)
```
安装密码复杂度插件
```
INSTALL PLUGIN validate_password SONAME 'validate_password.so';
# 3、查看默认策略配置：
show variables like 'validate_password%'; 
# validate_password_policy：密码安全策略，默认MEDIUM策略 (0|LOW,1|MEDIUM,2|STRONG)
# 修改策略（将策略要求置为LOW，长度要求置为8）
set global validate_password_policy=0;
set global validate_password_length=8;
```
### 未配置登录失败处理策略。

修改方法 [https://blog.csdn.net/ywd1992/article/details/83865537]

1、登录数据库，安装插件（CONNECTION_CONTROL和CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS）

```
mysql -uroot -p

install plugin CONNECTION_CONTROL soname 'connection_control.so';
install plugin CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS soname 'connection_control.so';
```

2、查看所有已安装的插件
```
show plugins;
```
3、按需修改配置文件（/etc/my.cnf）
```
vim /etc/my.cnf
```
添加如下两行配置：
```
connection-control-failed-connections-threshold=5   #登陆失败次数限制
connection-control-min-connection-delay=1800000    #限制重试时间，此处为毫秒，注意按需求换算
```
重新启动MySQL（根据版本选择重启命令）
```
service mysqld restart 或 service mysql restart
```
4、重新登录数据库，查看配置是否生效
```
mysql -uroot -p
show variables like '%connection_control%';
```
5、验证

输错5次密码后，会发现第6次登录会卡住，限制登录，时间为设定的限制时间30分钟

### 进行远程管理时，鉴别信息以明文方式进行传输。

mysql开启ssl

[https://blog.csdn.net/weixin_39845407/article/details/81708230]

询问核查通过什么管理工具连接数据库，查询此连接工具是否具备远程连接加密措施
注；MySQL自己支持使用ssl协议对连接进行加密，相关参数有have_openssl、have_ssl，执行

show global variables like '%ssl%';
为YES则代表数据库支持SSL连接。
如果某连接使用了SSL，使用status可以查看到，使用SSL需要运行mysql_ssl_rsa_setup

### 未开启审计功能，不能对重要的用户行为和重要安全事件进行审计。

```
// 先执行sql指令：
show variables like '%log%';
// 如果发现general_log为off，则使用下一句
set global general_log = ON;
```
永久修改需要在my.cnf的【mysqld】中添加：general_log = 1
