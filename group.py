import pandas as pd
company=["A","B","C"]
data=pd.DataFrame({"company":[company[x] for x in np.random.randint(0,len(company),10)],
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)})