class Join(BaseModel, Base):
    __tablename__ = 'join'
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    user_handle = Column(String(64), ForeignKey('accounts.handle'), primary_key=True)