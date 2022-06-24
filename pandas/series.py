
import numpy as np
import pandas as pd

#ser = pd.Series([0,1,2,3], index= ['a','b','c','d'])
#print(ser)

dist_test = {
    'one': 'F',
    'two': 'E',
    'three': 'D',
    'four': 'C',
    'five': 'B',
    'six': 'A'
}


dist_test_pl = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6
}

print()

ser = pd.Series(dist_test_pl)
ser2 = pd.Series(dist_test)


print(ser2)


data_fr = pd.DataFrame({'jeden':ser, 'dwa': ser2})


print("\ndata frame info:")
print(data_fr.T)

print('good grades:')
print(data_fr[data_fr['jeden'] >= 3])

data_fr2 = pd.DataFrame([{'aa': 5}, {'bb':10}])
data_fr2.fillna(0x0)

print(data_fr2)

print("\n")
seriess = pd.Series(['a','b','c'], index= [0,1,5])
print(seriess.loc[0:3])

#loc explicit
#iloc implicit



