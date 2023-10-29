import pickle
import streamlit as st

model = pickle.load(open('estimasi_kalori.sav', 'rb'))

st.title('Estimasi Kalori Pada Makanan Cepat Saji')

col1, col2 = st.columns(2)

with col1:
    fiber = st.text_input('Input Serat pangan')
    total_carb = st.text_input('Input Total Karbohidrat')
    sodium = st.text_input('Input Sodium')
    cal_fat = st.text_input('Input Kalori dari lemak')

with col2:
    total_fat = st.text_input('Input Total lemak')
    sat_fat = st.text_input('Input Lemak jenuh')
    protein = st.text_input('Input Protein')
    sugar = st.text_input('Input Gula')

predict = ' '

if st.button('Estimasi Kalori'):
        input_features = [[float(fiber), float(total_carb), float(sodium), float(cal_fat), float(total_fat), float(sat_fat), float(protein), float(sugar)]]
        prediction = model.predict(input_features)
        kalori = int(prediction)
        
        if kalori < 200:
            explanation = 'Kalori makanan rendah. Biasanya kurang dari 200 kalori per porsi.Kalori rendah biasanya mengandung jumlah energi yang lebih sedikit per porsi, yang dapat membantu dalam program penurunan berat badan atau pengendalian berat badan.'
        elif 200 <= kalori <= 400:
            explanation = 'Kalori makanan sedang. Biasanya antara 200 hingga 400 kalori per porsi.Konsumsi kalori yang seimbang dapat membantu dalam mempertahankan berat badan yang sehat jika sejalan dengan kebutuhan energi harian.'
        else:
            explanation = 'Kalori makanan tinggi. Biasanya lebih dari 400 kalori per porsi.Konsumsi kalori berlebihan, terutama dari makanan yang kaya lemak dan gula, dapat menyebabkan peningkatan berat badan dan meningkatkan risiko obesitas.'
        st.write('Jumlah Kalori: ', kalori)
        st.write('Penjelasan:', explanation)
