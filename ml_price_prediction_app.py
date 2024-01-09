import streamlit as st
import pickle
import numpy as np

lr= pickle.load(open("Linear_reg model.pkl","rb"))
rid= pickle.load(open("Ridge_reg model.pkl","rb"))
las= pickle.load(open("Lasso_reg model.pkl","rb"))
rf=pickle.load(open("RandomForest_reg model.pkl","rb"))
bag= pickle.load(open("Bagging_reg model.pkl","rb"))

st.title("Car Selling_price Prediction web app")
st.subheader("Fill the below detail to predict car price")

model=st.sidebar.selectbox("Choose the ML model",["Lin_reg","Ridge_reg","Lasso_reg","rf_reg","Bag_reg"])

year=st.slider('Year',2000,2020)
km_driven=st.slider('km_driven',1,200000)
name=st.selectbox('Name',['Ambassador Classic 2000 Dsz','Ambassador Grand 1800 ISZ MPFI PW CL','Audi A4 1.8 TFSI','Audi A4 2.0 TDI','Audi A4 2.0 TDI 177 Bhp Premium Plus',
                          'Audi A4 3.0 TDI Quattro','Audi A4 30 TFSI Technology'])
fuel=st.selectbox('Fuel',['Electric','LPG','Petrol'])
seller_type=st.selectbox('Seller_type',['Individual','Trustmark Dealer'])
transmission=st.selectbox('Transmission',['Manual','Automatic'])
owner=st.selectbox('Owner',['Fourth & Above Owner','Second Owner','Test Drive Car','Third Owner'])


Ambassador_Classic_2000_Dsz=0
Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
Audi_A4_18_TFSI=0
Audi_A4_2_TDI=0
Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
Audi_A4_3_TDI_Quattro=0
Audi_A4_30_TFSI_Technology=0
Electric=0
LPG=0
Petrol=0
Individual=0
TrustmarkDealer=0
transmission=0
Fourthandabove=0
Second=0
Testdrivecar=0
Third=0
   


if st.button('Predict Car Selling_price'):
    if name=='Ambassador Classic 2000 Dsz':
        Ambassador_Classic_2000_Dsz=1
        Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
        Audi_A4_18_TFSI=0
        Audi_A4_2_TDI=0
        Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
        Audi_A4_3_TDI_Quattro=0
        Audi_A4_30_TFSI_Technology=0
    elif name=='Ambassador Grand 1800 ISZ MPFI PW CL':
         Ambassador_Classic_2000_Dsz=0
         Ambassador_Grand_1800_ISZ_MPFI_PW_CL=1
         Audi_A4_18_TFSI=0
         Audi_A4_2_TDI=0
         Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
         Audi_A4_3_TDI_Quattro=0
         Audi_A4_30_TFSI_Technology=0
    elif name=='Audi A4 1.8 TFSI':
        Ambassador_Classic_2000_Dsz=0
        Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
        Audi_A4_18_TFSI=1
        Audi_A4_2_TDI=0
        Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
        Audi_A4_3_TDI_Quattro=0
        Audi_A4_30_TFSI_Technology=0
    elif name=='Audi A4 2.0 TDI':
        Ambassador_Classic_2000_Dsz=0
        Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
        Audi_A4_18_TFSI=0
        Audi_A4_2_TDI=1
        Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
        Audi_A4_3_TDI_Quattro=0
        Audi_A4_30_TFSI_Technology=0   
    elif name=='Audi A4 2.0 TDI 177 Bhp Premium Plus' :
        Ambassador_Classic_2000_Dsz=0
        Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
        Audi_A4_18_TFSI=0
        Audi_A4_2_TDI=0
        Audi_A4_2_TDI_177_Bhp_PremiumPlus=1
        Audi_A4_3_TDI_Quattro=0
        Audi_A4_30_TFSI_Technology=0   
    elif name=='Audi A4 3.0 TDI Quattro' :
        Ambassador_Classic_2000_Dsz=0
        Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
        Audi_A4_18_TFSI=0
        Audi_A4_2_TDI=0
        Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
        Audi_A4_3_TDI_Quattro=1
        Audi_A4_30_TFSI_Technology=0   
    else:
         Ambassador_Classic_2000_Dsz=0
         Ambassador_Grand_1800_ISZ_MPFI_PW_CL=0
         Audi_A4_18_TFSI=0
         Audi_A4_2_TDI=0
         Audi_A4_2_TDI_177_Bhp_PremiumPlus=0
         Audi_A4_3_TDI_Quattro=0
         Audi_A4_30_TFSI_Technology=1

    if fuel=='Electric':
        Electric=1
        LPG=0
        Petrol=0
    elif fuel=='LPG':
        Electric=0
        LPG=1
        Petrol=0
    else:
        Electric=0
        LPG=0
        Petrol=1
    
    if seller_type=='Individual':
        Individual=1
        TrustmarkDealer=0
    else:
        Individual=0
        TrustmarkDealer=1

    if transmission=='Manual':
        transmission=1
    else:
        transmission=0
           
     
    
    if owner=='Fourth & Above Owner':
        Fourthandabove=1
        Second=0
        Testdrivecar=0
        Third=0
    elif owner=='Second Owner':
        Fourthandabove=0
        Second=1
        Testdrivecar=0
        Third=0
    elif owner=='Test Drive Car':
        Fourthandabove=0
        Second=0
        Testdrivecar=1
        Third=0
    else:
        Fourthandabove=0
        Second=0
        Testdrivecar=0
        Third=1
         
        
        
    
test=np.array([year,km_driven,Ambassador_Classic_2000_Dsz,Ambassador_Grand_1800_ISZ_MPFI_PW_CL,Audi_A4_18_TFSI,Audi_A4_2_TDI,Audi_A4_2_TDI_177_Bhp_PremiumPlus,
               Audi_A4_3_TDI_Quattro,Audi_A4_30_TFSI_Technology,Electric,LPG,Petrol,Individual,TrustmarkDealer,transmission,Fourthandabove,Second,Testdrivecar,Third]+[0]*1484)


test=test.reshape(1,-1)

if model=='Lin_reg':
    st.success(lr.predict(test)[0])
elif model=='Ridge_reg':
    st.success(rid.predict(test)[0])
elif model=='Lasso_reg':
    st.success(las.predict(test)[0])
elif model=='rf_reg':
    st.success(rf.predict(test)[0])
else :
    st.success(bag.predict(test)[0])
    
    
    





    








        
