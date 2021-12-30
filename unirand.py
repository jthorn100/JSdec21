import random
import csv
ls = []


for i in range(200):
    ls.append(random.uniform(0,1))


f = open('uniform.csv','w')
writer = csv.writer(f)
writer.writerow(ls)
f.close()
