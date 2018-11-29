import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser(description = 'There is only one argument required to run this program, which is --path.\n\rYou can run this file with command like this in your command line:\n\rpython Yunze_Hao.py --path ./adult_age_gender_race_dataset.csv')
parser.add_argument('--path', required = True, type = str)
args = parser.parse_args()
print('----------------*Select * From R where Gender=1 and Race=2*----------------')
path=args.path
def DP(path,epsilon):
    with open (path,'r') as f:
        lines=f.readline()
        lines=f.readlines()
    list1=[]
    list2=[]
    list3=[]
    for line in lines:
        line=line[:-1]
        line=line.split(',')
        list1.append(line[0])
        list2.append(line[1])
        list3.append(line[2])
    list_1=sorted(list1)
    # let sensitivity/epsilon as beta, miu is zero.
    hit=[]
    for i in range(len(list1)):
        if int(list2[i])==1 and int(list3[i])==2:
            hit.append(i)
    ageran=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
    count1=[]
    for i in ageran:
        temp=0
        for each in hit:
            if i-5< int(list1[each]) <=i:
                temp+=1
        count1.append(temp)
    beta = 1/epsilon
    loc, scale = 0,beta
    s = np.random.laplace(loc, scale,len(ageran))
    count2=[]
    for i in range(len(count1)):
        count2.append(count1[i]+round(s[i]))
    error=0
    res=[]
    for each in s:
        res.append(round(each))
        error+=abs(round(each))
    return count2,error,res
i=0.1
errorlist=[]
while i <=1:
    plotlist,error,res=DP(path,i)
    errorlist.append(error)
    i+=0.1
index = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
rects=plt.bar(index, plotlist,width=1,label='noisy histogram_ϵ=1')
plt.legend()
plt.xlabel('age')
plt.ylabel('count')
plt.title(u'Select * From R where Gender=1 and Race=2')
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.show()
rects=plt.bar(index,res,width=1,label='noise when ϵ=1')
plt.legend()
plt.xlabel('age_bucket')
plt.ylabel('rounded noise')
plt.title(u'Select * From R where Gender=1 and Race=2')
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.show()
rects=plt.bar([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],errorlist,width=0.05,label='error')
plt.legend()
plt.xlabel('varying ϵ')
plt.ylabel('error')
plt.xlim(xmax=1,xmin=0)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.title(u'error vs. varying ϵ')
plt.show()