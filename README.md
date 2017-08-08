## Scikit-learnを使ったBitcoinの価格予測

<img src="https://user-images.githubusercontent.com/26180642/29090156-9965a3c0-7cb9-11e7-9fa0-f9694ba7ddc1.jpg" width="400px">


### 概要
* 機械学習の学習用
* 先月分のデータを学習させて、当日の結果を予測して正答率を算出
* 前日からの変化を見て上昇なら[1]下降なら[0]でラベルを振り分ける
* 学習用データと正解ラベルをセットで学習させ、予測用データで検証を行う
* Scikit-learnを使用
* 学習モデルはランダムフォレストを使用
* データはcoindesk (https://www.coindesk.com/price/) からダウンロード


## 実行環境
* python 3.6.0
* Anaconda 3
* Scikit-learn 0.18.2 (0.19以降だと動作しない可能性があります。)　
* RandomForestClassifier

## 参考
http://kasoutuuka.org/scikit-learn

