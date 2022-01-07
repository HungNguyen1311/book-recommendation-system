import streamlit as st
import pandas as pd
import numpy as np
from books import book_suggestions
# app title
dt=pd.read_csv("books1.csv",nrows=5000)

books_dt_image=['image_url','small_image_url']
books_name=dt[['book_id','title','original_title','language_code','authors','original_publication_year','image_url']]


rating_dt=pd.read_csv("ratings1.csv")

st.set_page_config(layout="wide")
st.title("Danh sách sách")

st.write(books_name['title'])

empty_text_search=st.empty()
empty_text_name=st.empty()
recommend_button=st.button("Gợi ý !!! ")
book_search = st.selectbox('NHẬP TÊN SÁCH MÀ BẠN MUỐN TÌM ',books_name['title'].values)
#st.write(option_movie_name)
search_button=st.button("Tìm Kiếm")
book_name=empty_text_name.text_input("Hãy nhập vào tên sách mà bạn muốn gợi ý")

#book_search=empty_text_search.text_input("Hãy nhập vào tên sách mà bạn muốn tìm")
def books_search(book_name):
    for i in range(0,len(books_name)):
        if book_search in books_name.iloc[i]['title']:
            st.write("Tên sách: ",books_name.iloc[i]['title'])
            st.write("Ngôn Ngữ: ",books_name.iloc[i]['language_code'])
            st.write("Tác giả: ", books_name.iloc[i]['authors'])
            st.write("Năm xuất bản: ",int(books_name.iloc[i]['original_publication_year']))
            st.image(books_name.iloc[i]['image_url'],width=170)     
            st.write("-------OoO--------")
            st.write("\n")
if search_button:
    st.write("Thông tin của sách: ")
    st.write(books_search(book_search))    
if recommend_button:
     array_book_name=[]
     array_image=[]
     array_author=[]
     st.write("Gợi ý sách dành cho "+book_name+" là:")
     a=book_suggestions(book_name,1000,11)
     a=a.drop(['rating_counts'], axis=1)
     for i in range(1,11):
      for j in range(0,len(books_name)):
        if a.iloc[i:i+1,i:i+1].index.values == books_name.iloc[j]['title']:
            array_book_name.append(books_name.iloc[j]['title'])
            array_image.append(books_name.iloc[j]['image_url'])
            array_author.append(books_name.iloc[j]['authors'])
     for k in range(0,10):
           stt=str(k+1)
           st.write("Quyển Sách Thứ " +stt+" :")
           st.write("Tên Sách: "+array_book_name[k])
           st.write("Tên Tác Giả: "+array_author[k])
           st.image(array_image[k],width=170)        