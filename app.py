from flask import Flask
import config
from flask_restful import Api,Resource,fields,marshal_with
from exts import db
from models import  User,Article,Tag
from articleviews import article_bp

app = Flask(__name__)
app.config.from_object(config)
# api = Api(app)
db.init_app(app)
app.register_blueprint(article_bp )




# class Article(object):
#     def __init__(self,title,content):
#         self.title=title
#         self.content = content
#
# article = Article(title='abc1',content='xx111')
#
# class ArticleView(Resource):
#
#     resource_fields={
#         'title':fields.String,
#         'content':fields.String
#     }
#
#     #     # restful规范中，要求，定义好了返回的参数
#     #     # 即使这个参数没有值，也应该返回，返回一个None回去
#
#     @marshal_with(resource_fields)
#     def get(self):
#         return article
#
#
# api.add_resource(ArticleView,'/article/',endpoint='article')


#
# class Article(object):
#     def __init__(self,title,content):
#         self.title=title
#         self.content = content
#
# article = Article(title='abc1',content='xx111')

# class ArticleView(Resource):
#
#     resource_fields={
#         'title':fields.String(attribute='title'),
#         'content':fields.String,
#         'author':fields.Nested({
#             'username':fields.String,
#             'email':fields.String
#         }),
#         'tags':fields.List(fields.Nested({
#             'id':fields.Integer,
#             'name':fields.String
#         })),
#         "read_count":fields.Integer(default=80)
#
#     }
#
#     #     # restful规范中，要求，定义好了返回的参数
#     #     # 即使这个参数没有值，也应该返回，返回一个None回去
#
#     @marshal_with(resource_fields)
#     def get(self,article_id):
#         article = Article.query.get(article_id)
#         return article
#
#
# api.add_resource(ArticleView,'/article/<article_id>/',endpoint='article')


@app.route('/')
def hello_world():
    user = User(username='zhiliao', email='xxx@qq.com')
    article = Article(title='abc', content='123')
    article.author = user
    tag1 = Tag(name='前端')
    tag2 = Tag(name='Python')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


"""
流程:
1.首先创建数据库
mysql> create database flask_restful_demo charset utf8;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+-----------------------+
| Database              |
+-----------------------+
| information_schema    |
| alembic_demo          |
| flask_alembic_demo    |
| flask_migrate_demo    |
| flask_restful_demo    |
| flask_script_demo     |
| flask_sqlalchemy_demo |
| icbc_demo             |
| mysql                 |
| performance_schema    |
| sys                   |
+-----------------------+
11 rows in set (0.00 sec)

mysql> use flask_restful_demo;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------------+
| Tables_in_flask_restful_demo |
+------------------------------+
| alembic_version              |
| article                      |
| article_tag                  |
| tag                          |
| user                         |
+------------------------------+
5 rows in set (0.00 sec)

mysql> select * from tag;
+----+--------+
| id | name   |
+----+--------+
|  1 | 前端   |
|  2 | Python |
+----+--------+
2 rows in set (0.00 sec)

mysql> select * from user;
+----+----------+------------+
| id | username | email      |
+----+----------+------------+
|  1 | zhiliao  | xxx@qq.com |
+----+----------+------------+
1 row in set (0.00 sec)

mysql> select * from article;
+----+-------+---------+-----------+
| id | title | content | author_id |
+----+-------+---------+-----------+
|  1 | abc   | 123     |         1 |
+----+-------+---------+-----------+
1 row in set (0.00 sec)
----------------------------------------
----------------------------------------
----------------------------------------
2.运行此程序
3.进入虚拟环境:
(my_env) $pwd
/Users/mac/PycharmProjects/flask_restful_demo2
(my_env) $ls
app.py		config.py	exts.py		manage.py	models.py	static		templates
(my_env) $python3 manage.py db init
  Creating directory /Users/mac/PycharmProjects/flask_restful_demo2/migrations ...  done
  Creating directory /Users/mac/PycharmProjects/flask_restful_demo2/migrations/versions ...  done
  Generating /Users/mac/PycharmProjects/flask_restful_demo2/migrations/script.py.mako ...  done
  Generating /Users/mac/PycharmProjects/flask_restful_demo2/migrations/env.py ...  done
  Generating /Users/mac/PycharmProjects/flask_restful_demo2/migrations/README ...  done
  Generating /Users/mac/PycharmProjects/flask_restful_demo2/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/mac/PycharmProjects/flask_restful_demo2/migrations/alembic.ini' before proceeding.
(my_env) $python3 manage.py db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'tag'
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added table 'article'
INFO  [alembic.autogenerate.compare] Detected added table 'article_tag'
  Generating /Users/mac/PycharmProjects/flask_restful_demo2/migrations/versions/25e51d73a3b6_.py ...  done
(my_env) $python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 25e51d73a3b6, empty message



"""