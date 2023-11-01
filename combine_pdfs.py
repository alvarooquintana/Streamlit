import streamlit as st 
import PyPDF2


output_pdf = 'documents/pdf_final.pdf'

def unir_pdf(output_path, documents):

    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)

    pdf_final.write(output_path)

st.image("assets/combine-pdf.png") 

st.header("Unir pdf")

st.subheader("Adjuntar pdfs para unir")

pdf_adjuntos = st.file_uploader(label=" ", accept_multiple_files=True)

unir = st.button(label="Une los Pdfs")

if unir:
    if len(pdf_adjuntos) <= 1:
        st.warning("Debes agregar mas de 1 pdf")
    else:

        unir_pdf(output_pdf,pdf_adjuntos)
        st.success("Desde aqui puede descargar el PDF final")

        with open(output_pdf, "rb") as file:
            pdf_data = file.read()

        st.download_button(label="Descarga el pdf", data=pdf_data, file_name="pdf_final.pdf")

