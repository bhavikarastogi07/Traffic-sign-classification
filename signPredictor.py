#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tensorflow as tf


# In[13]:


import keras.models


# In[14]:


mymodel=tf.keras.models.load_model('my_model.h5')


# In[15]:


import pandas as pd


# In[16]:


f= pd.read_csv("traffic dataset/labels.csv")


# In[18]:


dict={}
f=f.values.tolist()


# In[19]:


for i in range(len(f)):
    dict[f[i][0]]=f[i][1]


# In[20]:


from keras.preprocessing import image


# In[21]:


def preprocess(img):
    img=image.load_img(img,target_size=(40,40))
    X=image.img_to_array(img)
    X=X/255.0
    X=X.reshape(-1,40,40,3)
    return X
    


# In[23]:


def predict_sign(image):
    X=preprocess(image)
    pred=mymodel.predict(X).argmax()
    pred=dict[pred]
    return pred


# In[ ]:




