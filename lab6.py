with open("data.csv") as f:
    survivedC=0
    notSurvivedC=0
    survivedQ=0
    notSurvivedQ=0
    survivedS=0
    notSurvivedS=0
    next(f)
    for line in f:
        data = line.split(",")
        isSurvived = data[1]
        port=data[12].strip()
        if port=="C":
            if isSurvived=="1":
                survivedC+=1
            else:
                notSurvivedC+=1
        if port=="Q":
            if isSurvived=="1":
                survivedQ+=1
            else:
                notSurvivedQ+=1
        if port=="S":
            if isSurvived=="1":
                survivedS+=1
            else:
                notSurvivedS+=1
        
    print(f"Спасённых/погибших в порту Шербура: {survivedC}/{notSurvivedC}")
    print(f"Спасённых/погибших в порту Квинстоуна: {survivedQ}/{notSurvivedQ}")
    print(f"Спасённых/погибших в порту Саутгемптона: {survivedS}/{notSurvivedS}")
    
    
            

