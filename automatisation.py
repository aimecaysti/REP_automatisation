import os
import pyautogui
import time
import pyperclip
import streamlit as st
import shutil

# Define the main function
def run_automation(selected_table, x_value, fichier_source, fichier_destination):
    pyperclip.copy(x_value)  # Copy the x_value entered by the user
    # Duplicate the file
    shutil.copy(fichier_source, fichier_destination)

    if st.button('Start Automation'):
        os.startfile(fichier_destination)  # Open the duplicated .pbix file
        screen_width, screen_height = pyautogui.size()

        

        # Wait for Power BI to open (adjust sleep time based on your machine)
        st.write(f"Waiting for Power BI to open and updating the {selected_table} table...")
        time.sleep(30)

        # Automation steps for the selected table
        if selected_table == 'Pretest_Melong':
            pyautogui.moveTo(0.38 * screen_width, 0.093 * screen_height)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(0.044 * screen_width, 0.173 * screen_height)
            pyautogui.click(button='right')
            time.sleep(5)
            pyautogui.moveTo(0.0901 * screen_width, 0.481 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.585 * screen_width, 0.24 * screen_height)
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(3)
            pyautogui.moveTo(0.693 * screen_width, 0.781 * screen_height)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.moveTo(0.020 * screen_width, 0.087 * screen_height)
            pyautogui.click(button='left')
    
            time.sleep(10)
            pyautogui.moveTo(0.0197* screen_width, 0.120 * screen_height)
            pyautogui.click(button='left')
            time.sleep(35)
            pyautogui.moveTo(0.5947* screen_width, 0.573 * screen_height)
            pyautogui.click(button='left')
            time.sleep(3)
            pyautogui.moveTo(0.011* screen_width, 0.01 * screen_height)
            pyautogui.click(button='left')
            
            #Publier le dashboard
            time.sleep(15)
            pyautogui.moveTo(0.645* screen_width,0.0916 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.573* screen_width,0.612 * screen_height)
            pyautogui.click(button='left')
            # si le fichier existe deja, le remplacer
            time.sleep(25)
            pyautogui.moveTo(0.556* screen_width,0.573 * screen_height)
            pyautogui.click(button='left')
            time.sleep(30)
            pyautogui.moveTo(0.595* screen_width,0.613 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.98* screen_width,0.011 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.456* screen_width,0.521 * screen_height)
            pyautogui.click(button='left')



        elif selected_table == 'Postest_Melong':
            pyautogui.moveTo(0.38 * screen_width, 0.093 * screen_height)
            pyautogui.click(button='left')
            time.sleep(20)
            pyautogui.moveTo(0.0583 * screen_width, 0.266 * screen_height)
            pyautogui.click(button='right')
            time.sleep(5)
            pyautogui.moveTo(0.069 * screen_width, 0.572 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.578 * screen_width, 0.242 * screen_height)
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(3)
            pyautogui.moveTo(0.693 * screen_width, 0.781 * screen_height)
            pyautogui.click(button='left')
            time.sleep(10)
            pyautogui.moveTo(0.020 * screen_width, 0.087 * screen_height)
            pyautogui.click(button='left')
                
            time.sleep(10)
            pyautogui.moveTo(0.0197* screen_width, 0.120 * screen_height)
            pyautogui.click(button='left')
            time.sleep(35)
            pyautogui.moveTo(0.5947* screen_width, 0.573 * screen_height)
            pyautogui.click(button='left')
            time.sleep(3)
            pyautogui.moveTo(0.011* screen_width, 0.01 * screen_height)
            pyautogui.click(button='left')
            
            #Publier le dashboard
            time.sleep(15)
            pyautogui.moveTo(0.645* screen_width,0.0916 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.573* screen_width,0.612 * screen_height)
            pyautogui.click(button='left')
            # si le fichier existe deja, le remplacer
            time.sleep(25)
            pyautogui.moveTo(0.556* screen_width,0.573 * screen_height)
            pyautogui.click(button='left')
            time.sleep(5)
            pyautogui.moveTo(0.595* screen_width,0.613 * screen_height)
            pyautogui.click(button='left')


        st.success(f"{selected_table} table updated successfully.")


logo_path = 'logo01.ico'  # Replace with the path to your logo image
st.image(logo_path, width=150)  # Adjust width as needed


# Streamlit app
# Center the title
st.markdown(
    """
    <h1 style="text-align: center;">Power BI Table Update Automation</h1>
    """,
    unsafe_allow_html=True
)

x_value = st.text_input('Enter or paste the id form:', '')
# File selection and duplication
fichier_source = st.text_input('Enter the path of the source .pbix file', 'C:/Users/caysti/Documents/Formulaires/source.pbix')
fichier_destination = st.text_input('Enter the path where the duplicated .pbix file will be saved', 'C:/Users/caysti/Documents/Formulaires/destination.pbix')

# Table selection
tables = ['Pretest_Melong', 'Postest_Melong']
selected_table = st.selectbox('Select the table to update:', tables)

# Input field for variable 'x'


# Run automation
run_automation(selected_table, x_value, fichier_source, fichier_destination)
