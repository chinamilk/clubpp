# 社团招新平台

## 主旨：
    为社团网上招新提供平台
## 使用架构：
    前后端分离，restful风格
## 核心技术：
    1. flask-restful(python3.5.2)
        flask restful 支持
        
    2. mariadb(version 15.1)
        数据库账号:
        用户: clubpp 密码: 123456sql
        
    3. supervisor
        进程管理工具

    4. nginx
        管理静态资源(图片等)

    5. Ubuntu(16.04LTS)
        部署环境
    
## 前后端交互Api设计：
- [点击这里](https://github.com/Rabbit-A512/clubpp).

## 项目结构组织：
    /app -- api         api请求映射
         -- dao         数据库交互
         -- resource    资源文件，配置文件
         -- test        测试
         -- util        常用功能函数集合
    （详情见各包__init__.py文件)
## 项目依赖管理
    使用以下命令生成当前项目依赖：
```
    pip freeze > dependency.txt
```
    
    
    使用以下命令导入文件所描述的依赖：
```
    pip install -r dependency.txt
```
    
    
    建议准备推送时，更新依赖文件
## 代码规范(参考)
1. [Python代码规范和命名规范](http://www.imooc.com/article/19184?block_id=tuijian_wz#child_5_1)
2. [Python 编码规范(Google)](http://www.runoob.com/w3cnote/google-python-styleguide.html)