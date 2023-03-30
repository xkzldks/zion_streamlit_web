import streamlit as st
<<<<<<< HEAD
import pandas as pd
from modules.data_query import DataQuery
from modules.utils import run_concurrent_queries, estimate_gigabytes_scanned
from modules.sql_queries import (
    QUERY_POLLUTION,
    QUERY_TEMPERATURE,
    QUERY_PRCP,
    NAMES_TO_CODES,
    STATES,
    YEARS,
)
from google.cloud import bigquery
from modules.plot import plot_pol, plot_temp, plot_prc
import urllib
=======
from pymongo import MongoClient
# client = pymongo.MongoClient("mongodb+srv://test:test@cluster1.9pincbb.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.dbstreamlit

d = list(db.chulseck.find({}, {'_id': False}))
d
>>>>>>> 53acc03d71ea2bfc82ee3512362cfa2769d2e9a3
view = [100,150,30]
st.write('# asdf')
st.write('## rasd')
view
st.write('bar')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview
