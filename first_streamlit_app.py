import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#Snowflake function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')"
    return "Thanks for adding " + new_fruit
  
streamlit.title('My Parents New Healty Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry meal')
streamlit.text('🥗Kale, Spinache & Rocky Smotthie')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  streamlit.error();

streamlit.header('View our fruit list - Add Your Favorites!')
if streamlit.button('Get Fruit List'):  
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  

#allow to the end user to add a fruit to the list
add_my_fruit = streamlit.text_input("What fruit would yo like to add?")
if streamlit.button('add a fruit to the list'):  
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text(insert_row_snowflake(add_my_fruit))
  my_cnx.close()

