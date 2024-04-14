# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw: Customise Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the Fruits You Want in Custome Smoothie."""
)

name_on_order = st.text_input('Name on Smoothie')
st.write('The Name on your Smoothie will be:', name_on_order)

from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    'Choose upto 5 ingredients',
    my_dataframe,
    max_selections=5
)

if ingredients_list:
    ingredients_string=''
    
    for friut_choosen in ingredients_list:
        ingredients_string += friut_choosen + ' '

    st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" +name_on_order + """')"""
    
    #st.write(my_insert_stmt)
    #st.stop()  
   
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success("✅"'Your Smoothie is ordered,'+ name_on_order +'!')

                if fv_data:
                    st.subheader(fruit_choosen + ' Nutrition Information')
                    fv_df = st.dataframe(data=fv_data, use_container_width=True)
                else:
                    st.warning("No data found for " + fruit_choosen)
            else:
                st.error("Failed to fetch data for " + fruit_choosen + ". Status code: " + str(fruityvice_response.status_code))
        except Exception as e:
            st.error("An error occurred while fetching data for " + fruit_choosen + ": " + str(e))

    st.write(ingredients_string)

    my_insert_stmt = """INSERT INTO smoothies.public.orders(ingredients, name_on_order)
                       VALUES ('{}', '{}')""".format(ingredients_string, name_on_order)
   
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success("✅ Your Smoothie is ordered, " + name_on_order + "!")
