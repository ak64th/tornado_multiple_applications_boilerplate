from tornado_sqlalchemy import make_session_factory

from example import settings

session_factory = make_session_factory(
    settings.DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE
)
engine = session_factory.engine
