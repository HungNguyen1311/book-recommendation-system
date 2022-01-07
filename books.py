import pandas as pd
import numpy as np
dt=pd.read_csv("books1.csv",nrows=5000)
#Lua chon cac cot thuoc tinh can thiet
books_dt_image=['image_url','small_image_url']
books_name=dt[['book_id','title','original_title','language_code','authors','original_publication_year']]


rating_dt=pd.read_csv("ratings1.csv")
#gop 2 tap du lieu
books_dt=pd.merge(rating_dt,books_name,on='book_id')
#sap xep tap du lieu theo thu tu nguoi danh gia va chi so danh gia
ratings_mean_dt=pd.DataFrame(books_dt.groupby('title')['rating'].mean())
#tao cot thuoc tinh la so luot danh gia
ratings_mean_dt['rating_counts']=pd.DataFrame(books_dt.groupby('title')['rating'].count())

#Tao ma tran UxI
user_book_rating=books_dt.pivot_table(index='user_id',columns='title',values='rating')
def book_suggestions(tensach,rating,goiy):
  #Lay cac user co danh gia quyen sach muon tim goi y
  tensach_dt=user_book_rating[tensach]
  #Tinh do tuong tu giua cac quyen do cac nguoi dung danh gia va sach muon tim goi y
  book_tuongtu=user_book_rating.corrwith(tensach_dt)
  #dinh dang lai du lieu o dang pandas va gan ten cot gia tri tuong tu
  corr_tensach_dt=pd.DataFrame(book_tuongtu,columns=['Correlation'])
  
  #sap xep
  corr_tensach_dt.sort_values('Correlation',ascending=False).head(11)
  #Dinh dang lai du lieu pandas
  add_rating_count_dt=pd.DataFrame(corr_tensach_dt.groupby('title')['Correlation'].mean())
  
  add_rating_count_dt['rating_counts']=ratings_mean_dt['rating_counts'].astype(int)
  
  Rating_books_final=add_rating_count_dt[add_rating_count_dt['rating_counts']>rating].sort_values('Correlation',ascending=False).head(goiy)
  
  return Rating_books_final



