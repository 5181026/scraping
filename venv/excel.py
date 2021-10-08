import os
import openpyxl
import pprint

class Excel:
    # file_path = ""
    # wb = ""
    # sheet_name = "test"

    def __init__(self):
        self.file_path = ""
        self.wb = ""
        self.sheet_name = "test"
        print("コンストラクタ")
        self.file_path = "C:/excel_test/test.xlsx"



    def create_xlsx_file(self):
        if not os.path.exists(self.file_path):
            wb = openpyxl.Workbook()    #excelファイルの作成
            sheet = wb.active           #シートを作成
            sheet.title = self.sheet_name        #シートにタイトルをつける
            wb.save(self.file_path)          #ファイルを保存する
            print("ファイルを作成しました")

    # excelファイルに書き込む
    def xlsx_writer(self,search_keyword,site_dict):
        wb = openpyxl.load_workbook(self.file_path)
        sheet = wb[self.sheet_name]
        sheet.cell(row=1, column=1).value = "検索キーワード"
        sheet.cell(row=1, column=2).value = search_keyword
        sheet.cell(row=2 , column=1).value = "ランキング"
        sheet.cell(row=2 , column=2).value = "タイトル"
        sheet.cell(row=2 , column=3).value = "URL"
        sheet.cell(row=2, column=4).value = "h1"
        sheet.cell(row=2, column=5).value = "検出キーワード数"
        for i in site_dict.keys():
            j = 5
            sheet.cell(row=i + 2 , column=1).value = i #keyの値は1から始まるそのためi+2になっている
            sheet.cell(row=i + 2 , column=2).value = site_dict[i]["title"]
            sheet.cell(row=i + 2 , column=3).value = site_dict[i]["url"]
            sheet.cell(row=i + 2, column=4).value = site_dict[i]["h1"]

            for word in site_dict[i]["keyword"].keys():
                sheet.cell(row=i + 2, column=j).value = word + " : " + str(site_dict[i]["keyword"][word])
                j += 1
        wb.save(self.file_path)
