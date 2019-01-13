import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/shwars/PythonJump/master/Data/climat_russia_cities.csv")
print(data)

data.columns=["City","Lat","Long","TempMin","TempColdest","AvgAnnual","TempWarmest","AbsMax","Precipitation"]

print(data.dtypes)
for x in ["TempMin","TempColdest","AvgAnnual"]:
    data[x] = data[x].str.replace('−','-')
    data = data.apply(pd.to_numeric,errors='ignore')
    print(data.dtypes)

ax = data.plot(x="Lat",y="AvgAnnual",kind="Scatter")
ax.set_xlabel("Широта")
ax.set_ylabel("Среднегодовая температура")

plt.show()

ax=data.plot(x="TempMin",y="AbsMax",kind="scatter")
ax.set_xlabel("Рекорд отрицательной температуры")
ax.set_ylabel("Рекорд положительной температуры")
ax.invert_xaxis()
plt.show()

data['spread'] = data['TempWarmest'] - data['TempColdest']
data.nlargest(3,'spread')
plt.show()


import geopy.distance

msk_coords = tuple(data.loc[data["City"]=="Москва"][["Lat","Long"]].iloc[0])
data["DistMsk"] = data.apply(lambda row : geopy.distance.distance(msk_coords,(row["Lat"],row["Long"])).km,axis=1)
data.head()

msk = data.loc[data['DistMsk']<300]
print(msk)

ax=msk.plot(x="City",y=["TempColdest","AvgAnnual","TempWarmest"],kind="bar",stacked="true")
ax.legend(["Мин","Сред","Макс"],loc='lower right')
plt.show()
