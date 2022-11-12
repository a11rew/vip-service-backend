from db.models.common import TimestampModel, UUIDModel


class User(TimestampModel, UUIDModel, table=True):
    __tablename__ = "users"

    first_name: str
    last_name: str
    email: str
    password: str

    def __repr__(self):
        return f"<User (id: {self.id})>"
