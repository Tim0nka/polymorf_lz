import pandas as pd


class DataSetting:
    def __init__(self):
        self.data = pd.read_csv('var2.csv')
        self.df = self.data.copy() 


    def __pos__(self):
        proverka1 = self.df.shape[0] 
        self.df = self.df.drop_duplicates()
        proverka2 = self.df.shape[0]
        deletion = proverka1 - proverka2
        print(f'В файле удалено дубликатов: {deletion}')


    def split(self):
        def1 = self.df[self.df['Тип операции'] == 'получение средств'] 
        def2 = self.df[self.df['Тип операции'] == 'списание средств']   
        

        def1.to_csv('poluchka.csv', index=False)
        def2.to_csv('potracheno.csv', index=False)


    def __del__(self):
        print('Выполненно')

