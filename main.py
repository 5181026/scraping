import time                            # スリープを使うために必要
import chromedriver_binary             # パスを通すためのコード
import requests
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
from bs4 import BeautifulSoup

search_str = "wifi" #検索文字列
# TODO 辞書で細かく分けることで分析できる
# result_dict = {}    #値を保持するための辞書
title = []
title2 = []

url = []

# chromeを使用して情報収集(タイトル,URL)
driver = webdriver.Chrome()
# サンプルのHTMLを開く
driver.get('https://www.google.com/')  # Googleを開く


# chromeで検索した結果からタイトルとURLを取得する
# TODO 現在は表示のみをするようになっている、ファイルなどに保存する機能に変更する
def result():
    # タイトルとリンクはclass="r"に入っている
    class_group = driver.find_elements_by_class_name('yuRUbf')
    for elem in class_group:
        title.append(elem.find_element_by_class_name('LC20lb').text)  # タイトル(class="LC20lb")
        url.append(elem.find_element_by_tag_name('a').get_attribute('href'))  # リンク(aタグのhref属性)

        # とりあえず３番目まで検索
        if elem == class_group[2]:
            break


def scraping():
    for u in url:
        response = requests.get(u)
        soup = BeautifulSoup(response.text, 'html.parser')
        title2.append(soup.find('title').get_text())


search = driver.find_element_by_name('q')  # HTML内で検索ボックス(name='q')を指定する
search.send_keys(search_str)  # 検索ワードを送信する
search.submit()  # 検索を実行
time.sleep(3)

result()
scraping()

driver.quit()                               # ブラウザを閉じる

print(title)
print(title2)



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
