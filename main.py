import streamlit as st
from PIL import Image

st.set_page_config(page_title="imagefounder", page_icon="😀")

Image1 = Image.open("download.jpeg", "r")
Image2 = Image.open("Image.png", "r")
Image3 = Image.open("Imag2.png", "r")
Image4 = None
Image5 = None
Image6 = None
Image7 = None

def main():
    if Image1:
        st.image(Image1)
    if Image2:
        st.image(Image2)
    if Image3:
        st.image(Image3)
    if Image4:
        st.image(Image4)
    if Image5:
        st.image(Image5)
    if Image6:
        st.image(Image6)
    if Image7:
        st.image(Image7)
if __name__ == "__main__":
    main()