class Blog(BaseModel, Base):
    __tablename__ = 'blogs'
    blog_id = Column(Integer, primary_key=True)
    user_handle = Column(String(64), ForeignKey('accounts.handle'))
    title = Column(String(128), nullable=False)
    contest = Column(String(128))
    date = Column(DateTime, nullable=False)