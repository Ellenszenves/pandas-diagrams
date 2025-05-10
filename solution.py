import pandas as pd
import matplotlib.pyplot as plt
import requests
import csv
import seaborn as sns
import tkinter as tk

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
    #print(df)
    df.to_csv('tisztitott_nepesseg.csv', header=True, index=False)
    
def analyze():
    """statistics"""
    df = pd.read_csv('tisztitott_nepesseg.csv')
    print(df.head())
    print(df.corr())

def analyze_win():
    """GUI statistics"""
    df = pd.read_csv('tisztitott_nepesseg.csv')
    stat_window = tk.Toplevel()
    stat_window.title("Népesség Analizátor")
    text_widget = tk.Text(stat_window, width=60, height=15)
    text_widget.pack(padx=10, pady=10)
    text_widget.insert(tk.END, df.to_string(index=False))

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

def window_mode():
    """Creating GUI"""
    #Ablak
    window = tk.Tk()
    window.title("Népesség Analizátor")
    window.geometry("250x300")
    label = tk.Label(window, text="Nyomjon meg egy gombot!", font=("Arial", 14))
    label.pack(pady=10)
    #Gombok
    download_button = tk.Button(window, text="Letöltés", command=download)
    download_button.pack(pady=5)
    clear_button = tk.Button(window, text="Tisztítás", command=clear_data)
    clear_button.pack(pady=5)
    analyze_button = tk.Button(window, text="Statisztika", command=analyze_win)
    analyze_button.pack(pady=5)
    dot_button = tk.Button(window, text="Pont-diagram", command=dot_diagram)
    dot_button.pack(pady=5)
    line_button = tk.Button(window, text="Vonal-diagram", command=line_diagram)
    line_button.pack(pady=5)
    exit_button = tk.Button(window, text="Kilépés", command=exit)
    exit_button.pack(pady=5)
    window.mainloop()

def main_menu():
    """interactive menu"""
    print("Hello! Funkciók:\n 1. Letöltés\n 2. Tisztítás\n 3. Statisztika\n 4. Pont-diagram\n 5. Vonal-diagram\n 6. Grafikus felület\n 7. Kilépés")
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
        window_mode()
    elif func == "7":
        print("Bye!")
        exit
    else:
        print("Ilyen funkció nem létezik.")
        main_menu()

main_menu()
