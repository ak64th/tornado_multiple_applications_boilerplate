from tornado.gen import coroutine
from tornado_sqlalchemy import SessionMixin, as_future

from example.security import AuthRequestHandler
from .forms import LoginForm
from .models import App, User


class MainHandler(AuthRequestHandler):
    def get(self):
        self.write({'Hello': 'World'})


class LoginHandler(SessionMixin, AuthRequestHandler):
    @coroutine
    def post(self):
        with self.make_session() as session:
            form = LoginForm(self.request.arguments)
            if not form.validate():
                self.write(form.errors)
                self.finish()
            user = yield as_future(
                session.query(User, App).filter(
                    User.username == form.data['username'],
                    User.app_id == App.id,
                    App.key == form.data['app_key']
                ).first
            )
            if not (user and user.User.check_password(form.data['password'])):
                self.set_status(403)
                self.finish({'message': 'Incorrect password or username'})
            self.finish({'message': 'Success'})
