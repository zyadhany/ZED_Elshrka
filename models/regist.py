class Regist(BaseModel, Base):
    __tablename__ = 'regist'
    user_handle = Column(String(64), ForeignKey('accounts.handle'), primary_key=True)
    contest_id = Column(Integer, ForeignKey('contests.id'), primary_key=True)