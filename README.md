# 判定方法について
スートに関連するものと、ランクに関連する役をそれぞれ分割して判定を行った。  
スートに関連するものは、ロイヤルフラッシュ、ストレートフラッシュ、フラッシュ、ストレートの4役。  
ランクに関連するものは、上記以外の6役とする。  

## 判定方法１（スート関連）
* ロイヤルフラッシュ  
  二次元配列で取得した手札をソートし、`[[0, 1], [0, 10], [0, 11], [0, 12], [0, 13]]`と比較
* ストレートフラッシュ  
  スートを集合に変換し、要素数が1であること  
  且つ、ランクをソートし、最大値と最小値の差が4であること、または`10, J, Q, K, A`の並びであること
* フラッシュ  
  スートを集合に変換し、要素数が1であること
* ストレート  
  ランクをソートし、最大値と最小値の差が4であること、または`10, J, Q, K, A`の並びであること

## 判定方法２（ランク関連）
`collections.Counter`を利用して、配列内の重複要素をカウントしている
* フォーカード  
  重複数が一番多い要素の重複数が**4**であること
* フルハウス  
  重複数が一番多い要素の重複数が**3**であること且つ、重複数が二番目に多い要素の重複数が**2**であること
* スリーカード  
  重複数が一番多い要素の重複数が**3**であること
* ツーペア  
  重複数が一番多い要素の重複数が**2**であること且つ、重複数が二番目に多い要素の重複数が**2**であること
* ワンペア  
  重複数が一番多い要素の重複数が**2**であること
* ハイカード  
  重複数が一番多い要素の重複数が**1**であること
