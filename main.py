import pandas as pd
import xgboost as xgb
import streamlit as st


# Image URL
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR44QWCLUgbbIRyMkJzs-uY1TBQHLwrxzHAiO75TMGiXANUVk1EyMrBi1AkebcVIPYJOgc&usqp=CAU"

html_code = f'<img src="{image_url}" alt="Image" width="300">'

st.markdown(html_code, unsafe_allow_html=True)




def main():
    html_temp = """
    <div style = "background-color : Light;padding : 7px">
    <h2 style ='color:red; text-align : right'> Car Price Prediction Using Machine Learning</h2>
    </div>
    """
   
    model = xgb.XGBRegressor()

    model.load_model('xgb_model.json')
    
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write('')
    st.write('')
    
    st.markdown("#### Let's evaluate the price of a car")
    
    p1 = st.number_input("In which Year car was purchased", 1990,2024)
    
    p2 = st.number_input("Present_Price(In Lakhs)", 2.5, 25.0, step = 1.0)
    
    p3 = st.number_input("Distance completed by car in kilometers", 100, 5000000, step = 100)
    
    s1 = st.selectbox("Fuel Type",('CNG','Diesel','Petrol'))
    
    if s1 == 'CNG':
        p4 = 0
    elif s1 == 'Diesel':
        p4 = 1
    else:
        p4 = 2
    
    s2 = st.selectbox("Seller Type",('Dealer', 'Individual'))
    
    if s2 =='Dealer':
        p5 = 0
    else:
        p5 = 1
    
    s3 = st.selectbox("Transmission Type", ('Automatic', 'Manual'))
    
    if s3 == 'Automatic':
        p6 = 0
    else:
        p6 = 1
    
    p7 = st.slider('Number of owners car had previously?',0,3)
    
    data_new = pd.DataFrame({
        'Year' : p1,
        'Present_Price' : p2,
        'Kms_Driven' : p3,
        'Fuel_Type' : p4,
        'Seller_Type' : p5,
        'Transmission' : p6,
        'Owner' : p7
    }, index = [0])

    if st.button('Predict'):
        pred = model.predict(data_new)
        st.success('you can sell your car for {:.2f} Lakhs'.format(pred[0]))
           
        
if __name__ == '__main__':
    main()