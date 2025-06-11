import math
import streamlit as st
st.markdown("# Hello Data Analyst")
st.markdown ("## Hello Data Analyst")
st.markdown
st.markdown("# Hello")
st.markdown("# Hello")

st.title("right angle pythogoras theorem")
adj = st.number_input("enter your adjacent value")
opp = st.number_input("enter your opposite value")
def hyp(x,y):
    hypotenus  = math.sqrt(math.pow(x,2)+ math.pow(y,2))
    return hypotenus 


st.write(hyp(adj,opp))

















'''
power = math.pow  (5,20)

cosine = math.cos(45)
inv_cos =math.acos(0.525321988888177297)


print(cosine)


add = sum ([12,9])
print(add)


#list
fruits = ("mango,""apple")
num = (1,2,3,,4,5,6)

add2 = sum(num)
print(add2)
'''

