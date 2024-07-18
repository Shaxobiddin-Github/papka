import csv
file=open("C:\\Users\\As\\Desktop\\3-oy\\9-dars\\users.csv","r")
class LoadCsv:
    def __init__(self,file_name) -> None:
        self.file_name=file_name

    def info(self):
        csv_file=csv.reader(self.file_name,delimiter=",")
        for row in self.file_name:
            print(row)

obj=LoadCsv(file)
obj.info()
