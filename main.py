import time  # スリープを使うために必要
import chromedriver_binary  # パスを通すためのコード
import requests
from excel import Excel
from selenium import webdriver  # Webブラウザを自動操作する（python -m pip install selenium)
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

search_str = "Wi-Fi"  # 検索文字列
# TODO 辞書で細かく分けることで分析できる
# keyをranking(int)
# value
#   title辞書型
#   url辞書型
#   keyword辞書keywordの中をさらに単語ごとの辞書にする
site_dict = {}  # 値を保持するための辞書

# chromeを使用して情報収集(タイトル,URL)
driver = webdriver.Chrome()
# サンプルのHTMLを開く
driver.get('https://www.google.com/')  # Googleを開く


# chromeで検索した結果からタイトルとURLを取得する
# TODO 現在は表示のみをするようになっている、ファイルなどに保存する機能に変更する
def result():
    # タイトルとリンクはclass="yuRUbf"に入っている
    class_group = driver.find_elements_by_class_name('yuRUbf')
    for i in range(3):
        print("ループ")
        print(i)
        site_dict[i + 1] = {
            "title": class_group[i].find_element_by_class_name('LC20lb').text,  # タイトル(class="LC20lb")
            "url": class_group[i].find_element_by_tag_name("a").get_attribute("href")  # リンク(aタグのhref属性)
        }


# TODO h1がないサイトが存在すアプリが落ちる
def scraping():
    for u in site_dict.keys():
        response = requests.get(site_dict[u]["url"])
        soup = BeautifulSoup(response.text, 'html.parser')
        # str_conut_dict.update(string_count(soup.text))
        site_dict[u]["keyword"] = (string_count(soup.text)) #キーワードは辞書で保持することで複数の文字を保持できるようにする
        site_dict[u]["h1"] = soup.find('h1').get_text()


# 関数としては機能しているが完全一致した文字列のみを取得する。
# 例：wifi,Wi-Fi
# 上記のだとサイトごとに個数が違う
# TODO 現在はサイトごとにとれないようになっている,サイトごとにとれるようにする
def string_count(html_text):
    return {search_str: html_text.count(search_str)}


search = driver.find_element_by_name('q')  # HTML内で検索ボックス(name='q')を指定する
search.send_keys(search_str)  # 検索ワードを送信する
search.submit()  # 検索を実行
time.sleep(3)

result()
scraping()
driver.quit()                               # ブラウザを閉じる

excel = Excel()
excel.create_xlsx_file()
excel.xlsx_writer(search_str , site_dict)

print("辞書")
print(site_dict)



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
