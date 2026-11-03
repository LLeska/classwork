import pandas as pd
import matplotlib.pyplot as plt
mode = 0
while mode not in range(1, 4):
    try:
        mode = int(input("Choose task\n 1 - Transactions\n 2 - Flights\n 3 - Students\n"))
        if mode not in range(1, 4):
            print("incorrect number, try again")
    except ValueError:
        print("incorrect number, try again")
if mode == 1:
    trans = pd.read_csv("data/transactions.csv")
    pay = trans[trans["STATUS"] == "OK"]
    print("3 largest payments:")
    print(pay.nlargest(3, "SUM")[["CONTRACTOR", "SUM"]].to_string(index=False))
    umbrella = pay[pay["CONTRACTOR"] == "Umbrella, Inc"]
    print("\nUmbrella, Inc total:", umbrella["SUM"].sum())
elif mode == 2:
    data = pd.read_csv("data/flights.csv")
    flights = data.groupby("CARGO").agg(
        FLIGHTS=("CARGO", "size"),
        PRICE=("PRICE", "sum"),
        WEIGHT=("WEIGHT", "sum")
    )
    print(flights)
    titles = ["Number of flights", "Total cargo price", "Total cargo weight"]
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
    for i, column in enumerate(["FLIGHTS", "PRICE", "WEIGHT"]):
        axs[i].bar(flights.index, flights[column])
        axs[i].set_title(titles[i])
        axs[i].grid(True, axis="y")
        axs[i].set_axisbelow(True)
    plt.show()
elif mode == 3:
    groups = pd.read_excel("data/students/students_info.xlsx")
    ejudge = pd.read_html("data/students/results_ejudge.html")[0]
    empty = groups["login"].isna().sum()
    groups = groups.dropna(subset=["login"])
    students = groups.merge(ejudge, left_on="login", right_on="User")
    faculty = students.groupby("group_faculty")["Solved"].mean()
    informatics = students.groupby("group_out")["Solved"].mean()
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(9, 7))
    for i, data in enumerate([faculty, informatics]):
        axs[i].bar(data.index.astype(str), data.values)
        axs[i].set_title(["Average solved per faculty group", "Average solved per informatics group"][i])
        axs[i].set_ylabel("Average solved")
        axs[i].grid(True, axis="y")
        axs[i].set_axisbelow(True)
    plt.subplots_adjust(hspace=0.8)
    plt.show()
    special = students[(students["G"] > 10) | (students["H"] > 10)]
    print("\nStudents with G > 10 or H > 10:")
    print(special[["login", "group_faculty", "group_out", "G", "H"]].to_string(index=False))
    print("\nNumber of students per group pair:")
    print(special.groupby(["group_faculty", "group_out"]).size())
    print("Total:", len(special))
    print("\nEmpty rows in xlsx:", empty)
    print("Logins only in ejudge:", (~ejudge["User"].isin(groups["login"])).sum())