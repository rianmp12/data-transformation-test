# Teste de Transformação de Dados

Este projeto em Python realiza a extração de dados de um PDF (Anexo I do Rol de Procedimentos da ANS), estrutura os dados em formato tabular, realiza substituições conforme legenda e exporta para CSV compactado em `.zip`.

---

## 📁 Estrutura do Projeto

- `downloads/`: pasta onde o Anexo I está salvo.
- `csv_path/`: pasta onde o arquivo `.csv` será gerado.
- `output/`: pasta onde o arquivo `.zip` será gerado.
- `requirements.txt`: bibliotecas necessárias com versões fixas.
- `main.py`: script principal com toda a lógica.

---

## 🛠️ Requisitos

- Python 3.12

## ▶️ Como executar

### 1. Clonar o repositório

```bash
https://github.com/rianmp12/data-transformation-test.git
cd data-transformation-test
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # No Linux/macOS
venv\Scripts\activate      # No Windows
```

### 3. Instalar as depedências

```bash
pip install -r requirements.txt
```
As versões das bibliotecas estão fixadas no `requeriments.txt` para evitar problemas com atualiazações futuras.

### 4. Executar o script

```bash
python main.py
```

## 📒 Notebook de visualização

Foi adicionado um notebook simples em `notebooks/demonstracao_dados.ipynb` apenas para demonstrar a leitura e visualização básica dos dados extraídos do CSV.

Este notebook não faz parte da lógica principal do teste e serve apenas como apoio.

## 📦 Bibliotecas utilizadas

- `pdfplumber` - Utilizada para abrir o PDF e extrair tabelas de forma estruturada.
- `pandas` - Usada para manipulação e estruturação dos dados em formato tabular.
- `zipfile` - Para compactar o arquivo CSV gerado.
- `os` - Para lidar com criação de diretórios e caminhos de arquivos.

## ✅ Requisitos atendidos

- Leitura do PDF do Anexo I do Rol de Procedimentos da ANS.
- Extração de todas as tabelas do documento.
- Substituição das abreviações nas colunas OD e AMB conforme legenda:
  - OD → Seg. Odontologica
  - AMB → Seg. Ambulatorial
- Exportação dos dados em arquivo `.csv`.
- Compactação do arquivo `.csv` em um arquivo `.zip` com nome personalizado.
