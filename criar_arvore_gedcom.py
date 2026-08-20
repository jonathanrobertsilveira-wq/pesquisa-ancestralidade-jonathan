from pathlib import Path
import csv

OUT = Path('/home/ubuntu/gedcom_pesquisa_jonathan')
OUT.mkdir(parents=True, exist_ok=True)

people = {
    'I1': {'name': 'Jonathan Robert /Silveira De Souza/', 'sex': 'M', 'fsid': 'GK15-TLV', 'status': 'referência da pesquisa; identidade informada pelo usuário/árvore FamilySearch', 'notes': ['Pessoa de referência da árvore independente. Nenhuma alteração foi feita na árvore original do FamilySearch.']},
    'I2': {'name': 'Valdeci Kenes /de Souza/', 'sex': 'M', 'fsid': 'P4KK-B9S', 'status': 'hipótese derivada da árvore FamilySearch', 'notes': ['Filiação a Rosalvino Schell de Souza e Carolina Augusta Kenes de Souza ainda não confirmada por registro primário.']},
    'I3': {'name': 'Ana /Paula/', 'sex': 'F', 'fsid': 'P42Q-ZRT', 'status': 'hipótese derivada da árvore FamilySearch', 'notes': ['Cônjuge de Valdeci conforme árvore; nome incompleto e sem confirmação documental.']},
    'I4': {'name': 'Rosalvino Schell /de Souza/', 'sex': 'M', 'fsid': 'P4KK-1QH', 'status': 'hipótese de identidade e filiação; eventos ainda sem certidão primária lida', 'birth': ('06 OCT 1940', 'Tapes, Rio Grande do Sul, Brasil'), 'death': ('17 OCT 2014', 'Guaíba, Rio Grande do Sul, Brasil'), 'notes': ['Nascimento e óbito vêm do cartão FamilySearch e permanecem sem fontes diretas lidas.', 'A certidão de nascimento de Rosalvino é prioridade documental.', 'Buscas nominais FamilySearch civil em 1940, com Schell, Schel e apenas Rosalvino, retornaram zero; faixa 1938–1942 produziu homônimos sem correspondência a Tapes/Guaíba ou aos pais Raimundo/Alicia.', 'Busca APERS em 1940 e ampliada entre 1929–1948 não encontrou Rosalvino Schel/Schell em Tapes, Guaíba ou Cerro Grande.']},
    'I5': {'name': 'Carolina Augusta Kenes /de Souza/', 'sex': 'F', 'fsid': 'P42Q-FT6', 'status': 'hipótese derivada da árvore FamilySearch', 'notes': ['Cônjuge de Rosalvino conforme árvore. O óbito indexado de José Maria confirma Carolina no conjunto familiar, mas não confirma todos os dados biográficos.']},
    'I6': {'name': 'Raimundo José /de Souza/', 'sex': 'M', 'fsid': 'GV4D-D91', 'status': 'hipótese de filiação; pessoa aparece em fonte civil indexada', 'birth': ('1914', None), 'death': ('1983', None), 'notes': ['A árvore o apresenta como pai de Rosalvino. O óbito de Manoel de 1941 menciona Raimundo, mas a filiação de Rosalvino ainda não foi lida em fonte primária.', 'Buscas APERS e FamilySearch civil/católica não localizaram casamento indexado com Alicia Schell em 1930–1945; a Caixa 20 de habilitações de Tapes está com imagem restrita.']},
    'I7': {'name': 'Alicia Schell /de Souza/', 'sex': 'F', 'fsid': 'GV54-K3Q', 'status': 'hipótese derivada da árvore FamilySearch', 'notes': ['Cônjuge de Raimundo conforme árvore; casamento em Cerro Grande/Tapes ainda não localizado.', 'Busca exata Alicia Schell no APERS retornou zero; os resultados de Alicia em Tapes eram homônimos Lícia/Acácia. FamilySearch civil e católico também retornaram zero para o casal.']},
    'I8': {'name': 'Manoel José /de Souza/', 'sex': 'M', 'fsid': 'GV4D-FLS', 'status': 'evento de óbito confirmado por índice; filiação de Raimundo ainda não confirmada', 'birth': ('1879', None), 'death': ('21 FEB 1941', 'Barão do Triunfo, São Jerônimo, Rio Grande do Sul, Brasil'), 'notes': ['A árvore o apresenta como pai de Raimundo e cônjuge de Maria Candida Tavares. O índice civil confirma o óbito e menciona Raimundo, mas a imagem manuscrita ainda não foi lida em alta resolução.']},
    'I9': {'name': 'Maria Candida /Tavares/', 'sex': 'F', 'fsid': 'GV46-7JK', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1895', None), 'death': ('1956', None), 'notes': ['Cônjuge e possível mãe de Raimundo conforme árvore; ainda sem certidão primária lida.']},
    'I10': {'name': 'Alvino Paulino /de Souza/', 'sex': 'M', 'fsid': 'LZGD-TYJ', 'status': 'nascimento e casamento confirmados por habilitação APERS; datas da árvore conflitam', 'birth': ('23 FEB 1897', 'Americana, 3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'notes': ['A árvore FamilySearch indicava 1891–1977; a certidão anexada ao APERS nº 180190 registra nascimento em 23/02/1897.', 'Filho legítimo de Geremias de Souza e Anna Joaquina Paulino de Souza.', 'Avós paternos: Alexandrino de Oliveira e Souza e Felicia Rodrigues de Souza. Avós maternos: Joaquim Paulino Tavares e Victoria Tavares.']},
    'I11': {'name': 'Rosalina /Schell/', 'sex': 'F', 'fsid': 'LXVC-28B', 'status': 'nascimento, pai e casamento confirmados por habilitação APERS; data da árvore conflita', 'birth': ('16 DEC 1906', 'Americana, 3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'notes': ['A árvore FamilySearch/MyHeritage indicava 1899–1993; a certidão anexada ao APERS nº 180190 registra nascimento em 16/12/1906.', 'Filha legítima de Regino Schell. O nome da mãe não ficou legível com segurança na leitura atual.', 'Depois do casamento, passou a assinar Rosalina Schell de Souza.', 'Buscas nominais FamilySearch nas coleções civil 3741255 e católica 2177295, em 1906, retornaram zero resultados; waypoints de Tapes, Camaquã e São Jerônimo não cobrem batismo de 1906.', 'A certidão anexada ao APERS menciona Carlos Schell e Anna Schell como avós; o papel exato deles na linha e sua ligação a Regino ainda precisam ser confirmados em assento original.']},
    'I12': {'name': 'Geremias /de Souza/', 'sex': 'M', 'status': 'pai de Alvino confirmado pela certidão anexada ao APERS nº 180190', 'notes': ['Nenhum identificador FamilySearch foi localizado na pesquisa atual. Origem europeia ainda não demonstrada.']},
    'I13': {'name': 'Anna Joaquina Paulino /de Souza/', 'sex': 'F', 'status': 'mãe de Alvino confirmada pela certidão anexada ao APERS nº 180190', 'notes': ['Nenhum identificador FamilySearch foi localizado na pesquisa atual.']},
    'I14': {'name': 'Regino /Schell/', 'sex': 'M', 'status': 'pai de Rosalina confirmado pela certidão anexada ao APERS nº 180190', 'notes': ['Primeiro ancestral Schell nominalmente confirmado na linha de Rosalina. Origem europeia ainda não demonstrada.', 'Buscas APERS por Regino/Regino Schell/Schell entre 1890 e 1968 e buscas FamilySearch civil/católica por Regino Schell não localizaram registro indexado em Tapes/Cerro Grande.']},
    'I15': {'name': '[Mãe de Rosalina não identificada]', 'sex': 'F', 'status': 'placeholder; nome não legível na certidão anexada ao APERS', 'notes': ['Não tratar como pessoa identificada. Deve ser substituída pelo nome do assento original de nascimento de Rosalina.']},
    'I16': {'name': 'Alexandrino de Oliveira /e Souza/', 'sex': 'M', 'status': 'avô paterno de Alvino, conforme certidão anexada ao APERS nº 180190', 'notes': ['Origem europeia não demonstrada.']},
    'I17': {'name': 'Felicia /Rodrigues de Souza/', 'sex': 'F', 'status': 'avó paterna de Alvino, conforme certidão anexada ao APERS nº 180190', 'notes': ['Origem europeia não demonstrada.']},
    'I18': {'name': 'Joaquim Paulino /Tavares/', 'sex': 'M', 'status': 'avô materno de Alvino, conforme certidão anexada ao APERS nº 180190', 'notes': ['Origem europeia não demonstrada.']},
    'I19': {'name': 'Victoria /Tavares/', 'sex': 'F', 'status': 'avó materna de Alvino, conforme certidão anexada ao APERS nº 180190', 'notes': ['Origem europeia não demonstrada.']},
    'I20': {'name': 'José Maria Kenes /de Souza/', 'sex': 'M', 'status': 'filho de Rosalvino e Carolina confirmado por registro de óbito indexado', 'birth': ('13 MAR 1971', 'Guaíba, Rio Grande do Sul, Brasil'), 'death': ('29 MAR 1971', 'Guaíba, Rio Grande do Sul, Brasil'), 'notes': ['Registro FamilySearch informa 16 dias de idade, filho de Rosalvino Schel de Souza; Carolina aparece no conjunto familiar.']},
    'I21': {'name': 'Flauliano Brasil /Kenes/', 'sex': 'M', 'fsid': 'P7NS-NVL', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1923', None), 'death': ('2001', None), 'notes': ['Casamento com Eva Silveira indicado em 28/07/1948, Capela Velha, Camaquã; sem confirmação documental.']},
    'I22': {'name': 'Eva /Silveira/', 'sex': 'F', 'fsid': 'PH4B-XS2', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1927', None), 'notes': ['Não confundir com Eva Pereira da Silveira, homônima distinta identificada no APERS.']},
    'I23': {'name': 'Manoel Geraldo /Kenes/', 'sex': 'M', 'fsid': 'PMXJ-2SR', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1904', None), 'notes': ['Ramo lateral da árvore; casamento com Dorvalina indicado em Capela Velha em 1948, sem confirmação documental.']},
    'I24': {'name': 'Dorvalina Ferreira /Kenes/', 'sex': 'F', 'fsid': 'G56B-32T', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1905', None), 'death': ('1939', None)},
    'I25': {'name': 'Antonio Manoel /Silveira/', 'sex': 'M', 'fsid': 'PH4B-JD1', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1897', None), 'notes': ['Ramo lateral da árvore; relação não confirmada documentalmente.']},
    'I26': {'name': 'Tomazia /Silveira/', 'sex': 'F', 'fsid': 'PH4B-ZRX', 'status': 'hipótese derivada da árvore FamilySearch', 'birth': ('1898', None)},
    'I27': {'name': 'Alvina /Schell/', 'sex': 'F', 'status': 'filha de Rosalina Schell confirmada por habilitação APERS 180603; identidade separada da Rosalina de 1906', 'birth': ('29 JUN 1926', '3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'notes': ['Habilitação APERS nº 180603 confirma Alvina como filha ilegítima de Rosalina Schell e registra o casamento com Ademar Antunes Leal em 04/10/1947.', 'A leitura ampliada do atestado indica a avó como Regina Schell; não ler como Regino sem nova confirmação.', 'Não associar esta Alvina à Rosalina esposa de Alvino sem prova de identidade.']},
    'I28': {'name': 'Ademar Antunes /Leal/', 'sex': 'M', 'status': 'cônjuge de Alvina Schell confirmado por habilitação APERS 180603', 'birth': ('12 AUG 1926', '3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'notes': ['Filho legítimo de Veríssimo Antunes Leal e Maria Goulart Leal, conforme petição do processo 180603.']},
    'I29': {'name': 'Celanira /Schell/', 'sex': 'F', 'status': 'filha de Rosalina Schell confirmada por habilitação APERS 180674; identidade separada da Rosalina de 1906', 'birth': ('20 AUG 1934', '3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'notes': ['Certidão de nascimento nº 328, livro 13-A, e termo de consentimento assinado por Rosalina em 12/10/1953.', 'Habilitação APERS nº 180674 confirma o casamento com Cravilino Nogueira em 31/10/1953.', 'Não associar esta Celanira à linha de Jonathan sem prova de que sua mãe Rosalina é a mesma pessoa de 1906.']},
    'I30': {'name': 'Cravilino /Nogueira/', 'sex': 'M', 'status': 'cônjuge de Celanira Schell confirmado por habilitação APERS 180674', 'birth': ('04 OCT 1926', 'Rio Grande do Sul, Brasil'), 'notes': ['Filho legítimo de Ernesto José Nogueira e Hermínia Lopes Santos, conforme petição do processo 180674.']},
    'I31': {'name': 'Rosalina /Schell/ (mãe de Alvina e Celanira; identidade não resolvida)', 'sex': 'F', 'status': 'mãe de Alvina e Celanira confirmada em habilitações APERS; pessoa mantida separada da Rosalina de 1906', 'notes': ['Processos APERS 180603 e 180674 confirmam a maternidade, a residência em Vila Cerro Grande/Tapes e a presença de Rosalina em 1953.', 'A identidade, data de nascimento e eventual relação com Regino Schell não foram demonstradas.', 'A leitura de Regina Schell como avó de Alvina é apenas pista paleográfica.']},
}

families = [
    {'id': 'F1', 'husb': 'I2', 'wife': 'I3', 'children': ['I1'], 'status': 'hipótese da árvore FamilySearch', 'note': 'Valdeci e Ana Paula são apresentados como pais de Jonathan; relação ainda não foi validada com certidão.'},
    {'id': 'F2', 'husb': 'I4', 'wife': 'I5', 'children': ['I2'], 'status': 'hipótese da árvore FamilySearch', 'note': 'A árvore apresenta Rosalvino e Carolina como pais de Valdeci. O óbito de José Maria confirma que o casal teve ao menos um filho, mas não prova especificamente Valdeci.'},
    {'id': 'F3', 'husb': 'I6', 'wife': 'I7', 'children': ['I4'], 'status': 'hipótese da árvore FamilySearch', 'note': 'Raimundo e Alicia são apresentados como pais de Rosalvino; casamento em Cerro Grande/Tapes ainda não localizado.'},
    {'id': 'F4', 'husb': 'I8', 'wife': 'I9', 'children': ['I6'], 'status': 'hipótese da árvore FamilySearch', 'note': 'Manoel e Maria Candida são apresentados como pais de Raimundo. O óbito de Manoel menciona Raimundo, mas a filiação precisa ser lida na imagem original.'},
    {'id': 'F5', 'husb': 'I10', 'wife': 'I11', 'status': 'confirmada por fonte primária', 'marriage': ('17 APR 1955', 'Vila Cerro Grande, 3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'note': 'Processo APERS nº 180190. A petição registra que Rosalina passaria a assinar Rosalina Schell de Souza. O índice CSV exibe 01/01/1955 como data-padrão do ano.'},
    {'id': 'F6', 'husb': 'I12', 'wife': 'I13', 'children': ['I10'], 'status': 'filiação confirmada por fonte primária', 'note': 'Certidão de nascimento de Alvino anexada ao APERS nº 180190.'},
    {'id': 'F7', 'husb': 'I14', 'wife': 'I15', 'children': ['I11'], 'status': 'pai confirmado; mãe placeholder', 'note': 'Certidão de nascimento de Rosalina anexada ao APERS nº 180190. O nome da mãe não ficou legível; não tratar o placeholder como identificação definitiva.'},
    {'id': 'F8', 'husb': 'I21', 'wife': 'I22', 'status': 'hipótese da árvore FamilySearch', 'marriage': ('28 JUL 1948', 'Capela Velha, Camaquã, Rio Grande do Sul, Brasil'), 'note': 'Casamento indicado pela árvore; sem confirmação documental. Não confundir Eva com homônima Eva Pereira da Silveira.'},
    {'id': 'F9', 'husb': 'I23', 'wife': 'I24', 'status': 'hipótese da árvore FamilySearch', 'marriage': ('28 JUL 1948', 'Capela Velha, Camaquã, Rio Grande do Sul, Brasil'), 'note': 'Ramo lateral; casamento indicado pela árvore, sem confirmação documental.'},
    {'id': 'F10', 'husb': 'I25', 'wife': 'I26', 'status': 'hipótese da árvore FamilySearch', 'note': 'Ramo lateral; relação sem confirmação documental.'},
    {'id': 'F11', 'wife': 'I31', 'children': ['I27', 'I29'], 'status': 'maternidade confirmada; identidade da mãe não resolvida', 'note': 'Processos APERS 180603 e 180674 confirmam Rosalina Schell como mãe de Alvina e Celanira. A pessoa I31 é uma hipótese separada e não deve ser mesclada com I11, Rosalina esposa de Alvino.'},
    {'id': 'F12', 'husb': 'I28', 'wife': 'I27', 'status': 'confirmada por habilitação APERS 180603', 'marriage': ('04 OCT 1947', 'Vila Cerro Grande, 3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'note': 'Livro 6, folha 63, termo 400.'},
    {'id': 'F13', 'husb': 'I30', 'wife': 'I29', 'status': 'confirmada por habilitação APERS 180674', 'marriage': ('31 OCT 1953', 'Vila Cerro Grande, 3º distrito de Tapes, Rio Grande do Sul, Brasil'), 'note': 'Livro 7-A, folha 198, termo 723.'},
]

sources = {
    'S1': {'title': 'APERS — Habilitação de casamento de Alvino Paulino de Souza e Rosalina Schell, processo interno 180190', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://secweb.procergs.com.br/aap/ObtemDadosServlet?metodo=verArquivoPDF&NRO_INT_DOCUMENTO=180190', 'local': '/home/ubuntu/upload/apers_processo_180190.pdf', 'quality': 'Fonte primária; PDF de 18 páginas com certidões e tramitação judicial.'},
    'S2': {'title': 'APERS — Exportação da busca por Schell', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://buscadocumentos.apers.rs.gov.br/lista-documentos?semHeaders=true', 'local': '/home/ubuntu/upload/exportacao-1787179224315.csv', 'quality': 'Índice estruturado; revelou NRO_INT_DOCUMENTO=180190 e o link do PDF.'},
    'S3': {'title': 'Árvore FamilySearch — Jonathan Robert Silveira De Souza', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/tree/pedigree/landscape/GK15-TLV', 'quality': 'Fonte derivada; relações e datas a partir dos avós permanecem hipóteses.'},
    'S4': {'title': 'MyHeritage — Rosalina Schell', 'auth': 'MyHeritage', 'url': 'https://www.myheritage.no/names/rosalina_schell', 'quality': 'Fonte derivada; reproduz resumo de árvore e não substitui registro original.'},
    'S5': {'title': 'FamilySearch — Óbito de José Maria Kenes de Souza, 29/03/1971', 'auth': 'FamilySearch', 'url': 'https://familysearch.org/ark:/61903/1:1:6YPM-F1JQ', 'quality': 'Registro civil indexado; confirma José Maria como filho de Rosalvino e Carolina no conjunto familiar.'},
    'S6': {'title': 'FamilySearch — Óbito de Manoel José de Souza, 21/02/1941', 'auth': 'FamilySearch', 'url': 'https://familysearch.org/ark:/61903/1:1:6RM8-HCHX', 'quality': 'Registro civil indexado; evento confirmado, parentesco de Raimundo ainda parcial.'},
    'S7': {'title': 'FamilySearch — Imagem original do óbito de Barão do Triunfo, filme 004208553', 'auth': 'FamilySearch', 'url': 'https://familysearch.org/ark:/61903/3:1:3QS7-99GW-1966', 'quality': 'Imagem original localizada; manuscrito ainda não transcrito integralmente.'},
    'S8': {'title': 'FamilySearch — Rio Grande do Sul, Brazil, Civil Registration, 1810–2022', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/search/collection/3741255', 'quality': 'Coleção civil consultada nominalmente para Rosalina Schell em 1906; busca exata e busca sem localidade retornaram zero resultados.'},
    'S9': {'title': 'FamilySearch — Rio Grande do Sul, Brazil, Catholic Church Records, 1738–1952', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/search/collection/2177295', 'quality': 'Coleção católica consultada nominalmente e por imagens; busca de Rosalina em 1906 retornou zero e waypoints de Tapes, Camaquã e São Jerônimo não cobrem batismo de 1906.'},
    'S10': {'title': 'APERS — Busca pública por Rosalvino em 1940 e 1929–1948', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true', 'quality': 'Busca nominal estruturada; homônimos foram descartados e não houve ocorrência em Tapes, Guaíba, Cerro Grande ou Schel/Schell.'},
    'S11': {'title': 'FamilySearch — Busca civil de Rosalvino Schell/Schel, 1940', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/search/collection/3741255', 'quality': 'Busca nominal exata e por prenome; Schell, Schel e apenas Rosalvino retornaram zero em 1940. A faixa 1938–1942 retornou homônimos.'},
    'S12': {'title': 'FamilySearch — Busca de casamento Raimundo Souza + Alicia Schell', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/search/collection/3741255', 'quality': 'Consultas civil e católica, com e sem cônjuge/local, retornaram zero resultados para 1930–1945.'},
    'S13': {'title': 'APERS — Busca de Raimundo/Alicia/Schell em 1929–1948', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true', 'quality': 'Busca estruturada: Alicia Schell zero; Tapes exibiu apenas homônimos Lícia/Acácia e Raimundos sem Alicia; imagens das caixas S ficaram restritas no FamilySearch.'},
    'S14': {'title': 'APERS — Buscas históricas por Regino, Carlos Schell e Anna Schell', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true', 'quality': 'Consultas entre 1870 e 1968; sem ocorrência de Regino/Schell no Cartório de Tapes ou Cerro Grande. Homônimos de outras comarcas foram descartados.'},
    'S15': {'title': 'FamilySearch — Busca de Regino Schell nas coleções civil e católica', 'auth': 'FamilySearch', 'url': 'https://www.familysearch.org/en/search/collection/3741255', 'quality': 'Regino Schell retornou zero na coleção civil 3741255 e na coleção católica 2177295.'},
    'S16': {'title': 'APERS — Habilitação de casamento de Ademar Antunes Leal e Alvina Schell, processo 180603', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://secweb.procergs.com.br/aap/ObtemDadosServlet?metodo=verArquivoPDF&NRO_INT_DOCUMENTO=180603', 'local': '/home/ubuntu/gedcom_pesquisa_jonathan/apers_processo_180603.pdf', 'quality': 'Fonte primária; PDF de 20 páginas com filiação de Alvina a Rosalina Schell, avó lida como Regina Schell e casamento em 04/10/1947.'},
    'S17': {'title': 'APERS — Habilitação de casamento de Cravilino Nogueira e Celanira Schell, processo 180674', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://secweb.procergs.com.br/aap/ObtemDadosServlet?metodo=verArquivoPDF&NRO_INT_DOCUMENTO=180674', 'local': '/home/ubuntu/gedcom_pesquisa_jonathan/apers_processo_180674.pdf', 'quality': 'Fonte primária; PDF de 20 páginas com filiação de Celanira a Rosalina Schell, termo de consentimento materno e casamento em 31/10/1953.'},
    'S18': {'title': 'APERS — Acervo de Registro Civil', 'auth': 'Arquivo Público do Estado do Rio Grande do Sul', 'url': 'https://www.apers.rs.gov.br/acervo-registro-civil', 'quality': 'Fonte institucional; livros civis de 1929–1975 e habilitações de casamento de 1890–1985, com fundos de Tapes, Camaquã, Guaíba e São Jerônimo.'},
    'S19': {'title': 'Ministério Federal das Relações Exteriores — documentos de antepassados alemães', 'auth': 'República Federal da Alemanha', 'url': 'https://brasil.diplo.de/br-pt/servicos/nacionalidade/antepassados-2602086', 'quality': 'Fonte institucional; indica matrículas consulares, Instituto Genealógico do RS e Arquivo Nacional como rotas de pesquisa, sem provar origem da família.'},
    'S20': {'title': 'Arquivo Nacional — Entrada de Estrangeiros', 'auth': 'Arquivo Nacional', 'url': 'https://www.gov.br/arquivonacional/pt-br/servicos/acervos/copy_of_acervos-mais-consultados/entrada-de-estrangeiros', 'quality': 'Fonte institucional; descreve SIAN, listas de passageiros, RNE e naturalização como rotas para imigrantes.'},
}

# GEDCOM generation
lines = []
lines += ['0 HEAD', '1 SOUR Manus AI', '2 VERS 1.0', '1 NAME Árvore de pesquisa independente — Jonathan Robert Silveira De Souza', '1 NOTE Esta árvore é uma reconstrução de pesquisa. Não altera a árvore original do FamilySearch.', '1 DATE 19 AUG 2026', '1 GEDC', '2 VERS 5.5.1', '2 FORM LINEAGE-LINKED', '1 CHAR UTF-8', '1 LANG Portuguese', '1 DEST OTHER']

def add_note(level, text):
    # Keep GEDCOM lines readable and under common line-length limits.
    words = text.split()
    if not words:
        return [f'{level} NOTE']
    out = []
    current = ''
    first = True
    for word in words:
        candidate = (current + ' ' + word).strip()
        if len(candidate) > 210 and current:
            out.append(f'{level} {"NOTE" if first else "CONT"} {current}')
            first = False
            current = word
        else:
            current = candidate
    if current:
        out.append(f'{level} {"NOTE" if first else "CONT"} {current}')
    return out

for sid, s in sources.items():
    lines += [f'0 @{sid}@ SOUR', f'1 TITL {s["title"]}', f'1 AUTH {s["auth"]}', f'1 NOTE URL: {s["url"]}']
    if s.get('local'):
        lines.append(f'1 NOTE Arquivo local: {s["local"]}')
    lines += add_note(1, s['quality'])

for pid, p in people.items():
    lines += [f'0 @{pid}@ INDI', f'1 NAME {p["name"]}', f'1 SEX {p["sex"]}']
    if p.get('fsid'):
        lines.append(f'1 NOTE FamilySearch ID: {p["fsid"]}')
    lines += add_note(1, f'Status: {p["status"]}.')
    if p.get('birth'):
        date, place = p['birth']
        lines.append('1 BIRT')
        lines.append(f'2 DATE {date}')
        if place:
            lines.append(f'2 PLAC {place}')
        if p.get('fsid'):
            lines.append('2 SOUR @S3@')
    if p.get('death'):
        date, place = p['death']
        lines.append('1 DEAT')
        lines.append(f'2 DATE {date}')
        if place:
            lines.append(f'2 PLAC {place}')
        if p.get('fsid'):
            lines.append('2 SOUR @S3@')
    for note in p.get('notes', []):
        lines += add_note(1, note)
    # Relevant sources by individual
    if pid in {'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19'}:
        lines.append('1 SOUR @S1@')
    if pid == 'I11':
        lines.append('1 SOUR @S8@')
        lines.append('1 SOUR @S9@')
    if pid == 'I4' or pid == 'I5':
        lines.append('1 SOUR @S3@')
    if pid == 'I4':
        lines.append('1 SOUR @S10@')
        lines.append('1 SOUR @S11@')
    if pid in {'I6', 'I7'}:
        lines.append('1 SOUR @S12@')
        lines.append('1 SOUR @S13@')
    if pid in {'I11', 'I14', 'I15'}:
        lines.append('1 SOUR @S14@')
        lines.append('1 SOUR @S15@')
    if pid in {'I27', 'I28', 'I31'}:
        lines.append('1 SOUR @S16@')
    if pid in {'I29', 'I30', 'I31'}:
        lines.append('1 SOUR @S17@')
    if pid == 'I20':
        lines.append('1 SOUR @S5@')
    if pid in {'I6', 'I8', 'I9'}:
        lines.append('1 SOUR @S3@')
        lines.append('1 SOUR @S6@')
    if pid in {'I21','I22','I23','I24','I25','I26'}:
        lines.append('1 SOUR @S3@')

for f in families:
    lines += [f'0 @{f["id"]}@ FAM']
    if f.get('husb'):
        lines.append(f'1 HUSB @{f["husb"]}@')
    if f.get('wife'):
        lines.append(f'1 WIFE @{f["wife"]}@')
    for child in f.get('children', []):
        lines.append(f'1 CHIL @{child}@')
    if f.get('marriage'):
        lines.append('1 MARR Y')
        lines.append(f'2 DATE {f["marriage"][0]}')
        lines.append(f'2 PLAC {f["marriage"][1]}')
        if f['id'] == 'F5':
            lines.append('2 SOUR @S1@')
            lines.append('2 SOUR @S2@')
        elif f['id'] == 'F12':
            lines.append('2 SOUR @S16@')
        elif f['id'] == 'F13':
            lines.append('2 SOUR @S17@')
        else:
            lines.append('2 SOUR @S3@')
    lines += add_note(1, f'Status: {f["status"]}.')
    lines += add_note(1, f['note'])
    if f['id'] == 'F5':
        lines.append('1 NOTE A família derivada de MyHeritage menciona quatro filhas, mas nenhuma filha sem nome foi inserida como indivíduo até existir identificação documental.')

# Family links
for f in families:
    if f.get('husb'):
        lines.append(f'0 @LINK_{f["husb"]}_{f["id"]}@ NOTE_LINK')
# Write actual standard cross-references on individuals by inserting before next records is complex;
# append harmless custom notes documenting family membership for interoperability.
for f in families:
    for role in ('husb', 'wife'):
        pid = f.get(role)
        if pid:
            # A GEDCOM consumer generally uses FAMS; add a separate record-style line is invalid,
            # so we will patch the individual blocks below instead.
            pass

# Rebuild with FAMS/FAMC references by patching record blocks.
raw = '\n'.join(lines) + '\n'
for pid, p in people.items():
    # Remove temporary NOTE_LINK records later.
    pass
# Remove temporary invalid helper records.
raw = '\n'.join(line for line in raw.splitlines() if not line.startswith('0 @LINK_')) + '\n'
# Insert links after each individual block's last line before next 0 record.
record_lines = raw.splitlines()
family_by_person = {}
for f in families:
    for role in ('husb', 'wife'):
        if f.get(role):
            family_by_person.setdefault(f[role], []).append(('FAMS', f['id']))
    for child in f.get('children', []):
        family_by_person.setdefault(child, []).append(('FAMC', f['id']))
patched = []
for i, line in enumerate(record_lines):
    patched.append(line)
    if line.startswith('0 @') and line.endswith('@ INDI'):
        pid = line.split('@')[1]
        # links need to be inserted after all details, not right here
    if line.startswith('0 @') and line.endswith('@ INDI'):
        # Find next record and insert later using a separate pass.
        pass
final_lines = []
i = 0
while i < len(record_lines):
    line = record_lines[i]
    if line.startswith('0 @') and line.endswith('@ INDI'):
        pid = line.split('@')[1]
        final_lines.append(line)
        i += 1
        block = []
        while i < len(record_lines) and not record_lines[i].startswith('0 @'):
            block.append(record_lines[i])
            i += 1
        final_lines.extend(block)
        for tag, fid in family_by_person.get(pid, []):
            final_lines.append(f'1 {tag} @{fid}@')
    else:
        final_lines.append(line)
        i += 1

gedcom_path = OUT / 'arvore_pesquisa_jonathan.ged'
gedcom_path.write_text('\n'.join(final_lines) + '\n', encoding='utf-8')

# CSV inventory for auditability.
with (OUT / 'pessoas_evidencias.csv').open('w', encoding='utf-8', newline='') as fh:
    writer = csv.writer(fh, delimiter=';')
    writer.writerow(['id_gedcom', 'nome', 'familysearch_id', 'status', 'nascimento', 'local_nascimento', 'observacoes'])
    for pid, p in people.items():
        writer.writerow([pid, p['name'], p.get('fsid', ''), p['status'], p.get('birth', ('',''))[0], p.get('birth', ('',''))[1] or '', ' '.join(p.get('notes', []))])

# Source and methodology README.
readme = '''# Árvore de pesquisa independente — Jonathan Robert Silveira De Souza

Este diretório contém uma árvore GEDCOM independente, criada sem editar a árvore existente no FamilySearch. O arquivo GEDCOM separa fatos documentados, hipóteses derivadas da árvore antiga, conflitos de datas e placeholders que ainda exigem leitura de registros originais.

## Convenções de confiança

| Marca no GEDCOM | Significado |
|---|---|
| `Status: ... confirmado por fonte primária` | Relação ou evento apoiado por imagem/PDF de registro civil ou habilitação. |
| `Status: hipótese da árvore FamilySearch` | Dado reproduzido da árvore colaborativa, ainda não confirmado por documento primário. |
| `Status: ... conflito` | Há duas versões incompatíveis; a fonte primária atualmente preferida é indicada nas notas. |
| `placeholder` | Pessoa temporária criada para preservar uma lacuna documental; não deve ser tratada como identificação definitiva. |

## Fonte primária central

O processo **APERS nº 180190** contém 18 páginas e confirma o casamento de Alvino Paulino de Souza e Rosalina Schell em 17/04/1955, em Vila Cerro Grande, 3º distrito de Tapes. As certidões anexas registram Alvino nascido em 23/02/1897, filho de Geremias de Souza e Anna Joaquina Paulino de Souza, e Rosalina nascida em 16/12/1906, filha de Regino Schell. O nome da mãe de Rosalina ainda precisa ser recuperado no assento original.

## Conflitos preservados

A árvore antiga do FamilySearch/MyHeritage indicava Alvino em 1891 e Rosalina em 1899–1993. O GEDCOM preserva esses dados apenas nas notas de conflito, enquanto usa 23/02/1897 e 16/12/1906 como datas primárias preferidas no estado atual da pesquisa. Nenhuma alteração foi feita no FamilySearch.

## Próxima etapa

As buscas gratuitas nominais e os waypoints paroquiais consultados não localizaram o assento de nascimento de Rosalina em 1906; essa lacuna permanece explicitamente documentada. A busca nominal do nascimento de Rosalvino em 1940 foi concluída sem confirmação: APERS e FamilySearch retornaram apenas homônimos ou zero resultados. A busca do casamento de Raimundo e Alicia também terminou sem registro indexado; o casal permanece hipótese da árvore e as imagens das habilitações de Tapes estão restritas. As buscas por Regino, Carlos e Anna Schell não localizaram novos registros nem naturalidade europeia. A origem europeia permanece não comprovada; a próxima etapa é validar a árvore, preparar o relatório final de lacunas e deixar um roteiro seguro para solicitações institucionais gratuitas ou para a plataforma posterior. A origem europeia ainda não está comprovada.
'''
(OUT / 'LEIA-ME.md').write_text(readme, encoding='utf-8')
print(gedcom_path)
print(OUT / 'pessoas_evidencias.csv')
print(OUT / 'LEIA-ME.md')
