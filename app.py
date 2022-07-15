# Let's build average portfolio cost calculator 


from cProfile import label
import streamlit as st



st.write(""" 
# Average Portfolio Cost Calculator
### Laddering is an important strategy when it comes to investing in financial markets.
It allows you to place your buy orders with decreasing price thereby bringing down the average cost per share. 
If you have used laddering, this application will help you calculate the average cost per share for
the different elements in your portfolio.

 """)

# shares_1 = st.number_input(f"Please enter the amount of shares/coins/tokens/ you bought")
# price_1 = st.number_input(f"Please enter the price at which you bought the shares")

# shares_2 = st.number_input(f"Please enter the amount of shares/coins/tokens/ you bought")
# price_2 = st.number_input(f"Please enter the price at which you bought the shares")


col1,col2=st.columns(2)

with col1:
    st.markdown("**Shares Bought**")
    shares1=col1.number_input(label="1",value=1.0,key=1)
    shares2=col1.number_input("2",key=2)
    shares3=col1.number_input("3",key=3)
    shares4=col1.number_input("4",key=4)
    shares5=col1.number_input("5",key=5)
    shares6=col1.number_input("6",key=6)
    shares7=col1.number_input("7",key=7)
    shares8=col1.number_input("8",key=8)
    shares9=col1.number_input("9",key=9)
    shares10=col1.number_input("10",key=10)




with col2:
    
    st.markdown("**Price**")
    price1=col2.number_input(label="",value=1.0,key=11,step=0.000001,format="%.6f")
    price2=col2.number_input("",key=12,step=0.000001,format="%.6f")
    price3=col2.number_input("",key=13,step=0.000001,format="%.6f")
    price4=col2.number_input("",key=14,step=0.000001,format="%.6f")
    price5=col2.number_input("",key=15,step=0.000001,format="%.6f")
    price6=col2.number_input("",key=16,step=0.000001,format="%.6f")
    price7=col2.number_input("",key=17,step=0.000001,format="%.6f")
    price8=col2.number_input("",key=18,step=0.000001,format="%.6f")
    price9=col2.number_input("",key=19,step=0.000001,format="%.6f")
    price10=col2.number_input("",key=20,step=0.000001,format="%.6f")


# Lets build the logic

total_shares  = shares1+shares2+shares3+shares4+shares5+shares6+shares7+shares8+shares9+shares10
total_spent= shares1*price1+shares2*price2+shares3*price3+shares4*price4+shares5*price5+shares6*price6+shares7*price7+shares8*price8+shares9*price9+shares10*price10

avg_cost= total_spent/total_shares

st.write(f"**Total shares bought are {total_shares} at an average cost of {round(avg_cost,4)}**")



st.write(""" 
## Average Cost Formula

 """)


"""1. Total Shares Bought = Shares Bought(1st) + Shares Bought(2nd) + Shares Bought(3rd) + .... Shares Bought (nth)
2. Total Amount Bought = Shares Bought*Purchased Price(1st) + Shares Bought*Purchased Price(2nd) + Shares Bought*Purchased Price(3rd) + .... Shares Bought*Purchased Price(nth)
3. Stock Average Price = Total Amount Bought / Total Shares Bought"""
