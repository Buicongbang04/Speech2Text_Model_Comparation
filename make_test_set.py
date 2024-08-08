import os
import numpy as np
import pandas as pd
import ast

# Prepocessing data
with open(r"script\labeled_medical_data_test_transcript.txt", "r", encoding="utf8") as test_r:
    test_scripts = test_r.read().replace("\n", "")
    test_scripts = ast.literal_eval(test_scripts)
    test_r.close()

with open(r"script\labeled_medical_data_train_transcript.txt", "r", encoding="utf8") as train_r:
    train_scripts = train_r.read().replace("\n", "")
    train_scripts = ast.literal_eval(train_scripts)
    train_r.close()
    
# Make testing data
valTest = []
valTrain = []
for i in range(len(test_scripts)):
    obj = dict()
    obj['text'] = test_scripts[i]['text']
    obj['file'] = os.path.splitext(test_scripts[i]['file'])[0]
    valTest.append(obj)

for i in range(len(train_scripts)):
    obj = dict()
    obj['text'] = train_scripts[i]['text']
    obj['file'] = os.path.splitext(train_scripts[i]['file'])[0]
    valTrain.append(obj)

# Generate audio for specific file path
for idx, test in enumerate(valTest):
  valTest[idx]['path'] = os.path.join('wav_test_audio/' + valTest[idx]['file']+'.wav' )

for idx, train in enumerate(valTrain):
  valTrain[idx]['path'] = os.path.join('wav_train_audio/' + valTrain[idx]['file']+'.wav' )
  
data = valTest + valTrain

# Save to file csv
df = pd.DataFrame(data)
df.to_csv('valTest.csv', index=False)