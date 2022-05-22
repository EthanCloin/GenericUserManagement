from user_two import UserTwo
from base import Session, engine, Base

Base.metadata.create_all(engine)
session = Session()

u1 = UserTwo('email1@email.com', 'security', "myuser")
u2 = UserTwo('another@mail.com', 'mmsecurity')

# session.add(u1)
# session.add(u2)\

# session.commit()
session.close()
