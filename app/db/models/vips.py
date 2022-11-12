from db.models.common import TimestampModel, UUIDModel


class Vip(TimestampModel, UUIDModel, table=True):
    __tablename__ = "vips"

    name: str
    age: int
    gender: str
    occupation: str

    def __repr__(self):
        return f"<Vip (id: {self.id})>"
