def compute(principal,rate,numYears,total):
    total = principal * (1+rate) ** numYears
    return total




print(compute(100,0.04,1,1))
