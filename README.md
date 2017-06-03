# Rockabye

作者：李昌武
博客地址：
http://www.cnblogs.com/lixiaoliuer/p/6936692.html

有感
第一次听alex讲堡垒机的时候确实有点懵，完全不知道讲的是什么。写代码的时候，参考alex的代码也显得很杂乱无章，文件非常多，但有的文件却只有很少的一部分代码，再在不同文件间切换很是头疼。后来又找了别人的代码，参考着别人的代码，然后对着alex给的需求，遇到有疑问的地方再看视频，就很意外的能搞懂alex在视频里面讲的内容了。


程序功能

1) 每个用户登陆堡垒机后,只需要选择具体要访问的主机地址,就可以连接上,不需要输入机器访问密码
2) 允许设置用户对不同目标设备的不同访问权限
3) 用户权限分组管理 允许用户批量拥有主机组所有主机权限 也可只拥有其中几台主机权限
4) 用户操作日志记录在数据库中 格式：[时间 + 用户名 + 主机 + 命令]


目录结构

├── bin                         # 程序入口目录
│   ├── Manager.py              # 管理员初始化数据库程序
│   └── main.py                 # 堡垒机入口程序
├── conf
│   └── setting.py              # 配置文件
├── db
│   ├── new_fort_user.yml       # 新建堡垒机用户模板
│   ├── new_group.yml           # 新建主机组模板
│   ├── new_host_user.yml       # 新建主机用户模板
│   └── new_host.yml            # 新建主机模板
└── moudles
    ├── db_conn.py              # 数据库结构创建
    ├── modules.py              # 堡垒机主函数
    └── views.py                # 调用模板文件插入数据

使用说明

1) conf/setting 文件设置数据库
2) 根据模板文件新建数据库数据
3) 管理员运行/bin/Manager.py进行一键初始化数据库
   (注意：初始化数据库会清空日志 需要备份)
4) 运行main.py文件


测试环境说明：
OS:Windows 7 旗舰版 Linux
Python:Python 3.6.0 
模块：sqlalchemy yaml paramiko
mysql版本：mysql-5.6.17-winx64
PyCharm版本：PyCharm 2016.1.3





