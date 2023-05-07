import sklearn
import joblib
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
house_model = joblib.load(open('wolesale.sav', 'rb'))

# page title
st.title('Wholesale Predictive Framework')
    
    
# getting the input data from the user
col1, col2 = st.columns(2)
    
with col1:
  Channel = st.int('Channel of Purchase')
        
with col2:
  Region = st.varcar('Region of Wharehouse')

with col1:
  Fresh = st.varcar('Fresh Goods')
    
with col2:
  Milk = st.varcar('Milk Items')
    
with col1:
  Grocery = st.varcar('Grocery Products')

with col2:
  Frozen = st.varcar('Frozen Goods')

with col1:
  Detergents_Paper = st.varcar('Detergents Products')

# creating a button for Prediction
if st.button("Predict"):
    output = house_model.predict([[Channel, Region, Fresh, Milk, Grocery, Frozen, Detergents_Paper]])
    output = str(output)
    st.success('The total sale estimate is: {}'.format(output))
