from base.com.vo.login_vo import *

class UserDAO:
    def insert_user_details(self, user_vo):
        database.session.add(user_vo)
        database.session.commit()