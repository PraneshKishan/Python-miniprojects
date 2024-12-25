import streamlit as st 

col1, col2 = st.columns(2)

def dollar_to_rupee(dollars):
    cr = 85.39
    rupees = dollars * cr
    return rupees
    
def rupees_to_dollars(rupees,dollars):
    cr = 85.39
    dollars = rupees / cr
    return dollars

def conversion(type1, type2):
    if type1 == "Dollars" and type2 == "Rupees":
        r_op = dollar_to_rupee(inp_price)
        return r_op
    elif type1 == "Rupees" and type2 == "Dollars":
        d_op = rupees_to_dollars(inp_price)
        return d_op
    elif type1 == type2:
        return inp_price
    

with col1:
    inp_ctype = st.selectbox("Choose currency: ",("Dollars","Rupees"),index=None,key = 'input_currency')
    inp_price = st.number_input("Enter the price",key = 'input_price')

with col2:
    op_ctype = st.selectbox("Choose currency: ",("Dollars","Rupees"),index=None,key = 'output_currency')
    but = st.button("Convert")
    if but:
        final_price = conversion(inp_ctype, op_ctype)
        st.write(final_price)

