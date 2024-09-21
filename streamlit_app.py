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
    , my_dataframe
    , max_selections =5
)
st.write(INGREDIENTS_LIST)
st.text(INGREDIENTS_LIST)
if INGREDIENTS_LIST:
    ingredients = ''
for fruit_chosen in INGREDIENTS_LIST: 
    ingredients +=fruit_chosen +' '
#st.write(ingredients)

my_insert_stmt = """ insert into smoothies.public.orders (ingredients,name_on_order) values ('""" + ingredients + """','""" +name+ """')"""
st.write(my_insert_stmt)
#st.stop();
time_insert= st.button('SUBMIT ORDER'); 

if time_insert:
    session.sql(my_insert_stmt).collect()
st.success('Your Smoothie is ordered,+name')

    


