# Ngô Thu Thảo 20216960
import pandas as pd
import logging


def find_book(keyword):
    """
    Tìm sách theo mã sách, tên sách hoặc số ISBN
    :param keyword:
    :return: index của sách trong file dữ liệu
    """
    df = dataframe()

    for i, row in df.iterrows():
        if keyword in [str(row['Mã sách']), row['Tên sách'], row['Số ISBN']]:
            return i

    return -1


def is_book_id_exists(book_id):
    """
    Kiểm tra xem sách đã có trong thư viện hay chưa
    :param book_id: mã sách
    :return:
    """
    df = dataframe()

    return book_id in df['Mã sách'].values


def dataframe():
    """
    Lấy dữ liệu từ file excel
    :return:
    """
    try:
        df = pd.read_excel('book.xlsx')
        return df
    except FileNotFoundError:
        logging.warning("Không tìm thấy file Excel. Vui lòng kiểm tra lại đường dẫn.")
        return False
