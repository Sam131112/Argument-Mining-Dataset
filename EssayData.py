#!/usr/bin/env python
# coding: utf-8

# In[260]:


from string import punctuation
from collections import defaultdict
import pandas as pd
import os
import glob


# In[265]:


class ArguememtText():
    def __init__(self,seq1,annos):
        self.essay = seq1.replace('.',' .').split()
        self.annos = annos
        self.labels = ['O']*len(self.essay)
    def get_id(self,args):
        args = args.split()
        for i in range(len(self.essay)):
                if self.essay[i:i+len(args)] == args:
                    self.labels[i:i+len(args)] = ['Arg_I']*len(args)
                    self.labels[i] = 'Arg_B'
                    print(self.essay[i:i+len(args)],args,self.labels)
    
    def fill_labels(self):
        for anno in self.annos: 
            anno = anno.split('\t')
            if 'T' in anno[0]:
                start , end  = int(anno[1].split()[1]),int(anno[1].split()[2])
                args = anno[2].strip('\n')
                print(args)
                self.get_id(args)


# In[246]:


df = pd.read_csv("ArgumentAnnotatedEssays-2.0/train-test-split.csv",delimiter=";")


# In[ ]:


for i,k in df.iterrows():
    print(i,k['ID'],k['SET'])
    if k['SET'] == 'TRAIN':
        os.system(f"cp ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}* ArgumentAnnotatedEssays-2.0/train_set/.")
    else:
        os.system(f"cp ArgumentAnnotatedEssays-2.0/brat-project-final/{k['ID']}* ArgumentAnnotatedEssays-2.0/test_set/.")
        
        
        


# In[276]:


#glob.glob("ArgumentAnnotatedEssays-2.0/train_set/*")


# In[ ]:


train_objects = []
test_objects = []
for i,k in df.iterrows():
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


# In[269]:


len(train_objects)


# In[270]:


len(test_objects)


# In[278]:


train_objects[0].essay[85:95]


# In[277]:


train_objects[0].labels.index('Arg_B')


# In[275]:


train_objects[0].annos


# In[280]:


f = open('train.txt','w')

for obj in train_objects:
    text = obj.essay
    labels = obj.labels
    for (i,j) in zip(text,labels):
        f.write(i+'\t'+j+'\n')
    f.write('\n')


# In[281]:


f = open('test.txt','w')

for obj in test_objects:
    text = obj.essay
    labels = obj.labels
    for (i,j) in zip(text,labels):
        f.write(i+'\t'+j+'\n')
    f.write('\n')


# In[312]:


#train_objects[3].essay


# In[288]:


import datasets


# In[294]:


from datasets import load_dataset


# In[310]:


data = load_dataset("Sam2021/Arguement_Mining_CL2017")


# In[ ]:





# In[ ]:




