# for testing receipt geenration 
import streamlit as st
from fpdf import FPDF
import base64

# Function to create the PDF
def create_pdf(name, address, total_price):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add content to the PDF
    pdf.cell(200, 10, "Invoice", 0, 1, 'C')
    pdf.cell(200, 10, f"Name: {name}", 0, 1, 'L')
    pdf.cell(200, 10, f"Address: {address}", 0, 1, 'L')
    # pdf.cell(200, 10, f"items ordered: {orders}", 0, 1, 'L')
    pdf.cell(200, 10, f"Total Price: ${total_price}", 0, 1, 'L')
    
    pdf_output = pdf.output(dest='S').encode('latin-1')
    return pdf_output

# Streamlit app
st.title("PDF Generator")

name = st.text_input("Name")
address = st.text_area("Address")
total_price = st.number_input("Total Price", min_value=0.0, step=0.01)

pdf_output = create_pdf(name, address, total_price)
st.download_button(label="Download PDF",
                   data=pdf_output,
                   file_name="invoice.pdf",
                   mime="application/pdf",
                   key="download_pdf")  # Add this key argument

