import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

def generate_qr_code(url, label_text=None, label_position="Top"):
    # 1. QRコードの生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # 注釈がない場合は、そのままQR画像のみを返す
    if not label_text:
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        return buf.getvalue()

    # 2. 注釈（ラベル）付き画像の作成
    width, height = qr_img.size
    margin = 60    # 上下の余白サイズ
    font_size = 24 # 文字の大きさ
    
    # --- フォントの読み込み設定 ---
    current_dir = os.path.dirname(__file__)
    font_path = os.path.join(current_dir, "fonts", "NotoSansJP-Medium.ttf")
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        # フォント読み込み失敗時の保険（エラーを表示して標準フォントを使用）
        st.error(f"Font Load Error: {e}")
        font = ImageFont.load_default()

    # 新しいキャンバス（余白分だけ縦を長くする）
    new_height = height + margin
    combined_img = Image.new("RGB", (width, new_height), "white")
    draw = ImageDraw.Draw(combined_img)

    # テキストを中央寄せにするための計算
    text_bbox = draw.textbbox((0, 0), label_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    x_pos = (width - text_width) // 2

    # 指定された位置にテキストとQRを配置
    if label_position == "Top":
        # 上に文字、下にQR
        draw.text((x_pos, (margin - font_size) // 2), label_text, fill="black", font=font)
        combined_img.paste(qr_img, (0, margin))
    else:
        # 上にQR、下に文字
        combined_img.paste(qr_img, (0, 0))
        draw.text((x_pos, height + (margin - font_size) // 2), label_text, fill="black", font=font)

    # 3. メモリ上に保存してバイナリを返す
    buf = BytesIO()
    combined_img.save(buf, format="PNG")
    return buf.getvalue()

def main():
    # ページの設定
    st.set_page_config(page_title="QRコード生成アプリ", layout="centered")
    st.title("URL to QR Generator")
    st.write("URLを入力してQRコードを生成できます。日本語の注釈も追加可能です。")

    # 入力フォーム
    url = st.text_input("QRコードにするURLを入力:", placeholder="https://example.com")
    
    # 必要な人だけが使う「注釈設定」
    with st.expander("注釈（ラベル）の設定"):
        label_text = st.text_input("表示する文字を入力してください", placeholder="例：公式LINEはこちら")
        label_position = st.radio("文字の配置を選択", ["Top", "Bottom"], horizontal=True)

    if st.button("QRコードを生成"):
        if url:
            with st.spinner("生成中..."):
                # 画像のバイナリデータを取得
                qr_bytes = generate_qr_code(url, label_text, label_position)
                
                # 画面表示
                #修正前　st.image(qr_bytes, caption="生成結果", use_container_width=True)
                st.image(qr_bytes, caption="生成結果（プレビュー）", width=300)
                
                # ダウンロードボタン
                st.download_button(
                    label="画像を保存する",
                    data=qr_bytes,
                    file_name="qr_code.png",
                    mime="image/png"
                )
        else:
            st.warning("URLが空欄です。入力をお願いします。")

if __name__ == "__main__":
    main()

