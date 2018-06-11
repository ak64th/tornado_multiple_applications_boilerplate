from tornado.web import Application

from example import settings
from example.db import session_factory
from . import models
from . import views

models.Base.metadata.create_all(session_factory.engine)

application = Application(
    [
        (r'/auth/', views.MainHandler)
    ],
    session_factory=session_factory,
    debug=settings.DEBUG
)
