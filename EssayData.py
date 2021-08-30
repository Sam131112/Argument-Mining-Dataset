#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from string import punctuation
from collections import defaultdict
import pandas as pd
import os
import glob
import re


# In[ ]:


class ArguememtText():
    def __init__(self,seq1,annos):
        self.essay = seq1.replace('.',' .').split()
        self.annos = annos
        self.labels = ['O']*len(self.essay)
        self.arguments = defaultdict(tuple)
        self.edges = []
        self.mistakes = 0
        self.found = 0
    def get_id(self,args):
        args = args.replace('.',' .').split()
        #args = args.split()
        for i in range(len(self.essay)):
                target = self.essay[i:i+len(args)]
                if len(target)>0 and (target[-1][-1] == "," or target[-1][-1] == ";"):
                    #print(target)
                    target[-1] = target[-1].replace(target[-1][-1],'')
                if target == args:
                    self.labels[i:i+len(args)] = ['I-ARG']*len(args)
                    self.labels[i] = 'B-ARG'
                    return (i,i+len(args))
                    #print(self.essay[i:i+len(args)],args,self.labels)
                
    
    def fill_labels(self):
        for anno in self.annos: 
            anno = anno.rstrip('\n')
            anno = anno.split('\t')
            if 'T' in anno[0]:
                args = anno[-1]
                #print(args)
                outs = self.get_id(args)
                if outs == None:
                    self.mistakes=self.mistakes+1
                else:
                    self.found = self.found + 1
                    start, end = self.get_id(args)
                    self.arguments[anno[0]]=(start,end)
            if 'R' in anno[0]:
                #print(anno)
                t1,t2  = re.findall(r"Arg\d+:(.\d+)",anno[1])
                self.edges.append((t1,t2))
        print(self.mistakes,self.found)


# In[ ]:


df = pd.read_csv("ArgumentAnnotatedEssays-2.0/train-test-split.csv",delimiter=";")


# In[ ]:


for i,k in df.iterrows():
    print(i,k['ID'],k['SET'])
    if k['SET'] == 'TRAIN':
        os.system(f"cp ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}* ArgumentAnnotatedEssays-2.0/train_set/.")
    else:
        os.system(f"cp ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}* ArgumentAnnotatedEssays-2.0/test_set/.")
        
        
        


# In[ ]:


#glob.glob("ArgumentAnnotatedEssays-2.0/train_set/*")


# In[ ]:


train_objects = []
test_objects = []
for i,k in df.iterrows():
            print(k['ID'])
            f1 = open(f"ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}.txt",'r')
            f2 = open(f"ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}.ann",'r')
            txt = []
            for x in f1.readlines():
                x=x.strip('\n')
                txt.append(x)
            txt1 = ' '.join(txt)
            anno = f2.readlines()
            compare = ArguememtText(txt1,anno)
            compare.fill_labels()
            if k['SET'] == 'TRAIN':
                train_objects.append(compare)
            else:
                test_objects.append(compare)


# In[ ]:





# In[ ]:





# In[ ]:


compare.arguments


# In[ ]:


compare.edges


# In[ ]:


f = open('train.txt','w')

for obj in train_objects:
    text = obj.essay
    labels = obj.labels
    for (i,j) in zip(text,labels):
        f.write(i+'\t'+j+'\n')
    f.write('\n')


# In[ ]:


f = open('test.txt','w')

for obj in test_objects:
    text = obj.essay
    labels = obj.labels
    for (i,j) in zip(text,labels):
        f.write(i+'\t'+j+'\n')
    f.write('\n')


# In[ ]:


#train_objects[3].essay


# In[ ]:


import datasets


# In[ ]:


from datasets import load_dataset


# In[ ]:


data = load_dataset("Sam2021/Arguement_Mining_CL2017")


# In[ ]:





# In[ ]:




