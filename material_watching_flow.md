# 樹脂振動後の平滑度 画像処理フロー

### メインルーチン
---
```flow
st=>start: 処理開始
ed=>end: 処理終了

op1=>operation: 樹脂 セット
op2=>operation: 振動ON
op3=>operation: タイマリレー カウント開始
op4=>operation: タイマリレー カントアップ
op5=>operation: 振動OFF
op6=>operation: 樹脂状態 撮影

sb1=>subroutine: 画像処理

cd1=>condition: OK/NG判定

io1=>inputoutput: OK出力
io2=>inputoutput: NG出力

st->op1->op2->op3->op4->op5->op6->sb1->cd1(yes)->io1->ed
cd1(no)->io2(right)->op1
```

### 画像処理
---
```flow
st=>start: 処理開始
ed=>end: 処理終了

op1=>operation: HSV 変換処理
op2=>operation: 指定色にマスク 生成
op3=>operation: OK/NG判定

st->op1->op2->op3->ed
```
