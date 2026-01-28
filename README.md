# QRコード自動生成アプリ (Streamlit)

シンプルなURL入力でQRコードを即座に生成・表示できるWebアプリです。  
Python + Streamlit でサクッと作りました。


## 機能
- 任意のURLを入力するだけでQRコードを生成
- 生成したQRコードをブラウザ上で即座に確認
- 軽量・シンプル設計（依存関係も最小限）

## デモ（予定）

## ローカルでの実行方法

1. リポジトリをクローン
   git clone https://github.com/RuuL333/qr-code-generator-streamlit.git
   cd qr-code-generator-streamlit

仮想環境を作成（推奨）Bashpython -m venv venv
source venv/bin/activate    # Windowsの場合は venv\Scripts\activate
依存関係をインストールBashpip install -r requirements.txt
アプリを起動
streamlit run app.py
ブラウザが自動で開くので、URLを入力して「QRコード作成」を押してください！
ターミナルでCtrl + Cを押して終了
