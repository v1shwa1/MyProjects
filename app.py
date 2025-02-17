import pickle
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc

# importing the smaller apps
from ml_app import run_ml_app
from eda_app import run_eda_app

html_temp = """
			<div style="background-color:#8A9A5B;
				padding:10px;
				border-radius:10px"
				>
			<h1 style="color:white;text-align:center;"> Real Estate Price Prediction</h1>
			
			</div>
			"""

def main():
	stc.html(html_temp)

	menu = ["Home", "Data Analysis", "Prediction", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":
		img1 = Image.open("IMG\Realty_Growth.jpg")
		st.image(img1)
		st.write("""
				### Thinking Ahead
				Real estate prices are deeply cyclical and much of it is dependent on factors you can't control.
				Whether you plan on buying a new property or want to use the equity in your home for other expenses,
				it is important to analyze both broader market conditions and your specific property
				to determine how the home's value may fare over the course of time.
				
				### Real Estate Price Prediction ML App
				##### 1. This App predict the price of property.
				##### 2. Estimate your budget as per your requirements.
				""")
	elif choice=="Data Analysis":
		run_eda_app()
	elif choice == "Prediction":
		run_ml_app()
	else:
		st.subheader("About :")
		
		socials = ["LinkedIn", "Github", "GMail","LeetCode"]
		linkedin = "https://www.linkedin.com"
		github = "https://github.com"
		mail = "maharshivishwas@gmail.com"
		Leetcode="https://leetcode.com/u/v1shwa1/"
		with st.expander("Check my Socials Links"):
			a = st.selectbox("Socials", socials)
			if a =="LinkedIn":
				st.write(linkedin)
			elif a =="Github":
				st.write(github)
			elif a=="GMail":
				st.write(mail)
			elif a=="LeetCode":
				st.write(Leetcode)
		st.write("### Thanks You... ")

main()