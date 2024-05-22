import streamlit as st 
from  recipt_generator import create_pdf

st.title("PDF Generator")

name = st.text_input("Name")
address = st.text_area("Address")
total_price = st.number_input("Total Price", min_value=0.0, step=0.01)

if st.button("Generate PDF"):
    pdf_output = create_pdf(name, address, total_price)
    st.download_button(label="Download PDF",
                       data=pdf_output,
                       file_name="invoice.pdf",
                       mime="application/pdf")
    st.success("PDF generated and ready for download!")

