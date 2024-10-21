class Friend(BaseModel, Base):
    __tablename__ = 'friends'
    handle1 = Column(String(64), primary_key=True)
    handle2 = Column(String(64), primary_key=True)
