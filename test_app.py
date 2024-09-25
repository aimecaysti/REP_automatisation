import os
import pyautogui
import time
import pyperclip
import streamlit as st

# Define the main function
def run_automation(selected_table, x_value):
    fichier_duplique = st.text_input('Enter the path of the .pbix file', 'C:/Users/caysti/Documents/Formulaires/destination.pbix')
    if st.button('Start Automation'):
        os.startfile(fichier_duplique)  # Open the .pbix file
        screen_width, screen_height = pyautogui.size()

        pyperclip.copy(x_value)  # Copy the x_value entered by the user

        # Wait for Power BI to open (adjust sleep time based on your machine)
        st.write(f"Waiting for Power BI to open and updating the {selected_table} table...")
        time.sleep(30)

        # Example automation for different tables
        if selected_table == 'Pretest_Melong':
            # Code for the 'pretest' table (same as before)
            pyautogui.moveTo(0.38*screen_width, 0.093*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
            
            time.sleep(20)
            pyautogui.moveTo(0.044*screen_width, 0.173*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='right')  # Clic droit
            
            time.sleep(5)
            pyautogui.moveTo(0.0901*screen_width, 0.481*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
            
            
            time.sleep(5)
            pyautogui.moveTo(0.585*screen_width, 0.24*screen_height)  # (X, Y) à adapter
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')  # Pour Windows/Linux
            
            time.sleep(10)
            
            pyautogui.moveTo(0.693*screen_width,0.781*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
            
            time.sleep(10)
            pyautogui.moveTo(0.020*screen_width, 0.087*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droitaTRJUA4e8S4nxE4UR5h5rg
            
            time.sleep(10)
            pyautogui.moveTo(0.0255*screen_width,0.118*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
            
            time.sleep(10)
            pyautogui.moveTo(0.599*screen_width,0.574*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
            
            time.sleep(10)
            pyautogui.moveTo(0.013*screen_width,0.015*screen_height)  # (X, Y) à adapter
            pyautogui.click(button='left')  # Clic droit
        elif selected_table == 'Postest_Melong':
            # Code for the 'Postest_Melong' table
            pyautogui.moveTo(0.38 * screen_width, 0.093 * screen_height)
            pyautogui.click(button='left')
            time.sleep(20)

            pyautogui.moveTo(0.056 * screen_width, 0.087 * screen_height)
            pyautogui.click(button='right')
            time.sleep(10)

            pyautogui.moveTo(0.040 * screen_width, 0.177 * screen_height)
            pyautogui.click(button='right')
            time.sleep(10)

            pyautogui.moveTo(0.69*screen_width, 0.24*screen_height)
            pyautogui.doubleClick()
            time.sleep(5)

            pyautogui.hotkey('ctrl', 'v')  # Paste copied content
            time.sleep(10)

            pyautogui.moveTo(0.69 * screen_width, 0.78 * screen_height)
            pyautogui.click(button='left')
            time.sleep(10)

            pyautogui.moveTo(0.98 * screen_width, 0.004 * screen_height)
            pyautogui.click(button='left')
            time.sleep(10)

            pyautogui.moveTo(0.49 * screen_width, 0.521 * screen_height)
            pyautogui.click(button='left')
            time.sleep(10)

            pyautogui.moveTo(0.013 * screen_width, 0.0 * screen_height)
            pyautogui.click(button='left')

        st.success(f"{selected_table} table updated successfully.")

# Streamlit app
st.title('Power BI Table Update Automation')

# Table selection
tables = ['Pretest_Melong', 'Postest_Melong']  # List includes 'pretest' and 'Postest_Melong' for now
selected_table = st.selectbox('Select the table to update:', tables)

# Input field for variable 'x'
x_value = st.text_input('Enter or paste the value of x:', '')

run_automation(selected_table, x_value)
