from ninja import Schema

class SequenceOut(Schema):
    id: int
    value: int


class SequenceIn(Schema):
    value: int