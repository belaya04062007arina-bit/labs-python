pro= {
    "Яблоко":0.8, "Груша":1.19, "Сыр":5.7
}

min=float('inf')
nam=''
for i in pro:
    if pro[i]<min:
        min=pro[i]
        nam=i
print(nam, min)        