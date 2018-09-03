from app import db
from werkzeug.security import check_password_hash,generate_password_hash
from sqlalchemy.orm import class_mapper


# 后台用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))
    type = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('Error')

    @password.setter
    def password(self,password):
        print(password)
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        print(password)

        return check_password_hash(self.password_hash,password)

    def as_dict(obj):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        #上面的有缺陷，表字段和属性不一致会有问题
        return dict((col.name, getattr(obj, col.name)) \
                    for col in class_mapper(obj.__class__).mapped_table.c)

    # def __repr__(self):
    #     return  self

################### 以下为简单记事前台对象
#简单记事用户对象
# class jdUser(db.Model):
#     __tablename__ = 'jdusers'
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(64),unique=True)
#     password_hash = db.Column(db.String(128))
#     avatar = db.Column(db.String(128))
#     nickname = db.Column(db.String(128))
#
#     @property
#     def password(self):
#         raise AttributeError('Error')
#
#     @password.setter
#     def password(self,password):
#         print(password)
#         self.password_hash = generate_password_hash(password)
#
#     def verify_password(self,password):
#         print(password)
#
#         return check_password_hash(self.password_hash,password)
#
#     def as_dict(obj):
#         # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#         #上面的有缺陷，表字段和属性不一致会有问题
#         return dict((col.name, getattr(obj, col.name)) \
#                     for col in class_mapper(obj.__class__).mapped_table.c)
