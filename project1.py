import pandas as pd
#read csv
df = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])
print("Number Of Rows:", df.__len__())
print("Column Names:", *df.columns)
print("Data Types:", df.dtypes)
print("Mean Fareheit Temperature:", df['TEMP'].mean())
print("SD of max tempearute:", df['MAX'].std())
print("Number of unique stations:", df['USAF'].unique())
print("----------ONE----------")
selected = pd.DataFrame({
    'USAF': list(df['USAF']), 'YR--MODAHRMN': list(df['YR--MODAHRMN']),'TEMP': list(df["TEMP"]), 'MAX': list(df['MAX']),'MIN': list(df['MIN'])})
n=selected.dropna(axis=0,how='any',subset=['TEMP'])
tc=[]
for i in n['TEMP']:
    tc.append((i-32)*5/9)
n['CELCIUS']=tc
li=[]
for i in n['CELCIUS']:
    li.append(round(i))
n['CELCIUS']=li
print('----------TWO----------')
kumpula=n[n['USAF']==29980]
rovaniemi=n[n['USAF']==28450]
kumpula.to_csv('Kumpula_temps_May_Aug_2017.csv',sep=',')
rovaniemi.to_csv('Rovaniemi_temps_May_Aug_2017.csv',sep=',')
print(kumpula)
print(rovaniemi)
print('----------THREE----------')
index=(kumpula.__len__())/2
print("The Median Temperature O Helsinki Kumpula :",list(kumpula['TEMP'])[int(index)])
index=(rovaniemi.__len__()+1)/2
print("The Median Temperature O Rovaniemi :",list(rovaniemi['TEMP'])[int(index)])
print('----------FOUR----------')
rovaniemi_may=rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201705]
kumpula_may=kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201705]
print(kumpula_may)
print(rovaniemi_may)
rovaniemi_june=rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201706]
kumpula_june=kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201706]
print(kumpula_june)
print(rovaniemi_june)
print('Mean Temperature Of Rovaniemi in MAY is :',rovaniemi_may['TEMP'].mean())
print('Mean Temperature Of Rovaniemi in JUNE is :',rovaniemi_june['TEMP'].mean())
print('Mean Temperature Of Kumpula in MAY is :',kumpula_may['TEMP'].mean())
print('Mean Temperature Of Kumpula JUNE is :',kumpula_june['TEMP'].mean())
print('Max Temperature Of Rovaniemi in MAY is :',rovaniemi_may['TEMP'].max())
print('Max Temperature Of Rovaniemi in JUNE is :',rovaniemi_june['TEMP'].max())
print('Max Temperature Of Kumpula in MAY is :',kumpula_may['TEMP'].max())
print('Max Temperature Of Kumpula in JUNE is :',kumpula_june['TEMP'].max())
print('Min Temperature Of Rovaniemi in MAY is :',rovaniemi_may['TEMP'].min())
print('Min Temperature Of Rovaniemi in JUNE is :',rovaniemi_june['TEMP'].min())
print('Min Temperature Of Kumpula in MAY is :',kumpula_may['TEMP'].min())
print('Min Temperature Of Kumpula in JUNE is :',kumpula_june['TEMP'].min())
print("Does there seem to be large difference in temperatures between the months?:->")
print("Yes, there is a large difference in temperatures between May and June i.e.,:",rovaniemi_june['TEMP'].mean()-rovaniemi_may['TEMP'].mean()," in Rovaniemi and difference of",kumpula_june['TEMP'].mean()-kumpula_may['TEMP'].mean(),"in Kumpula")
print("Is Rovaniemi much colder place than Kumpula?:->")
print("YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
w=[]
for i in selected['YR--MODAHRMN']:
    w.append(str(i)[0:10])
selected['YR--MODAHRMN']=w
g=selected.groupby('YR--MODAHRMN')
hmean=[]
hmax=[]
hmin=[]
for x,y in g:
    hmean.append(y['TEMP'].mean())
    hmax.append(y['TEMP'].max())
    hmin.append(y['TEMP'].min())
d=pd.DataFrame({
    'Mean':hmean,'Maximum':hmax,'Minimum':hmin
})
d.to_csv('Exercise.csv',index=False)


