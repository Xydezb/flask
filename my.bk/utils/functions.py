from functools import wraps

from flask import session, redirect, url_for


def is_login(func):
    @wraps(func)
    def check():
        user_name = session.get('user_id')
        if user_name:
            return func()
        else:
            return redirect(url_for('back.home'))
    return check