import qrcode
import streamlit as st
from io import BytesIO
from PIL import Image

st.title("QRコード生成ツール")
st.write("URLを入力するだけで、QRコードを作成・ダウンロードできます。")

# 入力フォーム
url = st.text_input("QRコード化したいURLを入力してください", placeholder="https://example.com")

if st.button("QRコードを生成"):
    if url:
        # QRコード生成
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Streamlitで表示するためにPILに変換
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        # 画面に表示
        st.image(byte_im, caption="生成されたQRコード", width=300)
        
        # ダウンロードボタン
        st.download_button(
            label="画像をダウンロード",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("URLを入力してください。")
