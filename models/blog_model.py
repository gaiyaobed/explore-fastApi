# from sqlalchemy.orm import relationship
#
# from database import Base
# from sqlalchemy import Column, String, Integer, ForeignKey
#
#
# class Blog(Base):
#     __tablename__ = 'blogs'
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
#     # user_id = Column(Integer, ForeignKey("users.id"))
#     # creator = relationship("User", back_populates="blogs")
