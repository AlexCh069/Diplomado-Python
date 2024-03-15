# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 08:00:55 2024

@author: Dell
"""
"""
      BD. PYTHON
   - CONECTORES....mysql,sql server,oracle 
   - SQLITE........Python
   - ORM....Manejo de base de datos python ORIENTADO A OBJETOS sqlalquemy   
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bdejemplo.sqlite')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()