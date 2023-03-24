import streamlit as st
import numpy as np 
import pandas as pd
import pickle

model = pickle.load(open('model_xb.pkl','rb'))

st.title("Mushroom Classification")

cap_shape = st.selectbox('Select Cap Shape',("bell","conical","flat","knobbed","sunken","convex"))

cap_surface = st.selectbox('Select Cap Surface',("fibrous","grooves","smooth","scaly")) 

cap_color = st.selectbox('Select Cap Color',("buff","cinnamon","red","gray","brown","pink","green","purple","white","yellow")) 

bruises = st.selectbox('Select Bruises',("no","bruises")) 

odor = st.selectbox('Select Odor',("almond","creosote","foul","anise","musty","none","pungent","spicy","fishy")) 

gill_attachment = st.selectbox('Select Gill Attachment',("attached","free")) 

gill_spacing = st.selectbox('Select Gill Spacing',("close","crowded"))

gill_size = st.selectbox('Select Gill Size',("broad","narrow")) 

gill_color = st.selectbox('Select Gill Color',("buff","red","gray","chocolate","black","brown","orange","pink","green","purple","white","yellow"))
 
stalk_shape = st.selectbox('Select Stalk Shape',("enlarging","tapering")) 

stalk_root = st.selectbox('Select Stalk Root',("missing","bulbous","club","equal","rooted")) 

stalk_surface_above_ring = st.selectbox('Select Stalk surface above ring',("fibrous","silky","smooth","scaly"))
 
stalk_surface_below_ring = st.selectbox('Select Stalk surface below ring',("fibrous","silky","smooth","scaly"))

stalk_color_above_ring = st.selectbox('Select Stalk color above ring',("buff","cinnamon","red","gray","brown","orange","pink","white","yelllow"))

stalk_color_below_ring = st.selectbox('Select Stalk color below ring',("buff","cinnamon","red","gray","brown","orange","pink","white","yelllow"))

veil_color = st.selectbox('Select veil color',("brown","orange","white","yellow"))
 
ring_number = st.selectbox('Select ring number',("none","one","two")) 

ring_type = st.selectbox('Select ring type',("evanescent","flaring","large","none","pendant"))

spore_print_color = st.selectbox('Select spore print color',("buff","chocolate","black","brown","orange","green","purple","white","yellow"))
 
population = st.selectbox('Select population',("abundant","clustered","numerous","scattered","several","solitary")) 

habitat = st.selectbox('Select habitat',("wood","grasses","leaves","meadows","paths","urban","waste"))
        
l = {}
l['cap_shape'] = cap_shape
l['cap_surface'] = cap_surface
l['cap_color'] = cap_color
l['bruises'] = bruises
l['odor'] = odor
l['gill_attachment'] = gill_attachment
l['gill_spacing'] = gill_spacing
l['gill_size'] = gill_size
l['gill_color'] = gill_color
l['stalk_shape'] = stalk_shape
l['stalk_root'] = stalk_root
l['stalk_surface_above_ring'] = stalk_surface_above_ring
l['stalk_surface_below_ring'] = stalk_surface_below_ring
l['stalk_color_above_ring'] = stalk_color_above_ring
l['stalk_color_below_ring'] = stalk_color_below_ring
l['veil_color'] = veil_color
l['ring_number'] = ring_number
l['ring_type'] = ring_type
l['spore_print_color'] = spore_print_color
l['population'] = population
l['habitat'] = habitat

df = pd.DataFrame(l, index=[0])
df['cap_shape'] = df['cap_shape'].map({"bell":0,"conical":1,"flat":2,"knobbed":3,"sunken":4,"convex":5})
df['cap_surface'] = df['cap_surface'].map({"fibrous":0,"grooves":1,"smooth":2,"scaly":3})
df['cap_color'] = df['cap_color'].map({"buff":0,"cinnamon":1,"red":2,"gray":3,"brown":4,"pink":5,"green":6,"purple":7,"white":8,"yellow":9})
df['bruises'] = df['bruises'].map({"no":0,"bruises":1})
df['odor'] = df['odor'].map({"almond":0,"creosote":1,"foul":2,"anise":3,"musty":4,"none":5,"pungent":6,"spicy":7,"fishy":8})
df['gill_attachment'] = df['gill_attachment'].map({"attached":0,"free":1})
df['gill_spacing'] = df['gill_spacing'].map({"close":0,"crowded":1})
df['gill_size'] = df['gill_size'].map({"broad":0,"narrow":1})
df['gill_color'] = df['gill_color'].map({"buff":0,"red":1,"gray":2,"chocolate":3,"black":4,"brown":5,"orange":6,"pink":7,"green":8,"purple":9,"white":10,"yellow":11})
df['stalk_shape'] = df['stalk_shape'].map({"enlarging":0,"tapering":1})
df['stalk_root'] = df['stalk_root'].map({"missing":0,"bulbous":1,"club":2,"equal":3,"rooted":4})
df['stalk_surface_above_ring'] = df['stalk_surface_above_ring'].map({"fibrous":0,"silky":1,"smooth":2,"scaly":3})
df['stalk_surface_below_ring'] = df['stalk_surface_below_ring'].map({"fibrous":0,"silky":1,"smooth":2,"scaly":3})
df['stalk_color_above_ring'] = df['stalk_color_above_ring'].map({"buff":0,"cinnamon":1,"red":2,"gray":3,"brown":4,"orange":5,"pink":6,"white":7,"yelllow":8})
df['stalk_color_below_ring'] = df['stalk_color_below_ring'].map({"buff":0,"cinnamon":1,"red":2,"gray":3,"brown":4,"orange":5,"pink":6,"white":7,"yelllow":8})
df['veil_color'] = df['veil_color'].map({"brown":0,"orange":1,"white":2,"yellow":3})
df['ring_number'] = df['ring_number'].map({"none":0,"one":1,"two":2})
df['ring_type'] = df['ring_type'].map({"evanescent":0,"flaring":1,"large":2,"none":3,"pendant":4})
df['spore_print_color'] = df['spore_print_color'].map({"buff":0,"chocolate":1,"black":2,"brown":3,"orange":4,"green":5,"purple":6,"white":7,"yellow":8})
df['population'] = df['population'].map({"abundant":0,"clustered":1,"numerous":2,"scattered":3,"several":4,"solitary":5})
df['habitat'] = df['habitat'].map({"wood":0,"grasses":1,"leaves":2,"meadows":3,"paths":4,"urban":5,"waste":6})

y_pred = model.predict(df)

print(y_pred[0])
if st.button("Show Result"):
    if y_pred[0] == 0:
        st.header("Edible")
    else:
        st.header("Poisonous")
