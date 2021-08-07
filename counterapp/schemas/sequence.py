from ninja import Schema

class SequenceOut(Schema):
    id: int
    current: int


class SequenceIn(Schema):
    current: int