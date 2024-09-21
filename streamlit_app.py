# Import python packages
import streamlit as st


# Write directly to the app
st.title("CUSTOMIZE YOUR SMOOTHIE")
st.write("Choose the fruit:")

name = st.text_input("ENTER NAME")
st.write("Your name is", name)

# Get active session
session = snowflake.snowpark.context.get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(F.col('FRUIT_NAME')).to_pandas()

# Convert DataFrame to a list for multiselect
fruit_options = my_dataframe['FRUIT_NAME'].tolist()

INGREDIENTS_LIST = st.multiselect(
    "CHOOSE 5 FRUITS:",
    fruit_options,
    max_selections=5
)

st.write(INGREDIENTS_LIST)

if INGREDIENTS_LIST:
    ingredients = ' '.join(INGREDIENTS_LIST)

    # Parameterized query to avoid SQL injection
    my_insert_stmt = f"""
    INSERT INTO smoothies.public.orders (ingredients, name_on_order)
    VALUES (%s, %s)
    """
    st.write(my_insert_stmt)

    time_insert = st.button('SUBMIT ORDER')

    if time_insert:
        session.sql(my_insert_stmt, (ingredients, name)).collect()
        st.success(f'Your Smoothie is ordered, {name}!')
