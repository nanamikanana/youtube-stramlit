import streamlit as st 
import numpy as np 
import pandas as pd 
from PIL import Image
import time

st.title('Streamlit 超入門')

###########################################
st.write('プログレスバーの表示')
'Start!!!'
latest_iterarion = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iterarion.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'
#########################################
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムだよ')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2回答')


# text = st.text_input('あなたの趣味は?')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

######################################
# インタラクティブ Diplay Intaractive widgetsに書いてある

# text = st.sidebar.text_input('あなたの趣味は?')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition



# option = st.selectbox(
#     'あなたが好きな数字を教えて。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option , 'です。'
# checkboxはtrueかfalseを返す
# if st.checkbox('Show Image'):
#     img = Image.open('sample1.jpg')
#     st.image(img,caption = 'Miko', use_column_width = True)



####################################
# Display mediaに書いてある
# img = Image.open('sample1.jpg')
# st.image(img,caption = 'Miko', use_column_width = True)




###################################
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a','b','c']
# )

# # Display chartsに書いてある
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

######################################
# # df = pd.DataFrame({
# #     '1列目': [1, 2, 3, 4],
# #     '2列目': [10, 20, 30, 40]
# # })

# # 幅高さハイライトを指定できるのはdataframe
# # st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# # テーブルを静的に表示させる　詳しくはmanualのDispaly dataに書いてある
# st.table(df.style.highlight_max(axis=0))

# # Display textに書いてある
# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st # type: ignore
# import numpy as np # type: ignore
# import pandas as pd # type: ignore

# ```
# """


