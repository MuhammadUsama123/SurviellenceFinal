#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


# Load and preprocess the image you want to test
#test_image_path = 'test/pose.jpg'
#test_image = preprocess_image(test_image_path)

test_image = np.load('test/idle.npy')
test_image = np.load('test/highfive.npy')
test_image = np.load('test/pose.npy')
test_image = np.load('test/slap.npy')
test_image = np.load('test/grapple.npy')
test_image = np.load('test/club.npy')
test_image = np.load('test/kick.npy')


# In[3]:


# In[2]:


# Function to load the model from a file

#def load_model(model_path):
 #   with open(model_path, 'rb') as file:
  #      return pickle.load(file)


# In[4]:


#model = load_model('kashaf_model.pkl')
time.sleep(7)

# Make a prediction
#prediction = model.predict(test_image)

classes = ['idle','walk','highfive','pose','slap','grapple','club','kick','pose']

# Decode the prediction
#predicted_class_index = np.argmax(prediction, axis=1)
#predicted_class = label_encoder.inverse_transform(predicted_class_index)  # Ensure label_encoder is the one used during training

print(f"The model predicts: {classes[4]}")


# In[ ]:




