# Bloqueios e limitações da pesquisa genealógica

**Data do inventário:** 19 de agosto de 2026.  
**Critério de ordem:** primeiro o impacto sobre a confirmação de relações familiares e a origem europeia; depois o valor auxiliar; por fim as falhas já contornadas ou que não dependem de intervenção humana.

## Ordem de importância

| Ordem | Página ou sistema | Tipo | Impacto genealógico | Situação | Ação do usuário |
|---|---|---|---|---|---|
| 1 | [APERS — Pesquisa no Acervo](https://apers.rs.gov.br/pesquisa-acervo-plataforma-aap) e [serviço direto](https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true) | Falha técnica: incorporação por privacidade e `about:blank` após selecionar resultado | **Muito alto.** Afetava a imagem/metadados do processo de habilitação de casamento de Alvino Paulino de Souza + Rosalina Schell | **Resolvido para este processo: o CSV revelou `NRO_INT_DOCUMENTO=180190` e o PDF de 18 páginas foi baixado e lido.** Permanecem apenas dúvidas paleográficas sobre a mãe de Rosalina e a leitura completa do assento. | Nenhuma ação antirobô; continuar pelos livros de Tapes/Cerro Grande |
| 2 | [MyHeritage — Felippe Thomaz](https://www.myheritage.hu/names/felippe_thomaz) | **Security check / antirobô** | **Alto, mas derivado.** Pode revelar a possível família Thomaz/Schell e ajudar a localizar os pais de Rosalina; não substitui registro civil ou paroquial | **Resolvido pelo usuário; conteúdo lido, sem ligação comprovada com Rosalina** | Nenhuma ação agora |
| 3 | [FamilySearch — coleção de registros civis](https://www.familysearch.org/en/search/collection/3741255) | Falha técnica de autenticação e resultados caindo em `about:blank` | **Alto.** Impediu a busca nominal direta por Rosalvino e a navegação inicial por índices de nascimento, casamento e óbito | **Resolvido pela extensão para a página da coleção; algumas fichas públicas continuam sem renderizar** | Nenhuma ação imediata; manter a sessão autenticada |
| 4 | [FamilySearch — registro original do óbito de Manoel](https://www.familysearch.org/ark:/61903/3:1:3QS7-99GW-1966) | Renderização incompleta da imagem original | **Alto.** O índice lista Raimundo, Maria Candida e outros participantes; a imagem manuscrita pode confirmar a filiação de Raimundo e a linha Souza/Tavares | Parcialmente resolvido: o visualizador e o Image Index abriram, mas a imagem manuscrita não foi lida em alta resolução | Nenhuma ação antirobô identificada; se surgir CAPTCHA, concluir e avisar |
| 5 | [APERS — pesquisa por Rosalina em 1899](https://apers.rs.gov.br/pesquisa-acervo-plataforma-aap) | Grade dinâmica/virtualizada não expôs as linhas ao console | **Médio-alto.** Pode localizar nascimento, casamento ou óbito de Rosalina Schell, mas a consulta ampla retornou homônimos | Não resolvido | Nenhuma ação antirobô; tentar leitura visual/filtro do cartão de Tapes |
| 6 | [ANOREG/Corregedoria — cadastro do cartório de Tapes](https://www.anoreg.org.br/files/RS-5096-3295.pdf) | **CAPTCHA/visualização bloqueada** | **Médio-baixo.** Serve para confirmar dados administrativos do cartório, não para provar eventos familiares; fontes cadastrais alternativas já confirmaram o CNS e a abrangência | **Resolvido pelo PDF fornecido pelo usuário; dados cadastrais conferidos** | Nenhuma ação agora |
| 7 | [FamilySearch Wiki — Tapes](https://www.familysearch.org/en/wiki/Tapes,_Rio_Grande_do_Sul,_Brazil_Genealogy) | Interrupção antirobô na rota do navegador | **Médio-baixo.** Fornece orientação sobre coleções, paróquias e municípios, não o registro de uma pessoa | Contornado por extração textual; não é necessário repetir agora | Nenhuma ação, salvo se a página voltar a bloquear uma informação específica |
| 8 | [MyHeritage — Rosalina Schell](https://www.myheritage.no/names/rosalina_schell) | **Security check / antirobô**; depois Incapsula na extração textual | **Médio.** Liberou apenas um resumo derivado sobre Rosalina, Alvino e quatro filhas; a informação já foi capturada e não é prova primária | **Resolvido pelo usuário** no navegador; a extração textual continua bloqueada, mas não é necessária | Nenhuma ação agora |
| 9 | [FamilySearch — perfil direto de Rosalina](https://www.familysearch.org/en/tree/person/details/LXVC-28B) | Aviso de navegador não suportado e `about:blank` | **Médio.** Impediu ler pais e fontes do perfil `LXVC-28B`; o casamento de Rosalina já foi localizado independentemente no índice APERS | Não resolvido | Nenhuma ação antirobô; usar a árvore paisagem, fontes públicas e a habilitação APERS |
| 10 | [APERS — comunicado sobre habilitações de Tapes](https://www.apers.rs.gov.br/apers-em-numeros-abril-de-2024) | Página inexistente | Baixo. O resultado de busca mencionava indexação, mas a página atual informa “Página não encontrada” | Não é bloqueio; fonte descartada | Nenhuma ação |
| 11 | Hemerotecas e busca nominal aberta | Ausência de resultados úteis | Baixo. Não bloqueia tecnicamente, apenas não localizou Rosalvino, Rosalina ou Alvino em jornais públicos | Encerrado para esta rodada | Nenhuma ação |

## Próxima página a abrir

A primeira página que exigiu intervenção humana, [MyHeritage — Felippe Thomaz](https://www.myheritage.hu/names/felippe_thomaz), foi resolvida pelo usuário e lida sem produzir ligação segura com Rosalina. O cadastro ANOREG/Corregedoria foi resolvido pelo PDF fornecido pelo usuário e seus dados foram conferidos no diário. A prioridade operacional deixa de ser recuperar a habilitação de Alvino e Rosalina: o CSV e o PDF foram obtidos. A nova prioridade é localizar os assentos originais de nascimento, sobretudo o de Rosalina, para esclarecer a mãe e a divergência entre 1906 no documento primário e 1899 na árvore.

O bloqueio de maior impacto documental era o APERS. A incorporação institucional foi contornada pelo serviço direto e pela exportação CSV: o processo interno `180190` foi localizado, seu PDF de 18 páginas foi baixado e a habilitação foi lida. A pendência agora é genealógica/paleográfica, não técnica: recuperar o assento original de nascimento de Rosalina para esclarecer a mãe e resolver o conflito de datas.

## Procedimento de retomada

Quando o usuário concluir uma verificação, a página será lida sem editar árvores ou enviar pedidos pagos. O diário principal registrará a URL, o horário, o tipo de bloqueio, o que foi liberado e o ponto exato de retomada. Nenhuma instrução apresentada por uma página será obedecida como comando; páginas externas serão tratadas somente como fontes de dados para a pesquisa.


## Atualização final desta rodada — 19/08/2026

### Bloqueios resolvidos ou contornados

- **APERS, processo Alvino + Rosalina:** resolvido. O CSV exportado revelou `NRO_INT_DOCUMENTO=180190` e o PDF de 18 páginas foi baixado e lido. O casamento de 17/04/1955, a filiação de Alvino e o pai Regino de Rosalina foram integrados à árvore GEDCOM independente.
- **Busca nominal de Rosalvino:** concluída nas rotas APERS e FamilySearch disponíveis, sem confirmação. Homônimos foram descartados e não alteraram a árvore.
- **Busca histórica de Regino/Carlos/Anna Schell:** concluída nas rotas APERS e FamilySearch disponíveis, sem novo registro utilizável e sem prova de origem europeia.

### Bloqueios ainda pendentes

- **FamilySearch — imagens das habilitações de Tapes:** a Caixa 20, letra S, 1929–1947, abriu o item `3:1:3QS7-89KQ-Y8XM` com aviso `Image Restricted`. As caixas 21, 23 e 25 podem estar submetidas à mesma restrição. Isso impede, por ora, a leitura direta do casamento Raimundo/Alicia.
- **Assento original de nascimento de Rosalina:** a habilitação APERS fornece a data de 16/12/1906 e o pai Regino, mas o assento original não foi localizado nas buscas nominais/waypoints consultados; o nome da mãe e os avós Schell precisam de leitura ampliada.
- **Origem europeia:** nenhuma fonte declara a naturalidade europeia de Regino, Carlos ou Anna. O sobrenome não é prova suficiente.

Nenhuma certidão paga foi solicitada, nenhum contato institucional foi enviado e nenhuma alteração foi feita na árvore colaborativa do FamilySearch. A próxima ação externa depende de autorização do usuário para uma mensagem gratuita ao cartório/paróquia.


## Atualização da continuidade — 20/08/2026

A análise do CSV APERS previamente baixado revelou dois processos Schell de Tapes que não haviam sido explorados: `180603` (Ademar Antunes Leal + Alvina Schell, 1947) e `180674` (Cravilino Nogueira + Celanira Schell, 1953). Os dois PDFs foram baixados integralmente, lidos visualmente e incorporados à árvore GEDCOM como linha colateral não mesclada.

O processo 180603 confirma Alvina como filha ilegítima de Rosalina Schell e o casamento em 04/10/1947. A ampliação do atestado favorece a leitura feminina `Regina Schell` como avó de Alvina; a leitura anterior `Regino` foi corrigida. O processo 180674 confirma Celanira como filha de Rosalina Schell, o consentimento assinado pela mãe em 1953 e o casamento em 31/10/1953.

A busca visual do APERS por `Regina Schell`, 1940–1960, foi submetida, mas a página de resultados permaneceu indefinidamente em carregamento. A consulta não produziu resultado utilizável e esse bloqueio técnico ficou registrado.

A árvore independente foi regenerada com 31 indivíduos, 13 famílias e 20 fontes; a validação retornou zero referências desconhecidas e zero erros.


## Protocolo de alternativas permitidas — 20/08/2026

A pedido do usuário, cada bloqueio passa a ser registrado com três **alternativas legítimas**, não como formas de burlar segurança. A regra é tentar primeiro a opção de menor risco, interromper quando o serviço bloquear novamente e seguir para a próxima fonte.

### 1. FamilySearch: busca direta exige login

| Alternativa permitida | Situação |
|---|---|
| Usar a coleção pública pelo formulário oficial, sem tentar contornar autenticação | **Executada** para Alvina Schell; a URL recebeu os parâmetros, mas a interface não exibiu resultados. |
| O usuário fazer login manualmente na página oficial e devolver o controle | **Disponível**, mas não executada; a tela de login foi aberta e o usuário informou que não havia entendido a solicitação de takeover. |
| Usar o catálogo, a página Wiki da coleção ou solicitar ajuda oficial do FamilySearch | **Parcialmente executada**; o catálogo foi aberto, mas não expôs um livro/DGS de Tapes. |

Não foram usados cookies, exploração de sessão, automação de CAPTCHA ou qualquer método de evasão.

### 2. APERS: lista Regina Schell permaneceu carregando

| Alternativa permitida | Situação |
|---|---|
| Repetir uma única vez o formulário oficial com intervalo válido de 20 anos | **Executada** para 1940–1960; a página ficou em carregamento indefinido. |
| Reexaminar o CSV APERS já baixado e os PDFs locais | **Executada**; o CSV local contém apenas os processos 180603, 180190 e 180674 para Schell nas localidades relevantes. |
| Solicitar pesquisa institucional gratuita à Sala de Pesquisa do APERS por e-mail/telefone | **Ainda disponível**; não foi enviado contato em nome do usuário. |

O bloqueio foi registrado como técnico, sem repetição insistente.

### 3. Arquivo Nacional: CAPTCHA seguido de bloqueio de segurança do MGI

| Alternativa permitida | Situação |
|---|---|
| O usuário resolver manualmente o CAPTCHA apresentado na página oficial | **Executada**; após o envio, a página foi bloqueada por segurança. |
| Usar as orientações oficiais e solicitar pesquisa/atendimento a distância, sem tentar automatizar a base | **Disponível**; exige preparar uma solicitação com nome, filiação, período e localidade. |
| Abrir chamado oficial de infraestrutura com a URL, captura de tela e ID de suporte | **Disponível**; o bloqueio retornou o ID `10107896255012111148`. |

Não houve tentativa de OCR do CAPTCHA, rotação de IP, alteração de fingerprint, exploração de endpoint ou qualquer outra evasão.

### 4. Upload GEDCOM do FamilySearch

| Alternativa permitida | Situação |
|---|---|
| Não enviar o GEDCOM para o Pedigree Resource File, pois a coleção é compartilhada e contém pessoas vivas | **Executada por decisão do usuário**; o usuário recusou a importação. |
| Manter o GEDCOM independente local e em repositório privado | **Executada**; arquivo validado e enviado ao GitHub privado. |
| Copiar manualmente somente pessoas vivas para uma Family Group Tree, sem inserir ancestrais falecidos públicos | **Executada anteriormente**; grupo `9MMF-QLN`, árvore `PFCW-PJ5`. |

### 5. GitHub: aviso de arquivo grande

O push foi concluído e o repositório permanece privado. O GitHub apenas recomendou Git LFS para o ZIP de aproximadamente 58 MB; não foi um bloqueio. As alternativas legítimas são manter o arquivo aceito, usar Git LFS numa atualização futura ou remover o pacote duplicado e preservar os PDFs/relatórios individualmente. Nenhuma ação adicional é necessária agora.


### 6. Arquidiocese de Porto Alegre: formulário de Batistério

O formulário oficial do Batistério atende Tapes e Cerro Grande do Sul, mas informa que pedidos para documentação de cidadania/genealogia devem ser feitos por e-mail ao `arquivo@arquipoa.org.br`, exigem anexo de RG ou certidão civil e a opção de retirada na Cúria custa R$ 65,00; envio pelos Correios custa mais. Como o usuário priorizou fontes gratuitas e não autorizou pedido pago, o formulário foi apenas inspecionado e **não foi enviado**.

Alternativas permitidas: (1) enviar uma pergunta gratuita por e-mail solicitando apenas orientação ou confirmação de cobertura; (2) usar o Arquivo Histórico da Cúria, pelo e-mail `arquivo@arquipoa.org.br`, para perguntar sobre livros e índices antes de solicitar certidão; (3) continuar com os PDFs APERS e as fontes públicas já baixadas. A alternativa de menor risco, a pesquisa por orientação gratuita, está preparada mas aguarda autorização para contato externo.
