# 匯入必要的函式庫
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import streamlit as st
from streamlit_clickable_images import clickable_images

# Fashion MNIST 資料集的類別名稱
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def load_model():
    """載入並編譯一個簡單的神經網路模型，用於 Fashion MNIST 的分類。"""
    # 定義一個順序模型
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),  # 將 28x28 圖像展平為一維陣列
        tf.keras.layers.Dense(128, activation='relu'), # 全連接層，包含 128 個神經元，使用 ReLU 激活函數
        tf.keras.layers.Dense(10, activation='softmax') # 輸出層，包含 10 個神經元，用於分類
    ])
    
    # 使用 Adam 優化器和稀疏分類交叉熵損失函數編譯模型
    model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    
    return model  # 返回編譯後的模型

def convert_image_to_base64(image_array):
    """將代表影像的 numpy 陣列轉換為 base64 編碼的字串以供顯示。"""
    plt.figure(figsize=(3, 3))  # 設定圖像大小
    plt.imshow(image_array, cmap='gray')  # 以灰階顯示影像
    plt.axis('off')  # 關閉座標軸，讓圖像更乾淨
    
    # 將影像儲存為 PNG 格式到緩衝區
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    # 將緩衝區的內容轉換為 base64 字串
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{image_base64}"  # 返回 base64 編碼的影像字串

def main():
    """主要函式，用於執行 Streamlit 應用程式。"""
    # 設定應用程式的標題與描述
    st.title("Fashion MNIST 分類器")
    st.write("點擊任意圖像查看其預測結果！")

    # 載入模型
    model = load_model()

    # 載入 Fashion MNIST 資料集（測試集）
    (_, _), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
    
    # 選取前 25 張測試影像及其標籤
    display_images = test_images[:25]
    display_labels = test_labels[:25]

    # 將選取的影像轉換為 base64 格式以供點擊圖像網格顯示
    image_paths = [convert_image_to_base64(img) for img in display_images]

    # 建立雙欄佈局
    col1, col2 = st.columns([2, 1])

    with col1:
        # 顯示可點擊的圖像網格
        clicked = clickable_images(
            image_paths,
            titles=[f"影像 {i+1}" for i in range(len(image_paths))],
            div_style={"display": "grid", "grid-template-columns": "repeat(5, 1fr)", "gap": "10px"},
            img_style={"cursor": "pointer", "border-radius": "5px", 
                      "transition": "transform 0.3s", "width": "100%"}
        )

    # 處理預測並顯示結果
    with col2:
        if clicked > -1:  # 檢查是否有圖像被點擊
            st.write("### 選取的影像")
            selected_image = display_images[clicked]  # 取得被點擊的影像
            st.image(selected_image, caption=f'影像 {clicked + 1}', width=200)
            
            # 對影像進行前處理（正規化到 [0, 1] 範圍）
            processed_image = selected_image / 255.0
            # 預測類別機率
            prediction = model.predict(processed_image.reshape(1, 28, 28))
            predicted_class = np.argmax(prediction)  # 取得機率最高的類別
            actual_class = display_labels[clicked]  # 取得實際標籤
            
            # 顯示預測結果
            st.write("### 預測結果")
            st.write(f"預測類別：**{class_names[predicted_class]}**")
            st.write(f"實際類別：**{class_names[actual_class]}**")
            
            # 顯示所有類別的預測機率
            st.write("### 信心分數")
            for i, prob in enumerate(prediction[0]):
                st.progress(float(prob))  # 顯示每個類別機率的進度條
                st.write(f"{class_names[i]}: {prob*100:.1f}%")  # 顯示機率百分比

# 如果此腳本直接執行，則啟動應用程式
if __name__ == '__main__':
    main()
