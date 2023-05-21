
import pandas as pd

def get_sorted_excel_table() -> bytes:
    df = pd.read_excel('docs/last_month.xlsx') #, usecols=[0, 1, 2], nrows=10)
    data = df.to_dict()

    s=0
    keys = list(data.keys())
    for p, i in data[keys[0]].items():
        if "товар" in i.lower():
            s+=1
        # print(p)
    print(f'{s}/{len(data[keys[0]].values())}')

    print(data[keys[7]].values())
    # print(data["Кол-во товарны х карточек"].values())
    # print(data["% товарных карточек с продажам и (без учета неактивны"].values())
    
    # print(keys)



if __name__ == "__main__":
    get_sorted_excel_table()
    a = "80%"
    print(a[:-1])