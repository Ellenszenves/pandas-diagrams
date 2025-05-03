import pandas as pd
import matplotlib.pyplot as plt
import requests
import csv
import seaborn as sns

def download():
    """downloading data"""
    url = 'https://www.ksh.hu/stadat_files/nep/hu/nep0001.csv'
    response = requests.get(url)
    file_path = 'nepesseg.csv'
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print('Sikeres letöltés!')
    else:
        print('Letöltés nem sikerült!')
    clear_data()

def clear_data():
    """clearing data"""
    year = []
    total = []
    male = []
    woman = []
    with open('nepesseg.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        i = 0
        for row in spamreader:
            if i == 1:
                for column in row:
                    if column.isnumeric():
                        year.append(column)
            elif i == 3:
                for column in row:
                    if column != "férfi":
                        male.append(column.replace(" ", ""))
            elif i == 4:
                for column in row:
                    if column != "nő":
                        woman.append(column.replace(" ", ""))
            elif i == 5:
                for column in row:
                    if column != "összesen":
                        total.append(column.replace(" ", ""))
            i += 1
    dict = {'year': year, 'male': male, 'woman': woman,'total': total}
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('tisztitott_nepesseg.csv', header=True, index=False)
    
def analyze():
    """statistics"""
    df = pd.read_csv('tisztitott_nepesseg.csv')
    print(df.head())
    print(df.corr())

def line_diagram():
    """creating line-diagram"""
    df = pd.read_csv('tisztitott_nepesseg.csv')
    df.plot.line(x = 'year')
    plt.title("Teljes népesség alakulása + nemek szerinti változás")
    plt.show()

def dot_diagram():
    """creating dot diagram"""
    df = pd.read_csv('tisztitott_nepesseg.csv')
    sns.lmplot(x='year',y='total',data=df,fit_reg=True) 
    plt.title("Teljes népesség alakulása/lineáris regresszió")
    plt.show()

def main_menu():
    """interactive menu"""
    print("Hello! Funkciók:\n 1. Letöltés\n 2. Tisztítás\n 3. Statisztika\n 4. Pont-diagram\n 5. Vonal-diagram\n 6. Kilépés")
    func = input("Kívánt funkció: ")
    if func == "1":
        download()
    elif func == "2":
        clear_data()
    elif func == "3":
        analyze()
    elif func == "4":
        dot_diagram()
    elif func == "5":
        line_diagram()
    elif func == "6":
        print("Bye!")
        exit
    else:
        print("Ilyen funkció nem létezik.")
        main_menu()

main_menu()