import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('scamrates.csv')
print(df.tail())
rate = df["rate"]
print(rate.tail())
rate.hist()
plt.title('Scammer proposed daily growth rates')
plt.xlabel('Growth Rate (%)')
plt.ylabel('Frequency')
plt.show()




# how long to make 1,000,000 on an initial investment of 1,000
P = 1000
A = 1e6
num = np.log(A) - np.log(P)
den = np.log(1+rate/100)
D = num/den;
plt.plot(D)
plt.show()
print("mean",D.mean())
print("median",D.median())
print("mode",D.mode())

# how long to make 1,000,000 on an initial investment of 1,000
P = 1000
A = 1e9
num = np.log(A) - np.log(P)
den = np.log(1+rate/100)
D = num/den;
plt.plot(D)
plt.show()
print("mean",D.mean())
print("median",D.median())
print("mode",D.mode())
