# Import python packages
import streamlit as st




# Write directly to the app
st.title("CUSTOMIZE YOUR SMOOTHIE ")
st.write(
    """choose the fruit """
)


name = st.text_input("ENTER NAME")
st.write("your name is ", name);

#session = get_active_session()
#my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME')) 
#st.dataframe(data=my_dataframe, use_container_width=True)


INGREDIENTS_LIST= st.multiselect(
    "CHOOSE 5 FRUITS:"
    ,max_selections =5
)
st.write(INGREDIENTS_LIST)
st.text(INGREDIENTS_LIST)
if INGREDIENTS_LIST:
    ingredients = ''
for fruit_chosen in INGREDIENTS_LIST: 
    ingredients +=fruit_chosen +' '
#st.write(ingredients)



    


