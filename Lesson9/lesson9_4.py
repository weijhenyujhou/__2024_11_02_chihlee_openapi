import streamlit as st
import tensorflow as tf
import numpy as np

def load_and_use_tflite(tflite_model_path):
    """
    Load a TensorFlow Lite model and use it for prediction
    
    Args:
        tflite_model_path (str): Path to the .tflite model file
    
    Returns:
        Function: A predict function to perform inference using the loaded TFLite model
    """
    # 1. 載入 TensorFlow Lite 模型
    # 使用 TensorFlow Lite Interpreter 載入模型檔案
    interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
    
    # 2. 分配張量 (Allocate tensors for the model)
    interpreter.allocate_tensors()
    
    # 3. 取得模型的輸入和輸出資訊
    # input_details 包含輸入張量的索引、形狀、資料型別等資訊
    # output_details 包含輸出張量的索引、形狀、資料型別等資訊
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # 4. 定義一個預測函式
    def predict(input_data):
        """
        Perform prediction using the loaded TFLite model
        
        Args:
            input_data (list or numpy array): Input data for prediction
        
        Returns:
            numpy array: The prediction result
        """
        # 準備輸入資料，轉換成符合模型輸入形狀的 NumPy 陣列
        input_data = np.array(input_data, dtype=np.float32).reshape(input_details[0]['shape'])
        
        # 設定模型輸入的張量資料
        interpreter.set_tensor(input_details[0]['index'], input_data)
        
        # 執行推論 (Invoke the interpreter to perform inference)
        interpreter.invoke()
        
        # 獲取模型輸出的結果
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        return output_data

    # 回傳內部定義的預測函式供使用
    return predict


st.title('1元1次方程式')
st.title('Y = 2X - 1')

# 提供一個聊天輸入框，提示使用者輸入 X 的值
prompt = st.chat_input("請輸入X的值:")

# 如果使用者有輸入值，進行以下處理
if prompt:
    # 將輸入的值轉換為浮點數
    input_value = float(prompt)
    
    # 定義 TensorFlow Lite 模型檔案的路徑
    tflite_model_path = 'linear_model.tflite'
    
    # 使用自定義函數載入並初始化 TFLite 模型的預測功能
    tflite_predict_func = load_and_use_tflite(tflite_model_path)
    
    # 將輸入值轉換為測試輸入格式 (這裡假設模型需要一個列表作為輸入)
    test_input = [input_value]
    
    # 使用 TFLite 模型進行預測
    predict_value = tflite_predict_func(test_input)
    
    # 將預測結果中的第一個數值取整數，並轉換為浮點數型別後四捨五入
    round_value = round(float(predict_value[0, 0]))
    
    # 顯示輸入值 X 和對應的預測值 Y
    st.write(f"X={input_value},Y={round_value}")
