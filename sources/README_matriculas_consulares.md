# Matrículas consulares alemãs — artefatos de pesquisa

Esta pasta contém cópias de trabalho das listas de nomes de matrículas consulares remanescentes disponibilizadas pelo **Ministério Federal das Relações Externas da Alemanha** na página oficial de [Matrícula Consular](https://brasil.diplo.de/br-pt/servicos/nacionalidade/matriculaconsular-2602058). Os PDFs e planilhas foram baixados para pesquisa genealógica do ramo Schell; a procedência institucional e a data de acesso devem ser mantidas junto com qualquer uso futuro.

## Arquivos oficiais

As listas abrangem Porto Alegre A–F, G–K, L–R e S–Z; Belém; Joinville; Juiz de Fora; Recife; Rio de Janeiro; Santos; e São Paulo A–K e L–Z. As listas de Porto Alegre, Santos e São Paulo são PDFs escaneados. As listas de Belém, Joinville, Juiz de Fora, Recife e Rio de Janeiro são planilhas.

## Derivados

Os diretórios `matricula_poa_a-f_pages`, `matricula_poa_g-k_pages` e `matricula_poa_l-r_pages` contêm páginas PNG renderizadas a partir dos PDFs oficiais de Porto Alegre. Os arquivos TXT correspondentes contêm OCR produzido com Tesseract, usando alemão e inglês. O relatório `matricula_poa_ocr_hits_a_r.txt` registra as ocorrências localizadas pelo padrão nominal.

O arquivo `matriculas_planilhas_busca_variantes.txt` registra a busca automática nas planilhas. Os scripts reprodutíveis estão em `../scripts/ocr_matricula_porto_alegre.py` e `../scripts/search_consular_spreadsheets.py`.

## Critério de busca e limitações

Foram pesquisadas, entre outras, as variantes `Schell`, `Schnell`, `Schel`, `Shell`, `Nicolaus`, `Nikolaus`, `Nicolau`, `Johann`, `Johannes`, `Karl`, `Carlos` e `Becker`. No OCR dos quatro blocos de Porto Alegre não foi localizada ocorrência do sobrenome Schell/Schnell/Schel/Shell. Isso é um **resultado negativo limitado**: as listas são remanescentes, o OCR pode falhar em manuscritos e nomes podem aparecer com abreviações ou grafias inesperadas. A inspeção visual integral e a consulta no invenio permanecem métodos complementares.

A página oficial informa que a pesquisa também pode ser feita no [invenio](https://politisches-archiv.diplo.de/invenio/main.xhtml), sem necessidade de cadastro, e que outros documentos emitidos por autoridades alemãs podem ser relevantes quando a matrícula não é localizada. Nenhum documento privado, credencial, endereço residencial ou conteúdo de sessão foi incluído nesta pasta.
