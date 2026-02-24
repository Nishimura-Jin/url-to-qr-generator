# QRコード自動生成アプリ (Streamlit)

シンプルなURL入力でQRコードを即座に生成・表示できるWebアプリです。  
Python + Streamlit でサクッと作りました。


## 機能
- 任意のURLを入力するだけでQRコードを生成
- 生成したQRコードをブラウザ上で即座に確認
- 軽量・シンプル設計（依存関係も最小限）

## デモ
[https://qr-generator-jin.streamlit.app/](https://url-to-qr-generator-jin.streamlit.app/)

## ローカルでの実行方法

1. リポジトリをクローン
   git clone https://github.com/Nishimura-Jin/url-to-qr-generator.git
   cd url-to-qr-generator

3. 仮想環境を作成（推奨）python -m venv venv
source venv/bin/activate    # Windowsの場合は venv\Scripts\activate
4. 依存関係をインストール
   pip install -r requirements.txt
5. アプリを起動
  streamlit run app.py
6. ブラウザが自動で開くので、URLを入力して「QRコード作成」を押してください！
7. ターミナルでCtrl + Cを押して終了
