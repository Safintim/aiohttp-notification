from aiopg import sa
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


meta = MetaData()

device = Table(
    'fcm_django_fcmdevice',
    meta,
    Column('id', Integer, primary_key=True),
    Column('active', Boolean),
    Column('device_id', String(150)),
    Column('registration_id', Text),
    Column('type', String(10)),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE')),
)
