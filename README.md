# 社团招新平台

## 主旨：
    为社团网上招新提供平台
## 使用架构：
    前后端分离，restful风格
## 核心技术：
    flask-restful，mysql，supervisor，nagin, Ubuntu
## 前后端交互Api设计：
    [点击这里](https://github.com/Rabbit-A512/clubpp).
## 项目结构组织：
    /app -- api         api请求映射
         -- dao         数据库交互
         -- resource    资源文件，配置文件
         -- test        测试
         -- util        常用功能函数集合
    （详情见各包__init__.py文件)