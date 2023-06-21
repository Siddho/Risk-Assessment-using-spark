import random   
N = 1000000 
Points_incircle = 0 

for i in range(N):
   
    x= random.uniform(-0.5, 0.5)
    y= random.uniform(-0.5, 0.5)
  
  
    if (x**2 + y**2)<= 0.25:
        Points_incircle+= 1 
  
    pi = 4* Points_incircle/N
print("Approximate value of Pi is ", pi)    
conda install pyspark
try:
    from pyspark import SparkContext, SparkConfc
    from pyspark.sql import SparkSession
except ImportError as e:
    printmd('<<<<<!!!!! Please restart your kernel after installing Apache Spark !!!!!>>>>>')
sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))

spark = SparkSession \
    .builder \
    .getOrCreate()
INITIAL_CAPITAL = 10  
MAXTIME = 10         
INCOME_INTENSITY = 1  
CLAIM_INTENSITY = 1   
CLAIM_MEAN = 1       
TRAJEC_NUM = 1000      
import random
import time
from operator import add

def bankrupcy(seed):
    random.seed(seed)
    capital = INITIAL_CAPITAL
    time = 0
    while (time < MAXTIME)and(capital>=0):
      time_step=random.expovariate(CLAIM_INTENSITY)
      time+=time_step
      capital += INCOME_INTENSITY * time_step - random.expovariate(1/CLAIM_MEAN)
    if (capital<0):
      return 1 
    else: 
      return 0
ruin_probability =sc.parallelize([time.time() + i for i in range(TRAJEC_NUM)]).map(bankrupcy).reduce(add)/TRAJEC_NUM
print("Our company will bunkrupt with", ruin_probability, "probability")
