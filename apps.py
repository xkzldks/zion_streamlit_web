import streamlit as st
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://test:test@cluster1.9pincbb.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.dbstreamlit

d = list(db.chulseck.find({}, {'_id': False}))
d
view = [100,150,30]
st.write('# asdf')
st.write('## rasd')
view
st.write('bar')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview