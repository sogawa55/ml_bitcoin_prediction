#　ビットコインの価格予測
# 先月の価格推移をもとに今月の推移を予測する
# 前日比で上昇を[1],下降を[0]と扱う

import numpy as np
import pandas as pd
from sklearn import tree,metrics,svm
from sklearn.ensemble import RandomForestClassifier

# 期間指定
Start_Index=0 
Last_Index=25

# CSVファイルの読み込み
def importData(file):
    csvfile=file
    btc_price = pd.read_csv(csvfile)
    data=np.array(btc_price['Close'])
    return np.array(data[::-1])

# 訓練用のデータセットを用意
def trainData(data):
    for i in range(0,Last_Index):
        values = data[Start_Index+i:Start_Index+Last_Index+1+i]
        today = values[0]
        lastday = values[Start_Index+i]
        if  today > lastday:
            train_y.append(1)
        else:
            train_y.append(0)
        train_X.append(values)      
    return np.array(train_X), np.array(train_y)

# 予測と正解データの生成を行う
def prediction():
    for i in range(0,Last_Index):
        values = predict_data[Start_Index+i:Start_Index+Last_Index+1+i]
        test_y.append(values)
        today = values[0]
        lastday = values[Start_Index+i]
        if today > lastday :
            answer.append(1)
        else:
            answer.append(0)		
        result = clf.predict(test_y)
    predictions = result
    return predictions ,answer ,test_y

train_X = []
train_y = []
# CSVデータを格納
data = importData('bitcoin_data_train.csv')
# 訓練用データを格納
train_X, train_y = trainData(data)

#----SVMアルゴリズムによるモデルの生成----clf = svm.SVC()
# ランダムフォレストのアルゴリズムでモデルを生成
clf = RandomForestClassifier()
# 訓練を実行
clf.fit(train_X, train_y)
 
test_X = []
test_y = []
answer = []
result = []
predictions = [] 
predict_data = importData('bitcoin_data_test.csv')
# 予測を実行
predictions ,answer ,test_y = prediction()

#----訓練用データの表示----print("訓練用データ:", train_X)
#----予測用データの表示----print("予測用データ:", test_y)
print("学習結果:",train_y)
print("予測結果:", predictions)

up_count = 0.0
for i in predictions:
    if i > 0:
	    up_count += 1.0
total = len(predictions)
up_ratio = up_count / total *100
ac_score = metrics.accuracy_score(predictions,answer)
cl_report = metrics.classification_report(predictions,answer)
print("予測結果の正解率：" + str(ac_score*100) + "%")
print("正解データ：" + str(answer))
print("予測結果の上昇率:"+ str(up_ratio) + "%")	
print(cl_report)
import sklearn
print(sklearn.__version__)