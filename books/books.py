from flask import Blueprint,jsonify,request,session
import pandas as pd
import json
import os
books_v1 = Blueprint('books',__name__)



def get_book_data():
    response_data={'books':[]}
    try:
        data = request.args.get('rows')
        if data is not None:
            file_path = os.getcwd()+'/books.csv'
            df = pd.read_csv(file_path)
            json_data = df.head(int(data)).to_dict('index')
            books_list=[]
            for booksData in json_data:
                books_list.append(json_data[booksData])
            response_data['books']=books_list
    except Exception as e:
        print(e)
    return response_data

def get_book_filter_data():
    response_data = {'books': []}
    try:
        data = request.get_json()
        file_path = os.getcwd() + '/books.csv'
        df = pd.read_csv(file_path)
        books_list=[]
        for keys in data:
            json_data = df[keys]==data[keys]
            books_data = df[json_data].to_dict('index')
            for filterData in books_data:
                books_list.append(books_data[filterData])
        response_data['books'] = books_list
    except Exception as e:
        print(e)
    return response_data


books_v1.add_url_rule('/get-book-data/','getBookData',get_book_data,methods=['GET'])
books_v1.add_url_rule('/get-book-filter-data/','getBookFilterData',get_book_filter_data,methods=['POST'])