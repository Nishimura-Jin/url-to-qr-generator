import qrcode
import streamlit as st
import numpy as np
from PIL import Image

st.title("QRコード自動生成アプリ")

url = st.text_input("QRコードを作成したいURLを入力してください")

if st.button("QRコード作成"):
    _img = qrcode.make(url)
    _img.save("qrcode.png")
    img = Image.open("qrcode.png")
    st.image((img))

