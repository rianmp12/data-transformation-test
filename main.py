import pdfplumber
import pandas as pd
import os
import zipfile

def extract_tables_from_pdf(pdf_file):
    todas_tabelas = []

    with pdfplumber.open(pdf_file) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                df = pd.DataFrame(tabela[1:], columns=tabela[0])
                todas_tabelas.append(df)

    if todas_tabelas:
        return pd.concat(todas_tabelas, ignore_index=True)
    else:
        return pd.DataFrame()

def replace_abbreviations_and_clean(df):

    df = df.astype(str).apply(lambda col: col.str.replace('\n', ' ', regex=False))

    # Limpa e normaliza os nomes das colunas
    df.columns = [
        col.replace('\n', '_')
           .replace("á", "a")
           .replace("OD", "SEG_ODONTOLOGICA")
           .replace("AMB", "SEG_AMBULATORIAL")
           .strip()
        for col in df.columns
    ]

    return df

def save_and_compress_csv(df, csv_file, zip_file):
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    df.to_csv(csv_file, sep=';', index=False, encoding='utf-8-sig')

    with zipfile.ZipFile(zip_file, "w") as zipf:
        zipf.write(csv_file, arcname=os.path.basename(csv_file))

    print(f"CSV saved and compressed at: {zip_file}")

if __name__ == "__main__":
    pdf_path = "./downloads/attachment_1.pdf"  # Anexo I
    csv_path = "./csv_path/table_rol.csv"
    zip_path = "./output/Teste_Rian.zip"
    df_final = extract_tables_from_pdf(pdf_path)

    if not df_final.empty:
        df_final = replace_abbreviations_and_clean(df_final)
        save_and_compress_csv(df_final, csv_path, zip_path)
    else:
        print("No table was found in the PDF.")