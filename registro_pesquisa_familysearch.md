# Registro inicial — FamilySearch

Data da tentativa: 19 de agosto de 2026.

A URL de autenticação fornecida pelo usuário (`https://ident.familysearch.org/`) retornou **503 Service Unavailable**, sem elementos interativos.

A página principal (`https://www.familysearch.org/`) redirecionou para `https://www.familysearch.org/global` e exibiu **Application Error**, também sem elementos interativos.

Conclusão provisória: a auditoria da árvore existente não pôde começar pelo navegador devido à indisponibilidade do serviço. Nenhuma alteração foi feita na conta ou na árvore. A próxima tentativa deverá usar uma rota alternativa de acesso ou começar pela coleta de documentos e fontes públicas enquanto o FamilySearch permanece indisponível.


Testes adicionais:

- A rota direta `https://www.familysearch.org/tree/pedigree/landscape` redirecionou para `/en/tree/pedigree/landscape` e carregou uma página visualmente vazia, sem elementos interativos detectáveis.
- A comunidade pública `https://community.familysearch.org/en` carregou parcialmente, com conteúdo abaixo da janela, indicando que ao menos esse subdomínio está acessível; isso não disponibilizou a árvore nem a autenticação.

A falha parece concentrada nas rotas da aplicação principal ou na renderização da sessão, não sendo possível concluir ainda se é uma indisponibilidade geral do FamilySearch.


Nova tentativa com a URL exata enviada pelo usuário:

- A tela de login carregou corretamente em 19 de agosto de 2026 às 16:25, com campos de usuário, senha e botão “SIGN IN”.
- O problema anterior era de carregamento da página/rota, não uma rejeição de credenciais.
- Ainda não foi enviado nenhum formulário e nenhuma alteração foi feita.


Resultado da nova tentativa:

A tela de login foi preenchida com as credenciais fornecidas e o formulário foi enviado. O FamilySearch redirecionou para `https://www.familysearch.org/en/tree/pedigree/landscape`, exibindo o cabeçalho da árvore e um indicador de carregamento. Isso indica que o acesso foi aceito ou, no mínimo, que a autenticação avançou para a aplicação da árvore. A árvore ainda não estava visualmente carregada no último estado observado; não foram feitas edições.


Primeira leitura da árvore conectada:

A sessão entrou na árvore de Jonathan Robert Silveira De Souza, identificado no FamilySearch como `GK15-TLV`, nascido em 2001 e vivo. O ramo visível mostra Valdeci Kenes de Souza (`P4KK-B9S`), Ana Paula (`P42Q-ZRT`), Rosalvino Schell de Souza (`P4KK-1QH`, 1940–2014), Carolina Augusta Kenes de Souza (`P42Q-FT6`) e Miriam Beatriz da Silveira Ribeiro (`P427-9HW`).

Esses nomes e relações são apenas o inventário inicial da árvore colaborativa. Nenhuma dessas informações foi considerada confirmada ainda, e nenhuma edição foi feita. O próximo passo é abrir os detalhes e fontes de cada pessoa, começando pelo casal de avós visível e avançando para os ancestrais.


Teste de perfil individual:

As rotas `.../tree/person/P4KK-1QH` e `.../tree/person/details/P4KK-1QH` carregaram uma página visualmente vazia, sem elementos interativos ou texto de perfil. O HTML indica que a sessão continua autenticada (`isLoggedIn = true`), mas os dados do perfil são carregados dinamicamente e não foram renderizados nessa rota. A árvore em modo paisagem continua sendo a fonte navegável disponível.


Após retornar à visualização paisagem, o cabeçalho e os controles carregaram, mas os cartões da árvore permaneceram ausentes após novas esperas. A sessão segue autenticada; a renderização dos dados genealógicos parece intermitente. A primeira visualização anterior, no entanto, permitiu registrar os identificadores de Jonathan, seus pais e avós.


Expansão do ramo de Rosalvino:

A árvore colaborativa associa Rosalvino Schell de Souza a Raimundo José de Souza (`GV4D-D91`, 1914–1983) e Alicia Schell de Souza (`GV54-K3Q`), com casamento indicado em Cerro Grande, Tapes, Rio Grande do Sul, Brasil. Também associa Alicia a Rosalvino por meio desse casal.

Na geração anterior, a árvore mostra Manoel José de Souza (`GV4D-FLS`, 1879–1941) e Maria Candida Tavares (`GV46-7JK`, 1895–1956) como pais de Raimundo; Alvino Paulino de Souza (`LZGD-TYJ`, 1891–1977) e Rosalina Schell (`LXVC-28B`, 1899–1993) como outro casal relacionado ao ramo Schell; Manoel Geraldo Kenes (`PMXJ-2SR`, 1904–deceased) e Dorvalina Ferreira Kenes (`G56B-32T`, 1905–1939); e Antonio Manoel Silveira (`PH4B-JD1`, 1897–deceased) e Tomazia Silveira (`PH4B-ZRX`, 1898–deceased). A árvore indica casamento de Alvino e Rosalina em Tapes em 17 de abril de 1955, e de Manoel Geraldo e Dorvalina em Capela Velha, Camaquã, em 28 de julho de 1948.

Esses dados são leads da árvore, não provas. Há possíveis inconsistências a investigar: a cronologia de alguns casamentos e a forma como os casais se conectam a Rosalvino precisam ser confirmadas em registros civis ou paroquiais. A localização preliminar do ramo é o sul do Brasil, especialmente Tapes e Camaquã, Rio Grande do Sul.


Auditoria inicial do perfil de Rosalvino:

O painel lateral do FamilySearch informa: nascimento em 6 de outubro de 1940, em Tapes, Rio Grande do Sul, Brasil; falecimento em 17 de outubro de 2014, em Guaíba, Rio Grande do Sul, Brasil; ocupação “agricultor”; e duas fontes associadas ao perfil. O painel discrimina, porém, “Birth • 0 Sources” e “Death • 0 Sources”, enquanto a ocupação aparece com uma fonte. Portanto, a existência de duas fontes no perfil não significa que nascimento e óbito estejam documentalmente comprovados.

A rota dedicada `.../tree/person/sources/P4KK-1QH` não renderizou conteúdo no navegador, impedindo identificar as fontes sem uma alternativa de acesso. Os fatos acima foram registrados como informações da árvore colaborativa, ainda não confirmadas por imagem de documento.


Continuação após remoção do modal:

O FamilySearch manteve a sessão autenticada e o cabeçalho da árvore reapareceu, mas os cartões genealógicos ainda não renderizaram nesta sequência de carregamento. Nenhum formulário foi enviado e nenhuma alteração foi realizada. A árvore já foi parcialmente auditada no estado anterior, quando os cartões e os ancestrais estavam visíveis.


Fontes públicas para o ramo do Rio Grande do Sul:

A página oficial do Arquivo Público do Estado do Rio Grande do Sul informa que seu acervo de registro civil inclui livros de nascimentos, casamentos e óbitos de 1929 a 1975, organizados por cartório municipal, além de processos de habilitação de casamento de 1890 a 1985. O APERS descreve esses processos como fontes primárias e informa que parte está sendo informatizada em sua plataforma online. Essa cobertura é potencialmente relevante para Rosalvino (nascido em 1940), Raimundo (nascido em 1914, portanto fora do intervalo geral dos livros civis indicados) e para casamentos do ramo.

O guia genealógico do FamilySearch para Tapes acionou uma página de interrupção anti-robô, portanto ainda não foi possível ler seu conteúdo. Isso não é evidência sobre a família e será tratado apenas como limitação de acesso.


Atualização da pesquisa no APERS:

A página anteriormente retornada pelo mecanismo de busca (`https://www.apers.rs.gov.br/apers-em-numeros-abril-de-2024`) atualmente exibe “Página não encontrada”. Portanto, o trecho do resultado de busca que mencionava imagens de habilitações de casamento de Tapes não foi confirmado na página original e não será tratado como evidência. O problema é uma página inexistente, não um antirobô; a busca seguirá pelo acervo oficial e por páginas alternativas do APERS.


Bloqueio antirobô — MyHeritage:

Em 19 de agosto de 2026, a página pública `https://www.myheritage.no/names/rosalina_schell` exibiu “Security check” e solicitou comprovação de que o visitante não é um programa automatizado. A página foi deixada aberta como ponto de retomada, sem tentativa de contornar o bloqueio. O resultado de busca havia sugerido uma possível associação entre Rosalina Schell e Alvino Paulino de Souza, com casamento em 1955, mas esse trecho permanece apenas como pista de baixa confiabilidade até que a página ou um registro independente seja verificado.

A pesquisa continuará por fontes públicas alternativas. Quando essa página for necessária para avançar, o usuário será chamado para concluir a verificação antirobô.


Tentativa de consulta à coleção pública do FamilySearch:

A coleção `Brazil, Rio Grande do Sul, Civil Registration, 1810–2022` estava acessível sem login e permitiu preencher Rosalvino, o sobrenome, Tapes e o intervalo de 1938–1942. O envio alterou a URL para uma consulta com parâmetros, mas a página não apresentou resultados antes de a visualização seguinte cair em `about:blank`. Nenhum registro foi lido ou salvo como evidência. A coleção permanece uma rota pública promissora, e a busca deverá ser retomada por uma URL direta ou por nova sessão, sem usar a rota que expõe campos de senha.


Nova tentativa de consulta autenticada:

A URL direta da consulta pública redirecionou para login. O envio por teclado, depois de preencher os campos, não expôs novamente os valores na URL, mas a visualização seguinte caiu em `about:blank` e não apresentou resultados. Nenhum registro foi acessado. A coleção pública e sua descrição continuam confirmadas; a rota de resultados permanece instável no navegador.


Busca pública adicional:

As consultas por “Rosalvino Schell”, “Rosalvino Schell de Souza” em Guaíba e “Alvino Paulino de Souza” em Tapes não produziram resultados utilizáveis em fontes abertas. Isso não refuta os dados da árvore; apenas indica que os nomes são pouco indexados na web aberta e que os registros civis, paroquiais ou imagens de cartório serão mais promissores.


Fontes institucionais confirmadas por extração textual:

O guia do FamilySearch para Tapes informa que a pesquisa municipal deve considerar registros civis, paroquiais, cemitérios e municípios vizinhos. Para Tapes, ele aponta especificamente a coleção “Brazil, Rio Grande do Sul, Miscellaneous Records, 1748–1998”, que contém imagens e licenças de casamento. O próprio guia alerta que a disponibilidade de coleções pode mudar conforme contratos com os custodians.

A página oficial do APERS confirma que o acervo de registro civil inclui livros de nascimento, casamento e óbito de 1929 a 1975, além de habilitações de casamento de 1890 a 1985, descritas como fontes primárias e únicas para o período. A lista de fundos inclui os cartórios de Camaquã, Guaíba e Tapes, três localidades diretamente relevantes para o ramo: Camaquã aparece como local de casamento na árvore, Tapes aparece nos casamentos e no nascimento de Rosalvino, e Guaíba aparece como local de óbito de Rosalvino.

A coleção FamilySearch “Rio Grande do Sul, Civil Registration, 1810–2022” informa que registros de nascimento, casamento e óbito podem conter filiação, naturalidade, residência, ocupação, nomes de avós, testemunhas e local de sepultamento. Isso a torna a primeira rota documental gratuita a tentar para confirmar os elos do ramo.


Coleções gratuitas prioritárias:

A coleção “Brazil, Rio Grande do Sul, Miscellaneous Records, 1748–1998” contém 2.919.774 imagens do Arquivo Público do Estado do Rio Grande do Sul, incluindo cópias de registros civis, declarações e investigações de casamento, além de registros notariais. A descrição informa que registros de nascimento podem trazer pais e avós, casamentos podem trazer datas de nascimento, naturalidade e pais dos noivos, e óbitos podem trazer cônjuge, origem, pais e local de sepultamento. O guia de Tapes aponta essa coleção especificamente para imagens e licenças de casamento.

A coleção “Brazil, Rio Grande do Sul, Catholic Church Records, 1738–1952” contém registros de batismo, casamento e sepultamento de paróquias católicas. A descrição informa que batismos podem trazer pais e padrinhos, casamentos podem trazer naturalidade, idade, residência, legitimidade e pais dos noivos, e óbitos podem trazer origem, cônjuge, pais e sepultamento. Ela é especialmente importante para recuar além do início ou da cobertura efetiva do registro civil.

Como a pesquisa nominal autenticada caiu em about:blank, o próximo caminho gratuito é navegar pelas imagens dessas coleções por município/paróquia e período, começando por Tapes e Camaquã, e procurar os sobrenomes raros no índice de imagens quando houver waypoints.


Diagnóstico da autenticação do FamilySearch:

Foi tentado um envio pela lógica JavaScript do próprio formulário, sem usar o clique automatizado que havia colocado campos na URL. O botão foi acionado, mas a visualização seguinte também caiu em `about:blank`, sem abrir a coleção ou os waypoints. A autenticação automatizada é instável nesta sessão; não há indicação de antirobô no FamilySearch neste ponto. A pesquisa documental continuará pelas descrições das coleções, fontes oficiais e outras rotas públicas, e o caminho autenticado será retomado quando houver necessidade específica.


Busca em hemerotecas:

As consultas direcionadas a hemerotecas digitais e ao acervo da Biblioteca Nacional por “Rosalvino Schell” e “Rosalina Schell” não retornaram ocorrências brasileiras utilizáveis. Os resultados encontrados eram de hemerotecas estrangeiras ou páginas gerais, sem conexão demonstrada com a família pesquisada.


Pista liberada após intervenção antirobô no MyHeritage:

A página pública `https://www.myheritage.no/names/rosalina_schell` passou a carregar resultados. Entre os resultados aparece “Rosalina de Souza (født Schell), 1899–1993”, com a descrição de que ela se casou com Alvino Paulino de Souza em 1955 e teve quatro filhas. O resultado é identificado como “FamilySearch familietre” e a imagem vinculada contém o identificador `LXVC-28B`, exatamente o identificador que apareceu na árvore do usuário para Rosalina Schell. A correspondência de nome, período, cônjuge e identificador reforça que a página está reproduzindo o mesmo perfil do FamilySearch, mas não constitui uma fonte independente.

A página também mostra outros perfis homônimos de Rosalina Schell, incluindo uma Rosalina Schell nascida em 1892, associada a Theodor Schell e ao sobrenome de nascimento Trott. Esses homônimos não devem ser misturados ao ramo do usuário. A pista relevante para a árvore atual é a mulher identificada como Rosalina de Souza, nascida Schell, 1899–1993, `LXVC-28B`.

A informação de casamento em 1955 e de quatro filhas será usada como hipótese de trabalho para localizar o registro civil ou religioso correspondente. O MyHeritage permanece uma fonte derivada de árvore e não será usado sozinho para confirmar datas ou relações.


Leitura ampliada do resultado MyHeritage:

A página desbloqueada repete o perfil `LXVC-28B` como “Rosalina de Souza (nascida Schell), 1899–1993”, classificado como árvore do FamilySearch. O resumo informa que Rosalina se casou com Alvino Paulino de Souza em 1955, aos 55 anos, e que o casal teve quatro filhas. O texto não fornece local nem dia/mês do casamento, nem imagem de uma certidão; por isso, a pista confirma a coerência entre árvores, mas não substitui o registro original.

A mesma página exibe homônimos distintos: uma Rosalina Schell nascida em 1892, com nome de nascimento Trott, casada com Theodor Schell e falecida em 1971, identificada em um resultado FamilySearch como `K2VJ-JTR`; e uma Rosalina Cramer, além de uma Rosalina Scafidi. A mulher de 1892 não será confundida com a Rosalina de 1899 do ramo de Alvino Paulino de Souza.


A tentativa de abrir o detalhe do cartão de Rosalina de Souza não acrescentou campos novos; a página permanece um resumo público de árvore, sem imagem de certidão, localidade ou datas completas do casamento. A pista útil continua sendo a identificação `LXVC-28B`, o casamento com Alvino Paulino de Souza em 1955 e a existência de quatro filhas, todos dados derivados da árvore do FamilySearch exibida pelo MyHeritage.


Busca por identificadores:

As consultas abertas por `LXVC-28B` (Rosalina Schell), `P4KK-1QH` (Rosalvino Schell de Souza) e `GV4D-D91` (Raimundo José de Souza) não retornaram páginas públicas adicionais. Os identificadores permanecem úteis para navegação interna no FamilySearch, mas não produziram evidência independente na web aberta.


Busca nominal adicional:

As consultas por “Alvino Paulino de Souza” e “Rosalina de Souza” retornaram somente a página já examinada do MyHeritage. Não surgiu nova fonte independente, localidade ou documento original.


Tentativa de perfil direto de Rosalina:

A rota `https://www.familysearch.org/en/tree/person/details/LXVC-28B` apresentou apenas o aviso de que o navegador não é totalmente suportado e, em seguida, caiu em `about:blank`. Não foi possível obter pais, fontes ou localidades adicionais. Esse é um problema de compatibilidade/renderização, não um antirobô.


Busca de Alvino:

As consultas por “Alvino Paulino de Souza” não localizaram uma página nominal específica nem fonte independente. O único resultado familiar continuou sendo o resumo de Rosalina Schell no MyHeritage, que reproduz o perfil `LXVC-28B` do FamilySearch.


Busca de catálogos específicos:

As consultas abertas por catálogos de Tapes e Camaquã no FamilySearch não retornaram uma rota nova de imagens ou catálogo municipal. Permanecem como caminhos principais a coleção de registros diversos, a coleção de registros civis e a coleção de registros católicos já documentadas.


Contexto histórico oficial de Tapes:

A Biblioteca do IBGE identifica Tapes pelo código municipal 4321105 e informa que a região era conhecida como Dores de Camaquã. O histórico registra que o território pertenceu a Triunfo em 1831, teve a Paróquia de Nossa Senhora das Dores de Camaquã criada em 1833, foi anexado e desmembrado de Porto Alegre em diferentes períodos, e teve a sede municipal transferida para Tapes em 1929. Em 1950, o município incluía os distritos de Tapes, Cerro Grande e Vasconcelos.

Essa história é relevante para a pesquisa: registros anteriores a 1929 podem estar sob Dores de Camaquã, e registros ainda mais antigos podem estar vinculados a Porto Alegre ou Triunfo. O local “Cerro Grande, Tapes” indicado para o casamento de Raimundo José de Souza e Alicia Schell deve ser pesquisado também como distrito/localidade histórica, não apenas como município moderno.


Paróquia atual de Tapes:

A página oficial da Arquidiocese de Porto Alegre, filtrada por Tapes, identifica a **Paróquia Nossa Senhora do Carmo**, na Rua Felicíssimo Alfonsim, 769, Centro, Tapes–RS, CEP 96760-000. O contato publicado é `+55 51 3672-1493` e `nscarmo@arquipoa.org.br`. A página informa o pároco Padre João Miguel Schäfer.

Esse contato é uma rota institucional gratuita para perguntar pela custódia ou disponibilidade de livros paroquiais, mas ainda não será contatado sem uma necessidade documental definida e autorização do usuário para qualquer comunicação externa. A identificação da paróquia é coerente com a história de Tapes e com a invocação de Nossa Senhora do Carmo encontrada na documentação institucional.


Paróquia atual de Camaquã:

O filtro oficial da Arquidiocese de Porto Alegre identifica a **Paróquia São João Batista** em Camaquã, na Rua João de Oliveira, 30, Centro, CEP 96180-000. O contato publicado é `+55 51 3671-4616` e `saojoao.camaqua@arquipoa.org.br`. A identificação é relevante porque a árvore associa parte do ramo a Capela Velha, Camaquã, e os registros religiosos podem estar sob a paróquia local ou sob sua jurisdição histórica.


Paróquia atual de Cerro Grande do Sul:

O filtro oficial da Arquidiocese identifica a **Paróquia São José da Fortaleza**, na Rua Arthur Emílio Jenich, 252, Centro, Cerro Grande do Sul–RS, CEP 96770-000. O contato publicado é `+55 51 3675-1045`, com WhatsApp associado, e `saojosedafortaleza@arquipoa.org.br`. A existência dessa paróquia atual fornece uma terceira rota institucional para registros do local descrito na árvore como “Cerro Grande, Tapes”. A jurisdição histórica ainda precisa ser confirmada antes de qualquer pedido documental.


Paróquias atuais de Guaíba:

O filtro oficial da Arquidiocese lista quatro paróquias em Guaíba: Nossa Senhora da Paz (`+55 51 3401-1411`, `nspaz.guaiba@arquipoa.org.br`), Nossa Senhora de Fátima (`+55 51 3491-7447`, `fatima.guaiba@arquipoa.org.br`), Nossa Senhora do Livramento (`+55 51 3480-1465`, `livramento@arquipoa.org.br`) e Santa Rita de Cássia (`+55 51 3402-2524`, `santarita.guaiba@arquipoa.org.br`). Esses contatos são apenas referências institucionais para eventual busca de sepultamento ou registro religioso de Rosalvino; o registro de óbito civil deve ser priorizado no fundo de Guaíba do APERS ou no cartório competente.


Histórico oficial de Cerro Grande do Sul:

A página oficial do município informa que Cerro Grande do Sul foi criado como **3º distrito de Tapes em 13 de maio de 1924** e que sua sede foi elevada à categoria de vila em 1938. O texto também informa a presença histórica de famílias de origem alemã, portuguesa, italiana e de outras origens, mas essa distribuição populacional é contexto municipal e não prova a origem de nenhuma família específica.

Esse dado confirma que um registro de casamento ou residência descrito como “Cerro Grande, Tapes” pode estar no fundo de Tapes, mesmo quando o evento ocorreu na localidade que hoje é Cerro Grande do Sul. A paróquia atual identificada para a localidade é São José da Fortaleza, mas a jurisdição paroquial histórica ainda precisa ser comprovada.


Busca dos casamentos prioritários:

Consultas exatas por Rosalina Schell e Alvino em 17/04/1955, por Flauliano Brasil Kenes e Eva Silveira em 28/07/1948, e por Raimundo José de Souza e Alicia Schell não retornaram referências públicas independentes. Os três eventos continuam como alvos documentais prioritários nas imagens do FamilySearch/APERS ou nos cartórios e paróquias correspondentes.


Cartório civil prioritário:

Um diretório público de cartórios identifica o **Ofício dos Registros Públicos de Tapes**, no Centro, como cartório civil responsável por nascimentos, casamentos e óbitos, com abrangência declarada sobre os municípios de Tapes, Sentinela do Sul e Cerro Grande do Sul. O diretório informa a responsável legal Mara Liane Peter, horário de atendimento de segunda a sexta-feira, das 8h30 às 11h30 e das 13h30 às 17h, e os telefones `(51) 3672-3773` e `(51) 3672-2438`.

Essa informação é particularmente importante porque conecta a localidade moderna de Cerro Grande do Sul ao cartório de Tapes, exatamente como a hipótese histórica sugeria. O diretório não é a fonte primária do registro familiar e seus dados cadastrais deverão ser confirmados antes de qualquer contato. Nenhuma certidão foi solicitada ou paga.


Bloqueio antirobô — cadastro cadastral do cartório:

A página `https://www.anoreg.org.br/files/RS-5096-3295.pdf`, que contém cadastro da Corregedoria Nacional de Justiça/ANOREG, foi bloqueada por CAPTCHA antes de disponibilizar artefatos visuais. O conteúdo textual extraído antes do bloqueio informa: CNS `09.953-1`; denominação “Registros Públicos de Tapes”; instalação em `08/01/1876`; atribuição de Registro Civil das Pessoas Naturais; município Tapes–RS; endereço Rua Felicíssimo de Alfonsin nº 806, Sala 01; telefone `(51) 3672-3773`; e-mail `cartorio@marapeter.com.br`; titular Mara Liane Peter.

O bloqueio foi registrado conforme combinado. Esses dados cadastrais são coerentes com o diretório público consultado, mas a página bloqueada não será tratada como prova de nenhum evento familiar. O usuário poderá concluir o CAPTCHA em uma retomada futura se for necessário verificar o documento visualmente.


Confirmação independente do cartório de Tapes:

A página `cartoriosbrasileiros.org` confirma o Ofício de Registros Públicos de Tapes com CNS `09.953-1`, CNPJ `90.828.799/0001-00`, titular Mara Liane Peter e endereço Rua Felicíssimo de Alfonsin, 806, salas 01 e 02, Centro, Tapes–RS, CEP 96760-000. O cadastro também lista atribuições de nascimentos, casamentos, óbitos, interdições e tutelas, além de informar abrangência sobre Tapes, Sentinela do Sul e Cerro Grande do Sul.

A página oferece emissão online de certidões, mas nenhuma solicitação ou pagamento foi iniciado. A fonte é cadastral/administrativa e serve para localizar a serventia; a confirmação genealógica ainda depende do conteúdo dos registros.


Bloqueio adicional de extração — MyHeritage:

A tentativa de obter o texto completo da página do MyHeritage por uma rota textual retornou um incidente do Incapsula. A leitura pelo navegador, após o usuário concluir o antirobô, já capturou os dados relevantes disponíveis publicamente; não será feita nova tentativa de contornar essa proteção.


Resultado da retomada segura do FamilySearch:

A rota original de login foi aberta, preenchida e enviada pela lógica JavaScript da página. O redirecionamento levou à página global do FamilySearch, mas o cabeçalho ainda mostra “Sign In”, indicando que a sessão não ficou persistida nesta tentativa. Não houve CAPTCHA nem mensagem de credenciais incorretas, e nenhum dado da árvore foi alterado. A pesquisa seguirá com o material público e com as rotas institucionais já identificadas.


Bloqueio antirobô — perfil relacionado de Felippe Thomaz:

A página `https://www.myheritage.hu/names/felippe_thomaz`, encontrada por busca dos irmãos raros de Rosalina, exibiu novamente “Security check”. O resultado de busca havia indicado que Felippe Thomaz aparece com Wilbald Thomaz, Frieda Hoff e outros irmãos, o que pode ajudar a identificar os pais de Rosalina; porém, a associação continua derivada e não foi verificada na página. O bloqueio foi registrado e a pesquisa seguirá por outras rotas.


Pistas adicionais da possível família de Rosalina:

As buscas públicas pelos nomes raros retornaram páginas derivadas do MyHeritage para Adolpho Thomaz e Carolina Thomaz. Os trechos indexados repetem que Adolpho tinha como irmãos Wilbald Thomaz e Frieda Hoff, e que Carolina Thomaz se casou com Emilio Schelle e teve quatro filhos. A página de Felippe Thomaz também havia mostrado a mesma combinação de irmãos. Essas coincidências sugerem uma possível família Thomaz/Schell relacionada à Rosalina, mas ainda não estabelecem que Felippe, Adolpho, Carolina, Wilbald e Frieda sejam irmãos da Rosalina `LXVC-28B` nem identificam os pais.

O fato de os resultados MyHeritage classificarem a maioria como árvores familiares e de não fornecerem datas, localidades ou imagens originais exige confirmação em registros civis ou paroquiais. A busca por esses nomes raros será usada para priorizar nomes de testemunhas, pais e irmãos quando as imagens de casamento ou batismo forem acessadas.


Busca em páginas públicas de ancestrais:

As consultas por Felippe Thomaz, Adolpho Thomaz e Carolina Thomaz em páginas públicas do FamilySearch retornaram principalmente pessoas de outras famílias e estados, sem uma correspondência segura com o ramo de Tapes/Cerro Grande do Sul. Os resultados não serão incorporados à árvore.


Consulta APERS por Rosalina — 1955:

A busca livre do APERS retornou **43 registros em uma página**, organizados por tipos documentais. A tela visual mostrou agrupamentos que incluem “Processo / Habilitação para casamento” e “Cartório do Registro Civil de Tapes”, indicando que o acervo possui fundos potencialmente pertinentes. A tentativa de extrair automaticamente as linhas da tabela pelo console retornou texto vazio, provavelmente porque a grade é carregada em componente dinâmico/virtualizado. Nenhum registro foi aberto ou tratado como correspondência individual.


Leitura visual dos resultados do APERS:

A página mostrou resultados de nomes contendo “Rosalina” no ano de 1955, mas as linhas visíveis eram homônimos sem relação demonstrada com o ramo: Rosália Correia Machado, Rosalia Antônio Bento Ferreira e Rosalina Correia Silveira, todos em Porto Alegre, além de Rosalina Brasileiro de Mello em processo judicial de Rio Pardo e Dorallina de Almeida Boeira em arrolamento de Porto Alegre. Nenhuma linha visível correspondia a Rosalina Schell, Alvino Paulino de Souza ou Tapes. A busca ampla por prenome não produziu correspondência familiar útil.


**Achado documental decisivo no APERS — casamento Schell/Souza:**

A consulta gratuita pelo sobrenome `Schell`, com intervalo de 1955 a 1955, retornou **4 registros**, incluindo um agrupamento de **Processo / Habilitação para casamento** no **Cartório do Registro Civil de Tapes**. A linha visível identifica:

- noivo: **Alvino Paulino de Souza**;
- noiva: **Rosalina Schell**;
- data exibida pelo índice: **01/01/1955**;
- município: **Tapes**.

Essa linha é uma correspondência nominal e institucional muito forte com o casal da árvore `LZGD-TYJ` + `LXVC-28B`. A data `01/01/1955` deve ser interpretada com cautela: o índice do APERS pode usar uma data-padrão para o ano quando o dia/mês não estão disponíveis, enquanto a árvore FamilySearch indicava 17/04/1955. Portanto, o achado confirma a existência do processo/habilitação do casal no fundo de Tapes, mas ainda não resolve a data exata do casamento nem prova todos os demais dados da árvore.

O índice visual não mostrou o número do processo nem abriu a imagem nesta etapa. O próximo passo prioritário é abrir ou selecionar essa linha, se a interface permitir, para localizar a imagem digital ou os metadados do processo. Nenhum pagamento foi feito.


Instabilidade do APERS após o achado:

Depois da seleção visual da linha e de uma tentativa de reiniciar a consulta, a plataforma do APERS caiu em `about:blank` e não carregou nova tabela. A seleção não abriu imagem nem metadados adicionais. O achado do índice — Alvino Paulino de Souza + Rosalina Schell, Cartório do Registro Civil de Tapes, processo/habilitação de casamento — permanece salvo e é o principal resultado documental desta etapa.


Consulta APERS por Kenes — 1948:

A busca livre por `Kenes`, entre 1948 e 1948, retornou **1 registro**, agrupado como processo/habilitação de casamento do Cartório do Registro Civil de Ijuí. A linha visível identifica Emilio Germano Kromberg e Jenny Mafalda Denes, em Ijuí, com data indexada 01/01/1948. Não há correspondência com Flauliano Brasil Kenes e Eva Silveira, nem com Camaquã. O resultado não será incorporado à árvore; o índice mostra que a busca nominal é sensível ao fundo documental e que o casamento de Flauliano provavelmente exige outra grafia, outro ano de indexação ou acesso ao fundo/paróquia de Camaquã.


Consulta APERS por Flauliano — 1948:

A busca livre pelo prenome raro `Flauliano`, no intervalo de 1948 a 1948, retornou **0 registros**. Isso não refuta o casamento indicado na árvore: o índice pode ter grafia diferente, o registro pode estar em fundo não indexado, o evento pode ter sido indexado apenas pelo nome da cônjuge ou a data pode não estar associada ao ano esperado. Por enquanto, o casamento de Flauliano Brasil Kenes e Eva Silveira permanece sem confirmação documental.


**Achado parcial no APERS — busca por Eva Silveira:**

A consulta gratuita por `Eva Silveira`, no ano de 1948, retornou **2 registros**, ambos agrupados como processo/habilitação de casamento do **Cartório do Registro Civil de Tapes** e indexados em `01/01/1948`:

1. **Christiano Altmann** + **Eva Pereira da Silveira**, Tapes;
2. **Paulo Rodrigues da Silveira** + **Eva Pereira de Campos**, Tapes.

Nenhum noivo aparece como Flauliano Brasil Kenes. Entretanto, o primeiro registro contém uma Eva Pereira da Silveira e o segundo uma Eva Pereira de Campos, portanto são candidatos a serem comparados com a Eva Silveira da árvore, não evidência de que qualquer um seja o casal correto. A árvore informa Eva nascida em 1927 e casada com Flauliano em 28/07/1948 em Capela Velha/Camaquã; esses dados ainda não foram reconciliados com os dois índices de Tapes.


**Desambiguação de Eva Silveira — confirmação independente:**

A página pública `ancestors.familysearch.org` para `9XF9-YDG` identifica **Eva Pereira da Silveira**, nascida em 15/02/1931 e falecida por volta de 2002, filha de Viriato José da Silveira e Florisia Pereira da Silveira. A mesma página informa casamento por volta de 1950, em Tapes, com **Cristiano Lopes Altmann**, e lista uma fonte de registro civil do Rio Grande do Sul.

Esse perfil corresponde ao primeiro resultado do APERS (`Christiano Altmann` + `Eva Pereira da Silveira`, Tapes, 1948 no índice), demonstrando que essa Eva é uma pessoa distinta da Eva Silveira da árvore pesquisada, que aparece como nascida em 1927 e cônjuge de Flauliano Brasil Kenes. O resultado elimina um falso positivo e reforça a necessidade de encontrar a Eva correta pelo casamento, pais ou data de nascimento, não apenas pelo sobrenome.


Consulta APERS por Schell — 1940:

A busca livre por `Schell`, no intervalo de 1940 a 1940, retornou **0 registros**. Não foi localizado no índice um nascimento de Rosalvino ou outro ato civil com esse sobrenome. Isso não elimina o registro: a consulta pode não cobrir nascimentos do fundo esperado, o nome pode ter sido indexado por outra grafia, ou o documento pode estar disponível apenas em imagens não indexadas do FamilySearch. O casamento de Alvino e Rosalina continua sendo a melhor porta de entrada para recuperar os pais e a naturalidade de Rosalina.


Busca nominal de Rosalvino:

Consultas abertas por “Rosalvino Schell de Souza”, “Rosalvino Schell” em Tapes e “Rosalvino de Souza” com Schell em Guaíba não retornaram resultados públicos independentes. Os dados de nascimento e óbito de Rosalvino continuam apoiados apenas no perfil da árvore FamilySearch, aguardando registro civil, obituário ou fonte paroquial.


Consulta APERS por Rosalina — 1899:

A busca livre por `Rosalina`, no intervalo de 1899 a 1899, retornou **30 registros em uma página**, distribuídos por diversos tipos documentais e municípios. A área visível começou por processos/habilitações do Cartório do Registro Civil de Antônio Prado; a busca textual direta não encontrou imediatamente o agrupamento “Cartório do Registro Civil de Tapes”. Será necessário usar filtros visuais ou leitura programática da tabela para separar os registros de Tapes e Camaquã, sem atribuir homônimos a Rosalina Schell.


Limite técnico da consulta por Rosalina — 1899:

A tabela de resultados do APERS é renderizada dinamicamente em componentes que não expuseram linhas em `tr` nem os termos `Rosalina`, `Schell`, `Tapes` ou `Camaquã` no texto capturado pelo console. A consulta visual confirma 30 resultados, mas a separação por município não pôde ser feita automaticamente nesta tentativa. Nenhum homônimo será incorporado à árvore sem leitura da linha e da fonte.


**Retomada autenticada do FamilySearch — perfil de Rosalvino:**

Com a sessão iniciada pelo usuário e a extensão do navegador instalada, o perfil `P4KK-1QH` passou a renderizar corretamente em 19/08/2026. O FamilySearch confirma no detalhe: Rosalvino Schell de Souza, masculino, nascimento em 06/10/1940 em Tapes, Rio Grande do Sul, Brasil, e falecimento em 17/10/2014 em Guaíba, Rio Grande do Sul, Brasil. O perfil mostra `Birth • 0 Sources` e `Death • 0 Sources`; o nome tem 2 fontes e a ocupação “agricultor” tem 1 fonte. Portanto, as datas continuam sem fonte diretamente associada no perfil.

A página confirma o cônjuge Carolina Augusta Kenes de Souza (`P42Q-FT6`), sem evento de casamento registrado, e o filho Valdeci Kenes de Souza (`P4KK-B9S`). Na seção “Parents and Siblings”, os pais são Raimundo José de Souza (`GV4D-D91`) e Alicia Schell de Souza (`GV54-K3Q`), com casamento indicado em Cerro Grande, Tapes, Rio Grande do Sul, Brasil. A mesma seção lista quatro filhos do casal: Rosalvino, Jovenil de Souza (`PQXM-T6K`, 1948–1963), Manoel de Souza (`P4LK-52C`, 1949–1949) e Waldemar de Souza (`P99P-N9F`, 1955–1974).

O perfil mostra `Sources (2)`, mas as fontes ainda não foram abertas nesta etapa. O histórico recente registra alterações de relação em 05/08/2026 por `LilicaJustino`, incluindo uma relação excluída e duas adicionadas; isso reforça a necessidade de conferir cada elo em documento, sem assumir que a estrutura atual é estável ou comprovada.


**Fonte civil autenticada aberta — Rosalvino, registro de 1971:**

A primeira fonte associada ao perfil `P4KK-1QH` abriu dentro do FamilySearch. Ela pertence à coleção “Brasil, Rio Grande do Sul, Registro Civil, 1810–2022” e apresenta:

- data do registro: **29/03/1971**;
- entrada para **José Maria Kenes de Souza** e **Rosalvino Schel de Souza**;
- link público do registro: `https://familysearch.org/ark:/61903/1:1:6YPM-F1JQ`;
- título indexado: “Rosalvino Schel de Souza”, com uma variação ortográfica de Schell;
- a fonte foi criada/anexada por `Jonathan2545` em 28/12/2025;
- tags já aplicadas: Sex, Name e Occupation; o FamilySearch informa que a fonte ainda não foi anexada a todas as pessoas encontradas no registro.

Esse achado é importante porque introduz **José Maria Kenes de Souza** como pessoa associada ao mesmo registro civil de Rosalvino em 29/03/1971. Ainda não se deve concluir se José Maria é pai, testemunha, cônjuge, declarante ou outro participante: a imagem/ficha do registro precisa ser aberta para ler a relação e os campos completos. A variação `Schel`/`Schell` deve ser preservada como grafia documental, sem correção automática.


A página autenticada do registro `6YPM-F1JQ` confirmou a natureza do evento: trata-se do **óbito de José Maria Kenes de Souza**, filho de Rosalvino Schel de Souza, com 16 dias de idade, nascido em 13/03/1971 e falecido em 29/03/1971 em Guaíba, Rio Grande do Sul. O registro informa sexo masculino, raça branca, local de sepultamento Guaíba e certificado nº 599. Rosalvino aparece como pai; Carolina Augusta Kenes de Souza aparece como esposa de Rosalvino e, portanto, mãe indicada no conjunto familiar do registro. A página também exibe “VIEW ORIGINAL DOCUMENT”, mas a navegação direta para o registro não renderizou a imagem/documento nesta tentativa.

Esse achado fornece uma confirmação documental indexada de que Rosalvino e Carolina tiveram ao menos um filho, José Maria, falecido em 1971. O perfil de Rosalvino não listava José Maria entre os filhos na seção inicialmente lida, o que indica uma relação incompleta ou não anexada na árvore. Não será feita nenhuma alteração online; a inconsistência será apenas registrada para revisão posterior.


Após retornar à aba de fontes, a fonte de 1971 permaneceu expandida e confirmou novamente a relação: José Maria Kenes de Souza aparece como filho de Rosalvino Schel de Souza, com Carolina Augusta Kenes de Souza no conjunto de cônjuge/mãe. A segunda fonte associada ao perfil é intitulada “Rosalvino Schele de Souza”, com data de 1979, criada em 31/12/2025 por `Jonathan2545`, mas ainda não foi expandida nesta sequência. A variação documental `Schel`/`Schele`/`Schell` deverá ser mantida no quadro de pesquisa.


**Segunda fonte civil associada a Rosalvino — 1979:**

A fonte de 1979, intitulada “Rosalvino Schele de Souza”, aponta para o registro `https://familysearch.org/ark:/61903/1:1:XSF9-NC8N` e cita a coleção “Brasil, Rio Grande do Sul, Registro Civil, 1810–2022”. O resumo do FamilySearch descreve uma entrada para **Magda Renes de Souza** e **Rosalvino Schele de Souza**, mas exibe a data textual “10 de janeiro de 1810”, incompatível com a pessoa Rosalvino de 1940 e provavelmente resultante de erro de indexação ou de campo mal interpretado. A fonte foi criada/anexada por `Jonathan2545` em 31/12/2025 e informa anexação incompleta.

A navegação direta para `XSF9-NC8N` não renderizou a ficha pública nesta tentativa. Por isso, a relação entre Magda Renes de Souza e Rosalvino, o evento de 1979 e a data correta permanecem pendentes. Essa fonte não será usada para confirmar parentesco ou cronologia até que o registro seja lido por outra rota.


**Retomada autenticada — perfil de Raimundo José de Souza:**

O perfil `GV4D-D91` renderizou corretamente. Ele confirma Raimundo José de Souza, masculino, nascido em 1914 e falecido em 09/09/1983 em Porto Alegre, Rio Grande do Sul. O perfil mostra `Birth • 4 Sources` e `Death • 1 Source`, além de um evento “Death Registration” em 09/09/1983 no Rio Grande do Sul. Isso representa uma base documental mais forte que a do filho Rosalvino, embora as fontes individuais ainda precisem ser abertas e conferidas.

O perfil confirma como cônjuge **Alicia Schell de Souza** (`GV54-K3Q`) e registra o casamento em **Cerro Grande, Tapes, Rio Grande do Sul, Brasil**. Os pais exibidos são **Manoel José de Souza** (`GV4D-FLS`) e **Maria Candida Tavares** (`GV46-7JK`), sem evento de casamento listado. A seção parental indica oito filhos, mas não os nomeia na leitura atual. O histórico de alterações de 05/08/2026 registra três relações excluídas por `LilicaJustino`; a estrutura atual deve ser tratada como colaborativa e sujeita a revisão.


**Fontes do perfil de Raimundo — inventário autenticado:**

A aba `Sources (7)` de `GV4D-D91` lista sete fontes na coleção “Brasil, Rio Grande do Sul, Registro Civil, 1810–2022” ou em um registro de óbito relacionado:

1. `974` — “Raymendo José, de Souza Santos”, criada em 23/02/2025 por `LilicaJustino`;
2. `1800` — “Raymundo de Soura”, criada em 15/08/2025 por `LilicaJustino`;
3. `1941` — “Óbito de Manoel José de Souza em Barão do Triunfo. 21/2/1941”, criada em 07/08/2023 por `LilicaJustino`;
4. `1941` — “Raimundo José de Souza”, criada em 30/11/2024 por `LilicaJustino`;
5. `1941` — “Raimundo Jofe de Souza”, criada em 07/02/2025 por `LilicaJustino`;
6. `1949` — “Raimundo de Souza Finão Maniculta”, criada em 30/12/2025 por `Jonathan2545`;
7. `1983` — “Raimundo José de Souza”, criada em 28/01/2023 por `LilicaJustino`.

As fontes de 974, 1941 (uma delas), 1949 e possivelmente outras exibem anexação incompleta. O inventário sugere registros de nascimento/identidade, um possível óbito do pai Manoel em Barão do Triunfo, um registro de 1949 e o óbito de Raimundo em 1983. Nenhuma dessas fontes foi ainda aberta para leitura integral; portanto, não se deve usar os títulos com grafias erradas (“Raymendo”, “Soura”, “Jofe”, “Finão Maniculta”) como prova sem examinar os campos do documento.


**Primeira fonte aberta de Raimundo — registro de 0974:**

A fonte de 974 foi expandida e aponta para `https://familysearch.org/ark:/61903/1:1:XSX8-CTNC`. A citação descreve uma entrada para **Saldemar de Sousa** e **Raymendo José, de Souza Santos**, com o valor `0974` exibido como data/título indexado. A fonte contém tags Birth, Sex e Name e foi anexada ao perfil de Raimundo por `LilicaJustino`.

A página direta do registro não renderizou a ficha nesta tentativa. O título, a grafia e o valor “0974” são insuficientes para determinar se se trata de nascimento, registro tardio ou outro evento. Ainda assim, a associação de Raimundo com Saldemar de Sousa é uma pista documental que deverá ser lida na imagem original antes de ser interpretada como filiação.


**Leitura expandida da fonte 0974 de Raimundo:**

A fonte foi identificada como um registro de óbito de **Saldemar de Sousa**, no qual **Raymendo José, de Souza Santos** aparece como filho. Os dados indexados são: Raimundo com naturalidade indicada na **Paraíba, Brasil**; Saldemar de Sousa, sexo masculino, idade indexada como “19 anos - meses e — dias”, nascimento em 1955, naturalidade Paraíba, evento de óbito em `0974` em São Jerônimo, Rio Grande do Sul, certificado nº 4545, raça branca. O registro também lista **Alicia Sebello de Souza** como esposa de Raimundo, com naturalidade indicada na Paraíba.

Esse registro não pode ser ligado automaticamente ao perfil `GV4D-D91` sem resolver as inconsistências: o nome indexado é “Raymendo José, de Souza Santos”, a data aparece como `0974`, e Saldemar teria nascido em 1955, quando Raimundo é identificado na árvore como nascido em 1914. Entretanto, a naturalidade Paraíba e a presença de Alicia como esposa são pistas relevantes para a origem regional e para a linha Schell/Souza. A forma “Alicia Sebello” também deve ser comparada com “Alicia Schell” na árvore, sem presumir que sejam a mesma pessoa até a imagem original ser lida.


**Fonte não indexada do óbito de Manoel José de Souza:**

A fonte “Óbito de Manoel José de Souza em Barão do Triunfo. 21/2/1941” foi expandida. O FamilySearch informa que o registro **não foi indexado** e oferece o documento original no link `https://familysearch.org/ark:/61903/3:1:3QS7-99GW-1966`. A fonte foi anexada ao perfil de Raimundo por `LilicaJustino` em 07/08/2023.

O link de imagem foi acionado e abriu uma rota do FamilySearch para o documento original, mas a visualização permaneceu na página de fontes nesta captura. A próxima ação prioritária é abrir diretamente o link da imagem e ler a certidão/folha, pois ela pode confirmar se Manoel é o pai de Raimundo e fornecer idade, naturalidade, cônjuge e nomes dos pais de Manoel.


**Imagem original do óbito de Manoel — índice do FamilySearch:**

A rota da imagem carregou o visualizador do FamilySearch na coleção `Brazil, Rio Grande do Sul, Civil Registration, 1810–2022`, filme **004208553**, imagem indicada `2902`/`2903`. A aba “Image Index” expôs os seguintes dados indexados do documento:

- **Manoel José de Souza**, masculino, idade transcrita de forma inconsistente como “sessenta e dois (82) anos de idade”, nascimento indicado como 1879, naturalidade Rio Grande do Sul, sepultamento em Barão do Triunfo, ocupação agricultor, raça morena, evento óbito em 21/02/1941, local Barão do Triunfo, Rio Grande do Sul;
- **Raimundo José de Souza**, masculino, associado ao registro com local/observação “1.ª Zona de Barão do Triunfo”;
- Manoel Francisco da Silva;
- Maria Candida Tonares, variação indexada de Maria Candida Tavares;
- Raimundo Jofe de Souza, variação ortográfica de Raimundo José de Souza;
- Jacinto José de Souza;
- Manoela Francina de Silva;
- Elenterio José de Souza;
- Joaquina José de Souza;
- José de Souza, feminina, 17 anos, nascimento 1924;
- João José de Souza, masculino, 10 anos, nascimento 1931;
- Daison do Souza, 10 anos, nascimento 1931;
- Manoel Tovares dos Santos.

O índice confirma que Manoel José de Souza morreu em Barão do Triunfo em 21/02/1941 e que Raimundo José de Souza, Maria Candida Tavares e outros familiares aparecem no mesmo registro. O documento original ainda não foi lido visualmente em alta resolução; portanto, a relação exata — especialmente se Raimundo aparece como filho e Maria Candida como esposa — deve ser confirmada na imagem antes de elevar a filiação a nível documental definitivo. As grafias “Tonares/Tavares”, “Jofe/José” e a idade “62/82” são problemas de indexação a preservar e conferir no manuscrito.


O retorno às fontes confirmou que o item de 1941 sobre Manoel é exclusivamente uma imagem não indexada; a leitura do índice de pessoas no visualizador foi a única informação estruturada disponível. Na mesma aba permanecem as fontes indexadas de Raimundo de 1941 e 1949, além do óbito de 1983, que serão priorizadas em seguida para localizar registros com data e número de imagem mais legíveis.


**Registro indexado complementar do óbito de Manoel:**

A fonte indexada de 1941 aponta para `https://familysearch.org/ark:/61903/1:1:6RM8-HCHX` e identifica a entrada de **Manoel José de Souza** e **Jacinto José de Souza**, com evento em **21/02/1941**. A ficha pública direta não renderizou os campos nesta tentativa, mas o título e a citação confirmam que se trata do mesmo dia e coleção do documento visualizado no filme 004208553. O vínculo com Raimundo permanece indireto nesta ficha; a imagem original continua sendo a fonte mais importante para ler a relação familiar.


**Leitura indexada completa do óbito de Manoel — fonte 6RM8-HCHX:**

A fonte de 21/02/1941 identifica **Raimundo José de Souza** como mencionado no registro de óbito de **Manoel José de Souza**. Os dados estruturados informam Manoel, masculino, 62 anos, nascimento em 1879, sepultamento na Vila de Barão do Triunfo, ocupação agricultor, raça morena, óbito em 21/02/1941 no local indexado como São Jerônimo/São Jerônimo, Rio Grande do Sul, com local original “Barão do Triunfo”, certificado nº **10118**. Também aparecem **Jacinto José de Souza** e **Manoela Francisca da Silva** como outras pessoas no registro.

A citação da fonte é `https://familysearch.org/ark:/61903/1:1:6RM8-HCHX`. O FamilySearch apresenta Raimundo como “mentioned in the record of Manoel José de Souza”, mas a ficha indexada não explicita no texto se Raimundo é filho, declarante ou outro parente. Ainda assim, combinada com a árvore que coloca Manoel José de Souza como pai de Raimundo e Maria Candida Tavares como mãe, a fonte constitui confirmação documental parcial do elo Raimundo–Manoel; a imagem original deve ser lida para estabelecer o parentesco com segurança.


A tentativa de localizar automaticamente o item de 1983 por busca textual não encontrou o título na captura atual, embora a página de fontes continue listando “1983 Raimundo José de Souza”. A grade dinâmica e a posição expandida do registro de 1941 dificultam a seleção direta; a fonte de 1983 permanece como próxima fonte indexada a abrir.


A página de fontes foi rolada até o final. Os cartões de `1949 Raimundo de Souza Finão Maniculta` e `1983 Raimundo José de Souza` estão visíveis, mas o cartão de 1983 ainda não foi expandido. A próxima leitura deve começar por esse botão, sem novas rolagens desnecessárias.


**Fonte civil do óbito de Raimundo:**

A fonte `1983 Raimundo José de Souza` foi expandida e aponta para `https://familysearch.org/ark:/61903/1:1:68DD-YZVR`. A citação identifica uma entrada para **Raimundo José de Souza** e **Manoel José de Souza**, com data de evento em **09/09/1983**. A fonte está marcada com Birth, Death, Sex e Name e foi anexada por `LilicaJustino` em 28/01/2023.

A página pública direta da ficha não renderizou os campos nesta tentativa, mas a fonte fornece confirmação indexada independente da data de óbito já exibida no perfil. A presença de Manoel José de Souza na mesma entrada pode ser um participante/declarante ou relação familiar e requer leitura dos campos completos; não deve ser interpretada automaticamente como parentesco adicional.


**Retomada do bloqueio 1 — MyHeritage Felippe Thomaz:**

A URL `https://www.myheritage.hu/names/felippe_thomaz` foi aberta no navegador real em 19/08/2026. Tanto a navegação quanto a captura seguinte retornaram página sem elementos e sem screenshot disponível; o navegador não expôs o texto “Security check” nem um controle de CAPTCHA. O bloqueio continua registrado, mas não há uma tela verificável para o usuário resolver neste momento. A próxima tentativa deverá usar a rota no mesmo navegador após recarregar ou retornar à página pública do MyHeritage que já havia sido liberada.


**Bloqueio 1 resolvido — conteúdo MyHeritage de Felippe Thomaz:**

Após o usuário concluir o antirobô, a página `https://www.myheritage.hu/names/felippe_thomaz` carregou. Ela mostra resultados derivados de árvores do MyHeritage para homônimos chamados Felippe Thomaz, sem confirmação direta de que algum seja o Felippe relacionado a Rosalina Schell.

O primeiro perfil exibido é Felippe Thomaz, 1878–1961, com 11 irmãos indicados, incluindo Mathias Tomas e Filippo Tomas. O perfil lista casamento com Dominga/Domingas Thomaz (Faoro) em 1899, uma filha chamada Ursula Alves Ferreira (Fabro Thomaz), depois casamento com Elizabeth/Izabel Thomaz (Jagher) em 1907 e 11 filhos, entre eles Domingas Rocco (Thomaz) e Agueda Alberti (Thomaz), além de uma união posterior sem cônjuge nomeado e uma filha Maria Tomaz. Outro resultado mostra Felippe Thomaz nascido em 1870, casado com Anna Thomas (Martini) em 1892 e com seis filhos.

A página não forneceu localidade, imagem original, pais ou ligação nominal com Rosalina Schell, Carolina Thomaz, Wilbald Thomaz ou Frieda Hoff. Os dados serão mantidos como pistas derivadas e não serão incorporados à árvore. O bloqueio antirobô do item 2 foi considerado resolvido pelo usuário; a etapa seguinte é testar o próximo bloqueio relevante e manter o diário atualizado.


**Bloqueio 2 reavaliado — coleção civil do FamilySearch:**

A coleção `https://www.familysearch.org/en/search/collection/3741255` agora abriu normalmente na sessão autenticada, sem `about:blank` e sem novo CAPTCHA. A página identifica “Brazil, Rio Grande do Sul, Civil Registration, 1810–2022”, com busca por nome, evento, local, cônjuge, pai, mãe, palavra-chave, localização, tipo, lote e número DGS. Ela informa 1.519.432 registros, 97.155.270 pessoas e 933.552 imagens.

A descrição confirma que registros de nascimento podem conter pais, avós, naturalidade e testemunhas; casamentos podem trazer naturalidade, idade, ocupação e pais dos noivos; e óbitos podem trazer cônjuge, origem, pais, testemunhas e sepultamento. O bloqueio técnico de autenticação/coleção foi considerado **resolvido pela extensão**. A coleção agora passa a ser rota ativa de pesquisa, não página a ser liberada pelo usuário.


**Bloqueio 6 reaberto — cadastro ANOREG/Corregedoria:**

A URL `https://www.anoreg.org.br/files/RS-5096-3295.pdf` foi aberta novamente após a resolução do bloqueio anterior. A navegação e a captura seguinte permaneceram sem elementos, texto ou screenshot disponível; o CAPTCHA não foi exposto ao navegador automatizado nesta tentativa. O bloqueio continua pendente como validação administrativa de baixa prioridade, e os dados do cartório já foram confirmados por fonte cadastral alternativa.


**Bloqueio ANOREG resolvido por PDF fornecido pelo usuário:**

O usuário forneceu o arquivo `RS-5096-3295.pdf`, de uma página, emitido em Brasília em 24/02/2014 pela Corregedoria Nacional de Justiça, no relatório “Justiça Aberta”. A leitura visual confirmou os seguintes dados da serventia:

- Código CNS: **09.953-1**;
- Denominação: **Registros Públicos de Tapes**;
- Data da instalação: **08/01/1876**;
- Tipo: **Privatizado**;
- Situação: **em exercício**;
- Atribuições: Registro de Imóveis; Registro de Títulos e Documentos e Civis das Pessoas Jurídicas; Registro Civil das Pessoas Naturais; Registro de Interdições e Tutelas;
- Titular: **Mara Liane Peter**;
- Substituto: **Shirlei Rosalino Correa**;
- Município: **Tapes, RS**, bairro Centro, CEP **96760000**;
- Endereço: **Rua Felicíssimo de Alfonsin nº 806, sala 01**;
- Telefone: **(51) 3672-3773**;
- E-mail: **cartorio@marapeter.com.br**;
- Funcionários em regime de contratação CLT: 7; funcionários em regime estatutário: 0;
- Horário de funcionamento: de 09:00 às 17:00.

O PDF confirma administrativamente a serventia e suas atribuições, mas não contém nenhum registro de Alvino, Rosalina ou outro familiar. Portanto, ele serve para validar a rota institucional e o cartório responsável, não como prova genealógica. O bloqueio CAPTCHA/visualização da ANOREG foi considerado **resolvido** pelo arquivo fornecido pelo usuário.


**Reavaliação do bloqueio APERS:**

A plataforma `https://apers.rs.gov.br/pesquisa-acervo-plataforma-aap` agora carregou a página institucional normalmente, sem `about:blank`. Após fechar o aviso de cookies necessários, o serviço de pesquisa embutido não foi apresentado e exibiu a mensagem: “Devido a sua configuração de privacidade este serviço não poderá ser apresentado nesta página. Clique neste link para acessar o serviço.”

Isso substitui o diagnóstico anterior de falha genérica: o bloqueio atual é de incorporação/privacidade do navegador, não antirobô. A plataforma institucional está acessível e o índice do casamento Alvino/Rosalina continua preservado, mas é necessário abrir o link do serviço diretamente ou ajustar a permissão de conteúdo incorporado para recuperar a busca e os metadados.


**Rota direta do serviço APERS recuperada:**

O HTML da página institucional revelou o endereço direto `https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true`, apresentado quando o serviço não pode ser incorporado por privacidade. Essa rota abriu normalmente e exibiu os campos de busca livre.

A consulta foi preparada no serviço direto com a palavra `Schell` e ano inicial `1955`; o ano final ainda será preenchido antes de pesquisar. Essa rota contorna a falha de incorporação do APERS e permite tentar novamente a habilitação de Alvino Paulino de Souza + Rosalina Schell sem CAPTCHA ou pagamento.


No serviço direto do APERS, a consulta por `Schell` entre 1955 e 1955 foi preenchida e o botão “Pesquisar” foi acionado. A URL e a tela permaneceram inalteradas imediatamente após o clique, sem tabela de resultados visível; pode ser necessário aguardar mais tempo ou enviar a consulta por teclado. O serviço direto permanece acessível, portanto o bloqueio de incorporação foi parcialmente contornado.


**Achado APERS recuperado pela rota direta:**

A busca direta `https://buscadocumentos.apers.rs.gov.br/pesquisa-documentos?semHeaders=true` finalmente carregou os resultados para `Schell` entre 1955 e 1955. O APERS informou **250 registros em uma página**, agrupados por espécie documental e por aproximação fonética.

Na seção **Processo / Habilitação para casamento — Cartório do Registro Civil de Tapes**, o resultado estruturado exibiu exatamente quatro processos: Ademar Antunes Leal + Alvina Schell (1947), **Alvino Paulino de Souza + Rosalina Schell (1955)**, Cravilino Nogueira + Celanira Schell (1953) e Gabriel Pedro Leopoldo Schiehall + Maria Pereira (1945). A linha do casal pesquisado aparece como `ALVINO PAULINO DE SOUZA ROSALINA SCHELL 01/01/1955 Tapes`.

A rota direta confirmou que o resultado anterior não estava perdido: o registro é real no índice do APERS e pode ser filtrado por classificação “Cartório do Registro Civil de Tapes” e espécie “Processo / Habilitação para casamento”. O HTML/índice não exibiu número de processo nem imagem vinculada nessa leitura; a próxima tentativa será selecionar o cartão/linha ou exportar os resultados para obter o identificador documental.


A busca direta do APERS encontra `ALVINO PAULINO DE SOUZA + ROSALINA SCHELL` dentro de `Cartório do Registro Civil de Tapes`, na espécie `Processo / Habilitação para casamento`, ano 1955. A página tem 250 registros em uma única página e uma coluna de filtros à esquerda; a linha do casal está mais abaixo no agrupamento de Tapes. O cartão/checkbox de cada linha parece ser o controle disponível para seleção, mas ainda não há número de processo ou imagem exposta no texto do resultado.

Na tentativa visual do APERS, a coluna de filtros é um contêiner independente; duas rolagens de 462 px ainda deixaram visíveis apenas espécies de processos judiciais. A classificação `Cartório do Registro Civil de Tapes` aparece mais abaixo no mesmo contêiner, enquanto a grade de resultados permanece separada. Não houve CAPTCHA nem alteração de registros.

**Exportação estruturada do APERS — processo identificado**

O arquivo `exportacao-1787179224315.csv` finalmente revelou o identificador interno e o link do processo de habilitação pesquisado. A linha exata do casal é:

`Processo;Habilitação para casamento;Cartório do Registro Civil de Tapes;Arquivos;-1;;;Prenome noivo;ALVINO PAULINO DE;Nome noivo;SOUZA;Prenome noiva;ROSALINA;Nome noiva;SCHELL;Município;Tapes;;;Ano do processo;01/01/1955;;;-1;https://secweb.procergs.com.br/aap/ObtemDadosServlet?metodo=verArquivoPDF&NRO_INT_DOCUMENTO=180190`

Assim, o **NRO_INT_DOCUMENTO é 180190**. O link do APERS baixado diretamente por `curl` gerou um PDF válido de **18 páginas**, salvo como `/home/ubuntu/upload/apers_processo_180190.pdf`.

**Leitura inicial do PDF do processo 180190**

As primeiras páginas visíveis já confirmam pontos essenciais:

1. A capa do processo traz o título `HABILITAÇÃO DE CASAMENTO` no `Juízo Distrital de Vila Cerro Grande, 3º Distrito do Município de Tapes`, com os requerentes manuscritos **Alvino Paulino de Souza** e **Rosalina Schell**.
2. A autuação está datada de **12 de abril de 1955** em Vila Cerro Grande.
3. O termo de declarações para casamento, também em Vila Cerro Grande, informa que os requerentes pretendem casar-se em `23 de abril de 1955`.
4. O texto legível da declaração indica, em leitura preliminar:
   - **Alvino Paulino de Souza**, lavrador, nascido em **23 de fevereiro de 1897**, neste Estado, em Cerro Grande, filho legítimo de **Geremias de Souza** e **Anna Joaquina Paulino de Souza**.
   - **Rosalina Schell**, doméstica, nascida em **15 de dezembro de 1900**, neste Estado, em Cerro Grande, filha legítima de **Joaquim Schell** e **Cecilia** (sobrenome ainda não confirmado nesta leitura inicial).
5. A folha vista traz assinaturas/testemunhas e a assinatura de Rosalina; o texto também registra que o noivo não assinou por ser analfabeto, assinando a rogo outra pessoa.

Esses dados ainda precisam ser confirmados com nova leitura das páginas seguintes e, idealmente, com transcrição integral mais nítida, mas já constituem a primeira prova primária robusta ligando Rosalina Schell a pais nomeados e ao núcleo de Cerro Grande/Tapes.

**Leitura intermediária do PDF do processo 180190 (págs. 6–10)**

As certidões juntadas ao processo corrigem e fortalecem a leitura preliminar das declarações:

- A certidão de nascimento de **Alvino Paulino de Souza** informa que ele nasceu em **23 de fevereiro de 1897**, em `Americana, neste distrito` (3º distrito do município de Tapes), sexo masculino, cor branca, filho de **Geremias de Souza** e **Anna Joaquina Paulino de Souza**. Os avós paternos aparecem como **Alexandrino de Oliveira e Souza** e **Felicia Rodrigues de Souza**; os maternos, como **Joaquim Paulino Tavares** e **Victoria Tavares**.
- A certidão de nascimento de **Rosalina Schell** informa que ela nasceu em **16 de dezembro de 1906** (não 1900), em `Americana, neste distrito`, sexo feminino, cor branca, filha de **Regino Schell**. Os avós maternos legíveis são **Carlos Schell** e **Anna Schell**. O campo da mãe não ficou claramente legível nesta visualização e precisa de nova confirmação.
- O `Atestado de Conhecimento` declara que **Alvino Paulino de Souza** e **Rosalina Schell** eram solteiros, naturais deste Estado, domiciliados e residentes no distrito, sem parentesco em grau proibido e sem impedimento para casar. O documento foi assinado em **18 de abril de 1955** e menciona a expedição do edital de proclamas no mesmo dia.

Com isso, o processo APERS já fornece uma ligação primária concreta do ramo Schell a uma geração anterior em Cerro Grande/Tapes, com pelo menos o pai de Rosalina identificado como **Regino Schell** e dois avós maternos/paternos conforme as certidões anexas. A leitura das páginas finais poderá esclarecer a mãe de Rosalina e o texto do assento matrimonial.

**Leitura avançada do PDF do processo 180190 (págs. 11–15)**

As páginas seguintes completam a tramitação formal da habilitação:

- Há conclusão ao juiz e despacho de `Nada opor`, datado de **16 de abril de 1955**, indicando deferimento do prosseguimento da habilitação.
- O **Edital nº 886** resume os nubentes e confirma, em leitura suficientemente legível, que:
  - **Alvino Paulino de Souza** era solteiro, natural de **Cerro Grande**, agricultor, nascido em **23 de fevereiro de 1897**, filho legítimo de **Geremias de Souza** e **Anna Joaquina Paulino de Souza**.
  - **Rosalina Schell** era solteira, natural de **Cerro Grande**, nascida em **16 de dezembro de 1906**, filha legítima de **Regino Schell** e de mãe cujo nome permanece difícil de ler nesta visualização.
- O edital certifica que os contraentes juntaram os documentos exigidos pelo art. 180 do Código Civil, inclusive certidões de nascimento e atestado de conhecimento.
- Outra certidão confirma que o edital esteve afixado em lugar público e de costume pelo prazo legal, **sem impedimento ao casamento**.
- O promotor ad hoc declarou que a habilitação estava com as formalidades legais, e o escrivão certificou que os contraentes se achavam habilitados a requerer a celebração do casamento no prazo da lei.
- As páginas 14 e 15 registram custas, selos e a juntada final dos autos em **19 de abril de 1955**.

Até esta altura do processo, o ponto genealógico decisivo já está estabelecido documentalmente: **Rosalina Schell**, moradora do 3º distrito de Tapes/Cerro Grande, nascida em 1906, é filha legítima de **Regino Schell**; a habilitação fornece ainda o conjunto completo de ascendência imediata de Alvino e sugere que a mãe de Rosalina provavelmente também aparece no edital/certidão, faltando apenas leitura mais nítida.

**Páginas finais do processo APERS nº 180190 (págs. 16–18)**

As páginas finais resolvem a data efetiva do casamento e trazem a principal averbação nominal:

- Em petição dirigida ao Juiz de Paz, **Alvino Paulino de Souza e Rosalina Schell** afirmam estar habilitados e requerem a celebração do casamento.
- A petição declara expressamente: **“A contraente depois de casada passará a assinar-se Rosalina Schell de Souza.”** Isso documenta a transição do nome de solteira para o nome usado na árvore familiar.
- A certificação final do cartório informa que, em **17 de abril de 1955**, foi registrado no cartório o matrimônio de **Alvino Paulino de Souza com Rosalina Schell**, conforme termo lançado no livro matrimonial do cartório; o número/livro aparece manuscrito e deve ser citado com cautela até leitura ampliada.
- A mesma página certifica que foram feitas as averbações. A página intermediária do processo e a anotação final também mencionam a celebração na sede do **3º distrito de Tapes/Vila Cerro Grande**.

Conclusão documental do processo: o casamento de Alvino Paulino de Souza e Rosalina Schell é confirmado por fonte primária do APERS, com data efetiva de **17/04/1955**, local administrativo de **Vila Cerro Grande, 3º distrito de Tapes**, e nome pós-casamento **Rosalina Schell de Souza**.

**Árvore GEDCOM independente criada e validada**

Foi criada a pasta `/home/ubuntu/gedcom_pesquisa_jonathan/` com:

- `arvore_pesquisa_jonathan.ged`: GEDCOM UTF-8, versão 5.5.1, com 26 indivíduos, 10 famílias e 7 fontes.
- `pessoas_evidencias.csv`: inventário auditável das pessoas, IDs FamilySearch, status, datas e observações.
- `LEIA-ME.md`: regras de confiança, conflitos e prioridades da árvore de pesquisa.

O validador local encontrou 44 registros de nível zero, 26 indivíduos, 10 famílias e 7 fontes, sem referências internas desconhecidas e sem erros de sintaxe detectados. A família F5 liga Alvino Paulino de Souza a Rosalina Schell, inclui o casamento de 17/04/1955 em Vila Cerro Grande/Tapes e referencia as fontes APERS do CSV e do PDF nº 180190. A árvore original do FamilySearch não foi alterada.

**Busca prioritária — nascimento de Rosalina Schell**

Na fase de investigação do assento original, o serviço direto do APERS foi consultado por `Rosalina`, com ano inicial e final **1906**. A página de resultados abriu, mas permaneceu exibindo os indicadores de carregamento; o HTML foi salvo em `/home/ubuntu/upload/buscadocumentos.apers.rs.gov.br_lista-documentos_semHeaders_true_1787180434497.html` para análise programática. Nenhum novo registro foi considerado evidência antes da leitura do HTML/CSV.

**FamilySearch — coleção de Registro Civil do Rio Grande do Sul**

A coleção `Brazil, Rio Grande do Sul, Civil Registration, 1810–2022` está acessível na sessão autenticada. A descrição oficial informa que registros de nascimento podem conter data e local do nascimento, pais, naturalidade e nomes dos avós maternos e paternos; registros de casamento podem conter naturalidade e pais dos noivos. A coleção possui registros civis do Rio Grande do Sul e deve ser usada para localizar o assento original de Rosalina Schell em 1906 e, depois, o nascimento de Rosalvino em 1940.

O formulário renderizado oferece campos de nome, sobrenome, nascimento, local, membros da família e palavra-chave. A página foi aberta sem resultados ainda; nenhuma pesquisa foi enviada nesta etapa.

**FamilySearch — busca exata de Rosalina Schell em 1906**

A consulta na coleção civil `3741255`, com nome `Rosalina Schell`, ano de nascimento 1906–1906 e local `Cerro Grande, Tapes, Rio Grande do Sul, Brazil`, retornou **0 resultados**. Isso não contradiz a certidão anexada ao APERS; o campo de local pode estar indexado como Americana, Tapes, São Jerônimo ou apenas no cartório, e o registro pode não estar indexado nominalmente. A próxima tentativa será remover o filtro de localidade e ampliar o nome/data, sem aceitar homônimos sem comparação documental.

**FamilySearch — busca ampliada de Rosalina Schell em 1906**

A segunda consulta na coleção civil `3741255`, agora sem filtro de localidade e apenas com `Rosalina Schell` e ano de nascimento 1906–1906, também retornou **0 resultados**. O nascimento de Rosalina continua apoiado no documento primário anexado ao processo APERS nº 180190, não em um índice FamilySearch. A ausência pode significar que o livro/assento não está indexado nominalmente ou que o nome foi transcrito com outra forma; a investigação deve migrar para imagens/browse por cartório e para o assento de casamento, sem tratar buscas vazias como refutação.

**FamilySearch — waypoints de imagens da coleção Registros Diversos 1748–1998**

A página oficial da coleção `1985805` confirma a opção gratuita **Browse All 2,919,774 Images**. A lista de municípios inclui explicitamente **Cerro Grande**, **Camaquã**, **São Jerônimo** e **Tapes**, além de outros municípios relevantes. A descrição informa que os livros civis costumam ser cronológicos e que registros de nascimento normalmente trazem a criança, data/local, pais e avós; a coleção contém cópias de registros civis do APERS. Esta é agora a rota prioritária para consultar imagens do livro de nascimento de Rosalina em 1906, pois as buscas nominais FamilySearch retornaram zero.

A página de waypoints está aberta no navegador; é necessário selecionar o município e seguir a hierarquia de fundos/livros até o período de 1906. Nenhum assento foi lido ainda.

**FamilySearch — waypoint Cerro Grande**

O município/waypoint `Cerro Grande` na coleção `1985805` abriu uma hierarquia de **habilitações de matrimônios do Fundo 65**, em caixas 26–39, com letras e períodos entre 1839 e 1955. A lista inclui caixas com letras R–S e S, potencialmente úteis para casamento, mas não mostrou livros de nascimento de 1906. O processo APERS nº 180190 de Alvino e Rosalina já foi localizado independentemente; para o nascimento de Rosalina, a próxima rota será o waypoint de **Tapes**, onde podem existir livros civis ou outros fundos.

**FamilySearch — registros católicos e waypoint Tapes**

A coleção gratuita `Brazil, Rio Grande do Sul, Catholic Church Records, 1738–1952` foi localizada como coleção `2177295`. Sua descrição oficial informa que batismos podem conter data e local de batismo, data/local de nascimento, legitimidade, pais e padrinhos; casamentos podem informar naturalidade, idade, residência e pais dos noivos. A navegação por imagens contém 184.012 imagens e a lista de municípios inclui **Tapes**, **Camaquã**, **São Jerônimo** e **Guaíba**. O waypoint de Tapes será consultado para localizar o batismo de Rosalina em 1906 e, posteriormente, o batismo/nascimento de Rosalvino em 1940.

**FamilySearch — paróquia Nossa Senhora das Dores, Tapes**

O waypoint católico de Tapes conduz à paróquia **Nossa Senhora das Dores**. A lista de livros disponíveis mostra batismos até `1895, Ago–1898, Set`, casamentos até `1890, Maio–1904, Dez` e óbitos até 1890. Portanto, esta paróquia não oferece, na coleção consultada, um livro de batismos de 1906 para Rosalina. O achado reduz a prioridade de Tapes/Nossa Senhora das Dores para o nascimento, mas a rota ainda pode ser útil para gerações anteriores; o próximo caminho é verificar São Jerônimo, Camaquã e possíveis livros paroquiais de Cerro Grande/São José da Fortaleza.

**FamilySearch — paróquia São João Batista, Camaquã**

O waypoint católico de Camaquã conduz à paróquia **São João Batista**. A lista de livros mostra batismos até `1896, Out–1901, Mar`, casamentos até `1895, Jul–1928, Out` e óbitos até 1900 na coleção. Não há, nessa rota, livro de batismos de 1906 para Rosalina. O livro de casamentos de 1895–1928 pode ser útil para famílias Schell/Tavares, mas não substitui o assento de nascimento. A próxima verificação é São Jerônimo, cuja jurisdição histórica também pode abranger registros de Cerro Grande/Tapes.

**FamilySearch — paróquia São Jerônimo**

O waypoint católico de São Jerônimo conduz à paróquia homônima. Os livros de batismo disponíveis chegam até `1899, Out–1901, Mar`; os livros de matrimônio chegam a 1918, mas não há livro de batismos de 1906. Assim, as três rotas paroquiais gratuitas consultadas — Nossa Senhora das Dores/Tapes, São João Batista/Camaquã e São Jerônimo — não cobrem diretamente o batismo de Rosalina em 1906. A prioridade documental permanece o assento civil original, a solicitação de pesquisa ao cartório/APERS sem pedido pago não autorizado, ou uma coleção ainda não navegada de Cerro Grande.

**FamilySearch — índice católico de Rosalina Schell**

A consulta direta na coleção `2177295`, com `Rosalina Schell` e nascimento 1906–1906, retornou **0 resultados**. Somada à ausência de livros paroquiais de 1906 nos waypoints de Tapes, Camaquã e São Jerônimo, a busca gratuita específica do nascimento foi esgotada nesta rodada sem localizar novo assento. O resultado não invalida o documento APERS nº 180190; indica que o assento pode estar fora da cobertura digital/indexada, sob outra paróquia ou em livro civil não disponível na navegação.

**Fase 4 — busca do nascimento de Rosalvino Schell de Souza em 1940**

A API pública do APERS foi consultada para 1940 com `Rosalvino`, `Rosalvino Schel` e `Rosalvino Schell`. A busca ampla retornou sete homônimos em Caçapava do Sul, Santa Vitória do Palmar, Porto Alegre, Rosário do Sul e Cruz Alta, todos processos/ocorrências sem conexão demonstrada com Tapes/Guaíba. As buscas exatas `Rosalvino Schel` e `Rosalvino Schell` retornaram zero resultados. Nenhum homônimo foi incorporado à árvore.

**FamilySearch — busca de Rosalvino em 1940**

As consultas diretas na coleção civil `3741255` por `Rosalvino Schell` e por `Rosalvino Schel`, com ano de nascimento 1940–1940 e sem localidade, retornaram **0 resultados** em ambas as grafias. O nascimento de Rosalvino continua sendo hipótese da árvore FamilySearch; a fonte indexada localizada até agora é o óbito de seu filho José Maria, que confirma o casal Rosalvino/Carolina no conjunto familiar, não o nascimento do pai.

A consulta ampliada do APERS por `Rosalvino`, entre 1929 e 1948 (102 resultados), foi filtrada por municípios e sobrenomes. Não apareceu nenhum resultado em **Tapes**, **Guaíba**, **Cerro Grande**, nem com `Schel`/`Schell`; os resultados destacados eram homônimos de outras localidades e processos judiciais. Nenhum foi usado para confirmar o nascimento de Rosalvino.

A busca civil do FamilySearch apenas pelo prenome `Rosalvino`, com ano 1940–1940 e sem sobrenome, também retornou **0 resultados**. Não há, nesta coleção nominal, registro indexado que possa confirmar diretamente o nascimento ou os pais de Rosalvino.

**FamilySearch — busca ampliada de Rosalvino, 1938–1942**

Ao ampliar a consulta civil para o prenome `Rosalvino` e nascimento 1938–1942, o FamilySearch retornou 170.364 resultados gerais. Os primeiros resultados legíveis eram homônimos, incluindo crianças de Arroio dos Ratos/São Jerônimo, Rosalvino Vieira da Rosa com óbito em Tapes e outros registros sem sobrenome Schell/Schel. Nenhum resultado apresentava simultaneamente Rosalvino Schell/de Souza, Tapes/Guaíba e os pais Raimundo José de Souza e Alicia Schell. A busca ampla foi considerada inconclusiva e não foi usada para alterar a árvore.

**Fase 5 — busca inicial do casamento de Raimundo José de Souza e Alicia Schell**

A API APERS foi consultada no período 1929–1948. `Alicia Schell` retornou zero resultados; `Alicia` retornou 134 homônimos; `Raimundo` retornou 409 homônimos; `Raimundo de Souza` retornou 10 ocorrências judiciais ou de outras localidades; e `Schell` retornou 27 ocorrências. No fundo do Cartório do Registro Civil de Tapes apareceu apenas **Alvina Schell**, casada com Ademar Antunes Leal em 1947, processo `NRO_INT_DOCUMENTO=180603`, sem relação demonstrada com Alicia. Não apareceu casamento de Raimundo/Alicia em Tapes, Cerro Grande ou Guaíba nessa janela e nenhuma ocorrência foi incorporada à árvore.

**Bloqueio de imagens — habilitações de Tapes**

A Caixa 20 de habilitações de matrimônios de Tapes, letra S, 1929–1947, foi aberta pela URL do waypoint `QZS2-GTV:1073785701,1073787201` e direcionou ao item `https://familysearch.org/ark:/61903/3:1:3QS7-89KQ-Y8XM?cc=1985805`. O visualizador exibiu **Image Restricted**, informando que o acesso é determinado por leis locais ou pelo custodiante do documento. Assim, não foi possível ler as imagens da Caixa 20 para procurar Raimundo/Alicia. As caixas 21, 23 e 25 permanecem como possíveis rotas, mas podem estar submetidas à mesma restrição; nenhum pedido pago foi feito.

**FamilySearch — busca do casamento Raimundo Souza e Alicia Schell**

A consulta direta na coleção civil `3741255`, com Raimundo/Souza, cônjuge Alicia/Schell e intervalo de casamento 1930–1945, retornou **0 resultados**. O índice civil não confirmou o casamento; a imagem da Caixa 20 de habilitações de Tapes também está restrita. O casamento permanece hipótese da árvore FamilySearch, e a próxima fonte gratuita possível é uma busca por imagens de outras caixas de Tapes ou a coleção paroquial de São José da Fortaleza/Cerro Grande, caso exista fora dos waypoints atuais.

A inspeção isolada dos 134 resultados APERS por `Alicia` confirmou que os registros em Tapes são homônimos: Algémiro Lopes Meirelles + Lícia Pereira (1941, NRO_INT_DOCUMENTO 179606), Pedro de Oliveira Caldas + Acácia Lopes Pereira (1938, NRO_INT_DOCUMENTO 178096) e Manoel Pereira dos Santos + Lícia Peres da Silva (1931, NRO_INT_DOCUMENTO 178950). Não aparece `Alicia Schell`, `Alicia de Souza` ou Raimundo como noivo nesses itens.

A busca civil ampliada no FamilySearch por `Raimundo Souza`, casamento entre 1930 e 1945 e local Tapes, sem exigir o nome de Alicia, retornou **0 resultados**. Portanto, o índice civil não oferece atualmente uma rota nominal para o casamento do casal; a evidência continua restrita à árvore colaborativa e aos bloqueios de imagens das habilitações.

A consulta na coleção católica `2177295` por `Raimundo Souza`, cônjuge `Alicia Schell` e casamento entre 1930 e 1945 retornou **0 resultados**. Não foi localizado casamento paroquial indexado; a restrição das imagens civis continua sendo o principal bloqueio documental da fase 5.

**Fase 6 — primeira busca por Regino Schell no APERS**

O índice APERS foi consultado por `Regino`, `Regino Schell` e `Schell`, dividindo o período em 1890–1909 e 1910–1928. `Regino Schell` retornou zero; `Regino` trouxe homônimos de Santa Vitória do Palmar, Ijuí, Quaraí e outras comarcas; e `Schell` trouxe ocorrências de Passo Fundo, Porto Alegre, São Borja e Taquara. Não apareceu `Regino` em Tapes/Cerro Grande nem qualquer `Schell` no Cartório do Registro Civil de Tapes antes de 1929. Nenhum homônimo foi incorporado.

A consulta direta na coleção civil FamilySearch `3741255` por `Regino Schell`, sem restringir ano ou evento, retornou **0 resultados**. A ausência no índice civil não exclui a pessoa: Regino é conhecido pela certidão primária de Rosalina no processo APERS nº 180190, e o próximo foco deve ser localizar registros de casamento/óbito ou batismo em imagens e fundos históricos de Tapes/Camaquã/São Jerônimo.

A consulta direta na coleção católica FamilySearch `2177295` por `Regino Schell`, sem restrição de ano ou evento, retornou **0 resultados**. O ramo Regino permanece documentado apenas indiretamente pela certidão de Rosalina no APERS; não há, até aqui, registro paroquial nominal indexado para avançar à origem europeia.

A busca ampliada por `Regino` no APERS para 1929–1948 e 1949–1968 retornou muitos homônimos e erros fonéticos, mas o filtro específico do **Cartório do Registro Civil de Tapes** não encontrou nenhuma linha com `Regino`, `Schel` ou `Schell`. As ocorrências exibidas em Tapes eram nomes semelhantes, como Ercino/Eginio/Regina, sem relação demonstrada. Nenhum registro foi atribuído ao pai de Rosalina.

**Busca dos avós nomeados de Rosalina — Carlos Schell e Anna Schell**

As consultas APERS por `Carlos Schell`, `Anna Schell`, `Carlos Shell` e `Anna Shell`, divididas entre 1870 e 1928, retornaram apenas homônimos ou ocorrências em Porto Alegre, Passo Fundo, Pelotas, Ijuí, Taquara e outras localidades. Nenhum resultado apareceu no Cartório do Registro Civil de Tapes ou em Cerro Grande. Assim, os avós `Carlos Schell` e `Anna Schell`, embora legíveis na certidão anexada ao processo 180190, ainda não foram ligados a um documento histórico independente ou a uma naturalidade europeia.

**Busca pública por homônimos Schell**

O resultado público `ancestors.familysearch.org/GF2N-4LD` para João Carlos Schell, aparentemente de Passo Fundo, foi aberto, mas a página exibiu somente `SIGN IN / CREATE ACCOUNT`, sem eventos, pais ou fontes. Não foi possível verificar o conteúdo e nenhuma relação com Regino, Rosalina ou Tapes será presumida.

O resultado Geni encontrado para uma Anna Christina Schell/Felizardo redirecionou para a tela de login e não permitiu verificar eventos, pais ou fontes. A associação fica apenas como homônimo de Porto Alegre/Felizardo, sem conexão documental com Regino, Rosalina ou Tapes; não será incorporada à árvore.

A busca web aberta por `Regino Schell` combinada com `naturalidade`, `pais` e `imigração` não retornou resultados utilizáveis. Até aqui, não há evidência pública independente que atribua a Regino uma origem europeia; o sobrenome Schell permanece apenas uma pista linguística/contextual, não uma prova de nacionalidade.

**Verificação de privacidade no FamilySearch — 19/08/2026**

A conta autenticada `Jonathan2545` abriu o menu Family Tree e exibiu a opção **Family Groups**. A rota resultante foi `https://www.familysearch.org/en/groups/family/`, mas a página carregada não mostrou, no conteúdo extraído, uma opção explícita de criar uma segunda árvore privada independente. Family Groups deve ser tratado como área de colaboração/grupo, não como garantia de uma árvore privada separada. Nenhuma pessoa ou relação foi criada ou editada.

A documentação oficial do FamilySearch sobre a nova experiência de upload GEDCOM informa que o arquivo se torna uma árvore dinâmica separada, editável pelo proprietário e por colaboradores convidados; outros usuários podem visualizar pessoas falecidas, e a árvore pode ser configurada como privada. A mesma documentação diferencia essa árvore enviada da Family Tree colaborativa e confirma que o upload não deve ser tratado como edição automática da árvore global. Fonte: https://www.familysearch.org/en/help/helpcenter/article/the-new-gedcom-upload-experience (artigo 29510, 09/06/2026).

**Preparação do upload GEDCOM no FamilySearch — 19/08/2026**

Na conta autenticada `Jonathan2545`, foi aberta a área `https://www.familysearch.org/en/groups/files?from=import`. O arquivo `/home/ubuntu/gedcom_pesquisa_jonathan/arvore_pesquisa_jonathan.ged` foi selecionado com sucesso no formulário `Upload Your GEDCOM File`. O nome preenchido foi `Árvore de pesquisa — Jonathan Robert Silveira De Souza — documentos APERS`. A descrição informa que é uma árvore independente, baseada em fontes gratuitas e no APERS nº 180190, com hipóteses e conflitos marcados, e solicita que não haja mesclagem automática com a Family Tree colaborativa. O botão final `UPLOAD` ainda não foi acionado.

**Falha no upload GEDCOM — 19/08/2026**

O formulário autenticado do FamilySearch retornou `Can't process item — Unable to upload your file, please try again later` para o GEDCOM canônico. Uma segunda tentativa com `arvore_pesquisa_jonathan_fs_fallback.ged`, normalizada para ASCII, linhas de até 240 caracteres e cabeçalho GEDCOM 5.5.1 conservador, produziu a mesma mensagem. A árvore ainda não foi criada na conta e nenhuma edição foi feita na Family Tree colaborativa. O problema pode ser do serviço de upload ou de uma incompatibilidade não exposta pela mensagem.

**Family Group Tree criado — 19/08/2026**

O FamilySearch exibiu a confirmação `Group created successfully.` para o grupo **Pesquisa de ancestralidade — Jonathan Robert Silveira De Souza**. A opção de Family Group Tree foi ativada, a descrição e o código de conduta de pesquisa foram mantidos, e o consentimento para compartilhar nome/retrato com membros e convidados foi aceito conforme autorização do usuário. Ainda não foram adicionadas pessoas ou relações; a Family Tree colaborativa permanece inalterada.

**Family Group Tree ativo e núcleo copiado — 19/08/2026**

Após a edição do usuário, o FamilySearch abriu a árvore do grupo no endereço `https://www.familysearch.org/en/tree/pedigree/landscape/PFCW-PJ5`. O seletor superior mostra `Pesquisa de ancestralidade — Jonathan Robert Silveira De Souza`. Foram copiados para o grupo: Jonathan Robert Silveira De Souza, agora `PFCW-PJ5`; Valdeci Kenes de Souza, agora `PFCW-PJR`; e Ana Paula, agora `PFCW-PJT`. A árvore também exibe Rosalvino Schell de Souza como ancestral falecido vinculado ao perfil público `P4KK-1QH`, sem edição desse perfil.

A árvore de grupo está ativa e separada da FamilySearch Tree global. A próxima etapa é verificar como inserir fontes/notas e se o Family Group Tree permite criar cópias de pesquisa para pessoas falecidas; não editar os registros públicos de Rosalvino, Raimundo, Alvino ou Rosalina sem confirmação do escopo.

**Limitação confirmada da Family Group Tree — 19/08/2026**

A orientação oficial do FamilySearch informa que todos os participantes podem ver e editar os antepassados falecidos conectados às pessoas vivas do grupo, e que esses antepassados permanecem na árvore pública global; não há como torná-los visíveis somente ao grupo. Apenas pessoas vivas e pessoas confidenciais podem permanecer restritas ao grupo. Fonte: https://www.familysearch.org/en/help/helpcenter/article/see-and-edit-people-in-a-family-group-tree.

Consequência operacional: Jonathan, Valdeci e Ana Paula foram copiados para a Family Group Tree privada, mas não serão criados, editados ou enriquecidos ali os ancestrais falecidos Alvino, Rosalina, Regino, Rosalvino, Raimundo ou Alicia, pois isso poderia alterar a árvore pública colaborativa. O GEDCOM e o relatório permanecem como a versão completa e privada da pesquisa.

**Verificação final de sessão — 19/08/2026**

A URL `https://www.familysearch.org/en/tree/pedigree/landscape/PFCW-PJ5` continua abrindo no FamilySearch com o seletor `Pesquisa de ancestralidade — Jonathan Robert Silveira De Souza`, confirmando que a sessão está na árvore do grupo e não na árvore colaborativa global. A renderização visual variou entre carregamento completo e cartões ainda em carregamento; a leitura completa anterior confirmou os cartões `PFCW-PJ5` (Jonathan), `PFCW-PJR` (Valdeci) e `PFCW-PJT` (Ana Paula). Não foram realizadas novas edições nesta verificação e nenhum antepassado falecido foi editado.

**Verificação adicional da conta após pedido do usuário — 20/08/2026**

Foi inspecionada a conta autenticada `Jonathan2545` sem executar alterações. Em `https://www.familysearch.org/en/groups/trees`, a seção “Groups With Trees” exibiu apenas um grupo: `Pesquisa de ancestralidade — Jonathan Robert Silveira De Souza`. O grupo corresponde ao código `9MMF-QLN` e, ao abrir sua árvore, o FamilySearch redirecionou para a pessoa inicial `PFCW-PJ5` da mesma árvore já criada.

A página `https://www.familysearch.org/en/tree/private-people` exibiu exatamente 3 pessoas privadas/vivas: `PFCW-PJT` (ana paula), `PFCW-PJ5` (Jonathan Robert Silveira De Souza) e `PFCW-PJR` (Valdeci kenes de souza). Não apareceu uma segunda árvore privada nem outro conjunto de pessoas privadas.

A seção `https://www.familysearch.org/en/search/genealogies` foi aberta e confirmou que “Genealogies” é o diretório público de árvores compartilhadas e do Pedigree Resource File; a busca nominal exigiu mais dados e não mostrou uma importação pessoal da conta. Nenhum GEDCOM adicional ou importação concluída ficou visível. A busca não foi submetida com dados adicionais e nenhuma alteração foi realizada.

**Novas fontes institucionais consultadas — continuidade da pesquisa**

A página oficial do APERS sobre Registro Civil confirma que o acervo contém livros de nascimentos, casamentos e óbitos de 1929 a 1975, além de processos de habilitação de casamento de 1890 a 1985. A lista de fundos inclui Tapes, Camaquã, Guaíba e São Jerônimo, todos relevantes ao ramo pesquisado. Fonte: https://www.apers.rs.gov.br/acervo-registro-civil.

A página oficial do Ministério Federal das Relações Externas da Alemanha informa que as representações alemãs não realizam pesquisas genealógicas nem mantêm registros de imigração, mas menciona listas de matrículas consulares de 1869 a 1941 e indica o Instituto Genealógico do Rio Grande do Sul, com banco de cerca de 15.000 nomes registrados entre 1824 e 1993, como rota potencial. A página também aponta o Arquivo Nacional para registros brasileiros de imigração e naturalização. Fonte: https://brasil.diplo.de/br-pt/servicos/nacionalidade/antepassados-2602086.

Essas fontes orientam novas buscas, mas não constituem evidência de que Regino, Carlos ou Anna Schell fossem alemães ou europeus.

**Rota gratuita do Arquivo Nacional identificada — continuidade da pesquisa**

A página oficial “Entrada de Estrangeiros” do Arquivo Nacional informa que a base SIAN reúne listas de entrada por diversos portos e que a consulta deve considerar o nome do estrangeiro, porto, navio e período. Para imigrantes sem data de chegada, a instituição também indica a base do Porto do Rio de Janeiro (1875–1910), o Registro Nacional de Estrangeiros/RNE (prontuários de 1939–1987) e processos de naturalização (1823–1959), estes últimos mediante solicitação com nome completo e filiação. As regiões Sul e Sudeste são atendidas pelo acervo do Rio de Janeiro. Fonte: https://www.gov.br/arquivonacional/pt-br/servicos/acervos/copy_of_acervos-mais-consultados/entrada-de-estrangeiros.

A rota é potencialmente útil para Regino Schell ou para Carlos/Anna Schell, mas a pesquisa ainda não tem data de chegada, porto, navio, filiação completa ou prova de que eram estrangeiros. Não foi feita solicitação ao Arquivo Nacional e nenhuma taxa foi contratada.

**Leitura visual inicial da habilitação APERS nº 180603 — 20/08/2026**

As páginas 1 a 5 do processo `180603` confirmam tratar-se de uma `Habilitação de Casamento` autuada no Juízo Distrital de Vila Cerro Grande, 3º distrito de Tapes, em 15/10/1947, entre **Ademar Antunes Leal** e **Alvina Schell**.

A petição datilografada informa que:

- **Ademar Antunes Leal** nasceu no 3º distrito de Tapes em **12/08/1926**, era filho legítimo de **Veríssimo Antunes Leal** e **dona Maria Goulart Leal**, natural do Estado, agricultor, residente e domiciliado no distrito.
- **Alvina Schell** nasceu no mesmo 3º distrito de Tapes em **29/06/1926** e era **filha ilegítima de dona Rosalina Schell**, natural do Estado, doméstica, residente e domiciliada no distrito.
- A própria petição afirma que ambos residiam na **6ª zona de 1898**; a expressão deve ser conferida depois em leitura mais minuciosa, mas a filiação de Alvina a Rosalina Schell é clara.

Esse achado é potencialmente relevante para a pesquisa principal porque sugere a existência de **outra Rosalina Schell viva e em idade compatível para ser mãe em 1926**, distinta ou anterior à Rosalina Schell que casou com Alvino em 1955 e cujo nascimento no processo 180190 foi lido como 16/12/1906. Portanto, a homonímia de `Rosalina Schell` aumenta e exige desambiguação rigorosa antes de qualquer vínculo entre Alvina e a linha de Jonathan.

**Leitura visual complementar da habilitação APERS nº 180603 — páginas 6 a 10**

As páginas 6 a 10 reforçam e refinam o achado anterior:

- A página 8 traz atestado policial para fins de casamento confirmando **Alvina Schell**, sexo feminino, cor branca, nascida em **29/06/1926**, filha ilegítima de **dona Rosalina Schell**, natural deste Estado, de profissão doméstica, solteira e domiciliada no distrito. O texto ainda menciona como avó da referida Alvina **Abigail Schell** e, ao que tudo indica, como avô **Regino Schell**; essa leitura deve ser conferida mais uma vez, mas o nome `Regino Schell` aparece com força paleográfica relevante.
- A página 10 contém declaração de testemunhas afirmando que dona Alvina Schell e Ademar Antunes Leal não eram parentes em grau proibido. As assinaturas visíveis parecem corresponder a **Camillo/Camilo Mariano dos Passos** e **Geronimo/Geronias Grande de Oliveira Netto**; são testemunhas, não parentes diretos.
- A página 11 certifica que o edital foi afixado e que o casamento requerido por Ademar Antunes Leal e Alvina Schell estava dividido em registro no **livro nº 4, folha 60**.

Implicação genealógica provisória: o processo `180603` sugere fortemente que **Regino Schell** já estava presente em Tapes/Cerro Grande ao menos como nome da geração anterior de Alvina Schell. Isso pode indicar que Alvina pertence ao mesmo núcleo Schell pesquisado em Rosalina, mas a relação exata ainda não está provada. Também surge um novo nome relevante, **Abigail Schell**, que deve ser tratado como hipótese documental até leitura adicional das demais páginas ou novo documento independente.

**Leitura visual complementar da habilitação APERS nº 180603 — páginas 11 a 15**

As páginas 11 a 15 não trouxeram novas certidões de nascimento, mas consolidaram o contexto administrativo do casamento:

- O **edital número 472** repete a síntese do casal e confirma novamente que **Alvina Schell**, nascida em **29/06/1926**, era **filha ilegítima de dona Rosalina Schell**, natural do Estado e domiciliada no distrito.
- O edital declara que Ademar era filho legítimo de Veríssimo Antunes Leal e Maria Goulart Leal; já para Alvina, a única filiação explícita nessas páginas continua sendo a mãe **Rosalina Schell**.
- As páginas seguintes registram a tramitação do processo perante o juiz distrital, compromisso do promotor ad hoc, juntada de peças e o requerimento final para marcação da celebração em **04/10/1947**, em casa de **Sr. Fioravante Massardini**, no interior do distrito.

Implicação provisória: até a página 15, o processo `180603` confirma com segurança a existência de uma **Rosalina Schell mãe de Alvina**, ativa em Cerro Grande/Tapes antes de 1947. Isso fortalece a hipótese de homonímia importante dentro do mesmo núcleo local, mas ainda não demonstra se essa Rosalina é a mesma pessoa que aparece no processo `180190` de 1955 ou uma parente de geração distinta.

**Leitura visual final da habilitação APERS nº 180603 — páginas 16 a 20**

As páginas finais confirmam o encerramento do processo e, principalmente, o registro do casamento:

- O escrivão certifica que o casamento requerido por **Ademar Antunes Leal** e **Alvina Schell** foi regularmente anunciado pelo edital e não sofreu impugnação.
- A certidão final informa que, em **04/10/1947**, o casamento foi registrado no **livro nº 6, folha 63, sob o nº 400** do cartório de Vila Cerro Grande, 3º distrito de Tapes.
- As páginas 19 a 20 tratam apenas de custas e folhas em branco, sem novos nomes genealógicos relevantes.

Conclusão parcial deste documento: a habilitação `180603` confirma por fonte primária que **Alvina Schell** casou em 04/10/1947 em Vila Cerro Grande/Tapes e que era **filha ilegítima de Rosalina Schell**. O processo não demonstrou, por si só, que essa Rosalina seja a mesma pessoa do processo `180190`; ao contrário, a cronologia sugere que pode ser uma homônima ou parente de geração diferente. O nome **Regino Schell** segue como pista forte no próprio processo e deve ser reavaliado em nova leitura focalizada da página do atestado policial.

**Correção paleográfica importante — processo APERS 180603, página 7**

A ampliação individual da página 7 mostra o atestado do subdelegado Ramiro Gama Bilhalva. O texto confirma que **Alvina Schell**, nascida em 29/06/1926, era filha ilegítima de **Rosalina Schell** e informa, na linha seguinte, “sendo avó da referida Alvina Schell: **Regina Schell**”. A leitura ampliada favorece **Regina Schell**, nome feminino, e não `Regino Schell`. Assim, a menção anterior a Regino no processo 180603 deve ser corrigida: neste documento, a avó indicada de Alvina é provavelmente Regina Schell.

Essa correção elimina, por enquanto, a suposta evidência de que o processo 180603 ligaria diretamente Alvina ao **Regino Schell** que aparece como pai de Rosalina no processo 180190. A conexão entre os dois núcleos Schell continua aberta; a única relação segura em 180603 é Alvina ← mãe Rosalina Schell, com avó Regina Schell conforme a leitura ampliada.

**Nova fonte primária Schell — habilitação APERS nº 180674**

A habilitação de casamento `180674`, localizada no mesmo CSV do APERS para o Cartório de Tapes, é de **Cravilino Nogueira e Celanira Schell**, autuada em 12/10/1953 no Juízo Distrital de Vila Cerro Grande, 3º distrito de Tapes.

A petição visível na página 4 informa que:

- **Cravilino Nogueira** nasceu em 04/10/1926, filho legítimo de **Ernesto José Nogueira** e **Hermínia Lopes Santos**, ambos naturais do Estado e falecidos, respectivamente, em 1947 e 1951.
- **Celanira Schell** nasceu no distrito em **20/08/1934** e é filha de **dona Rosalina Schell**, natural do Estado, doméstica e residente no distrito.
- O processo é claramente de Tapes/Cerro Grande e traz testemunhas locais; não há, nesta página inicial, indicação de país europeu ou naturalidade estrangeira.

O achado confirma que uma mulher chamada **Rosalina Schell** teve pelo menos duas filhas identificadas em habilitações de Tapes: **Alvina Schell** (nascida em 29/06/1926, processo 180603) e **Celanira Schell** (nascida em 20/08/1934, processo 180674). Isso cria uma nova linha documental para reconstruir a Rosalina mãe e distingui-la da Rosalina Schell que casou com Alvino Paulino de Souza em 1955.

**Leitura visual complementar da habilitação APERS nº 180674 — páginas 6 a 10**

As páginas 6 a 10 trazem a prova mais importante do processo `180674`: a certidão de nascimento de **Celanira Schell** e a declaração de consentimento de sua mãe.

- A certidão de nascimento confirma **Celanira Schell**, sexo feminino, cor branca, nascida em **20/08/1934**, no **3º distrito de Tapes**, em domicílio, registrada sob o **nascimento nº 328**, no **livro nº 13-A**. Ela aparece expressamente como **filha ilegítima de Rosalina Schell**. Os campos de ascendência paterna não aparecem preenchidos e a linha de avós maternos parece não ter sido completada no talão visível.
- A certidão foi expedida em **28/01/1953** pelo oficial do 3º distrito de Tapes. O nome do declarante/testemunha na certidão parece ser **Carlos Felipe Konig**, leitura a confirmar.
- A página seguinte contém um **termo de declaração para casamento** em que **Rosalina Schell** declara dar pleno consentimento para sua filha **Celanira Schell** casar com **Sr. Cravilino Nogueira**, datado de **12/10/1953**, no 3º distrito de Tapes, com assinatura da própria Rosalina.

Implicação genealógica: o processo `180674` confirma por fonte primária que **Rosalina Schell estava viva em outubro de 1953** e era mãe de **Celanira Schell**, nascida em 1934. Junto com o processo `180603`, isso demonstra com segurança documental que existe em Tapes/Cerro Grande uma **Rosalina Schell mãe de filhas ilegítimas nascidas ao menos entre 1926 e 1934**. Essa Rosalina deve ser tratada, por ora, como uma pessoa possivelmente distinta da **Rosalina Schell nascida em 1906 que se casou com Alvino Paulino de Souza em 1955**, até que um documento prove o contrário.

**Leitura visual complementar da habilitação APERS nº 180674 — páginas 11 a 15**

As páginas 11 a 15 repetem e consolidam a filiação já observada:

- O **atestado de conhecimento** afirma que os declarantes conheciam **Cravilino Nogueira** e **Celanira Schell**, ambos solteiros, naturais deste Estado e domiciliados no distrito, e declara que não eram parentes em grau proibido.
- A certificação do edital registra o casamento requerido por **Cravilino Nogueira** e **Celanira Schell** no **livro 6, folha 143, nº 828**, referência que deve ser conferida novamente ao final do processo, pois pode ser a anotação do edital e não a do assento final.
- O **edital nº 803** repete que Celanira nasceu em **20/08/1934** e era **filha de Rosalina Schell**, natural deste Estado, doméstica e residente no distrito. Não há nessas páginas indicação do pai de Celanira nem de naturalidade estrangeira para Rosalina.
- A tramitação judicial até a data de **27/10/1953** confirma que os autos seguiram regularmente, sem oposição aparente.

Implicação genealógica: o processo `180674` reforça documentalmente que a **Rosalina Schell mãe** era pessoa conhecida e residente em Vila Cerro Grande/Tapes em 1953. Esse núcleo familiar permanece fortemente documentado, mas ainda sem prova de ligação direta com **Regino Schell** do processo `180190`.

**Leitura visual final da habilitação APERS nº 180674 — páginas 16 a 20**

As páginas finais encerram o processo e trazem a confirmação do matrimônio. O requerimento de 30/10/1953 pede a celebração do casamento de **Cravilino Nogueira** com **Celanira Schell** sob o regime de **comunhão de bens**, para o dia 31/10/1953, às 11 horas. A certidão final informa que o casamento foi registrado em **31/10/1953** no **livro nº 7-A, folha 198, sob o nº 723** do cartório de Vila Cerro Grande, 3º distrito de Tapes.

Essa habilitação confirma por fonte primária que a mesma **Rosalina Schell** assinou o consentimento para o casamento de uma filha nascida em 1934 e que o núcleo familiar estava firmemente estabelecido em Tapes/Cerro Grande em 1953. Junto com a habilitação `180603`, o processo reforça a existência de uma linha materna local formada por **Rosalina Schell → Alvina Schell (1926)** e **Rosalina Schell → Celanira Schell (1934)**, o que torna indispensável desambiguar essa Rosalina antes de relacioná-la à Rosalina que casou com Alvino em 1955.

**Busca visual APERS por “Regina Schell” — 20/08/2026**

A pesquisa livre do APERS foi preenchida com `Regina Schell`, ano inicial `1940` e ano final `1960`, respeitando o intervalo máximo de 20 anos, e submetida pelo formulário oficial. A página de resultados mudou para `lista-documentos?semHeaders=true` e exibiu `Resultado de "Regina Schell"`, mas permaneceu indefinidamente com dois indicadores `carregando...`. Nenhum registro ou resultado foi lido; portanto, esta tentativa não confirma nem refuta a existência de documentos para Regina Schell. O bloqueio é técnico e foi registrado sem repetir a submissão.

**Busca aberta por Regina Schell — resultado negativo**

As buscas web direcionadas por `Regina Schell` em Tapes, Cerro Grande e Camaquã não localizaram registro genealógico ou civil utilizável. Os resultados foram principalmente homônimos contemporâneos estrangeiros ou páginas comerciais, sem conexão demonstrada com a Rosalina Schell mãe de Alvina e Celanira. A ausência de resultado não refuta a fonte primária APERS; apenas confirma que o próximo avanço dependerá de registros civis/paroquiais ou de pesquisa institucional.


**Repositório GitHub privado criado — 20/08/2026**

Após a conclusão desta rodada, foi criado o repositório privado `jonathanrobertsilveira-wq/pesquisa-ancestralidade-jonathan` em https://github.com/jonathanrobertsilveira-wq/pesquisa-ancestralidade-jonathan. O branch principal é `main`, o push foi concluído e a verificação da API do GitHub confirmou `isPrivate: true`. O repositório contém README, relatórios, diário, inventário de bloqueios, GEDCOM regenerado com 31 indivíduos/13 famílias/20 fontes, os PDFs APERS 180603 e 180674, o PDF 180190, CSVs, scripts, artefatos da nova rodada e pacotes arquivados.

O GitHub emitiu apenas um aviso de recomendação porque `archives/pacote_arvore_pesquisa_jonathan_2026-08-20.zip` tem aproximadamente 58 MB; o arquivo foi aceito e o push terminou com sucesso. Nenhuma credencial foi encontrada na verificação textual do conjunto. O repositório permanece privado.


**Rota do catálogo FamilySearch — continuação da pesquisa**

O catálogo oficial do FamilySearch foi aberto em `https://www.familysearch.org/en/search/catalog/`. A página informa que o catálogo permite pesquisar livros, registros, imagens e outros recursos por lugar, palavra-chave, título, autor, assunto, sobrenome, número de filme ou DGS, com filtro de disponibilidade online. Essa será a rota para procurar livros civis/paroquiais de Tapes e Vila Cerro Grande nos períodos de Alvina (1926), Celanira (1934) e da Rosalina mãe. A página não foi submetida com dados nesta etapa; nenhuma edição ou solicitação foi feita.


**Catálogo FamilySearch para Tapes — resultado da tentativa atual**

A busca textual do catálogo por `Tapes, Rio Grande do Sul, Brazil` carregou a página de catálogo e reconheceu o parâmetro de lugar na URL, mas não expôs registros, filmes ou DGS no conteúdo extraído. A busca aberta por URLs indexadas de catálogo para Tapes também não retornou resultado. A interface visual ficou indisponível ao tentar selecionar o lugar, portanto não foi possível avançar para um livro específico nesta sessão. Nenhuma conclusão negativa sobre a existência dos livros deve ser tirada desse bloqueio técnico.


**Tentativa FamilySearch — Alvina Schell, Tapes, 1926**

Foi preenchida a coleção `3741255` com `Alvina`, sobrenome `Schell`, local de nascimento `Tapes, Rio Grande do Sul, Brazil` e ano de nascimento `1926–1926`. A URL parametrizada foi formada corretamente, mas a interface permaneceu na página da coleção após o clique em `Search`, sem exibir lista de resultados ou mensagem de zero registros. Por isso, não tratar essa tentativa como busca negativa concluída; permanece um bloqueio de carregamento/execução da interface.


**Arquivo Nacional — rotas gratuitas e bloqueio CAPTCHA**

A orientação oficial do Arquivo Nacional informa que a base de Entrada de Estrangeiros no Porto do Rio de Janeiro cobre 1875–1910 e permite busca por nome, navio, data, nacionalidade, procedência e destino. A mesma orientação informa que prontuários RNE de 1939–1987 exigem nome completo, filiação e cidade do registro, e que processos de naturalização de 1823–1959 exigem nome completo e filiação. Para Regino, Regina, Carlos e Anna Schell ainda não temos esses dados suficientes.

As páginas públicas `https://consulta.an.gov.br/orientacaoDesembarque/1` e `https://sian.an.gov.br/` retornaram CAPTCHA antirobô com código de suporte `9682415139445422152` e `9682415139445422120`, respectivamente. Não houve tentativa de contornar o CAPTCHA. A orientação e o bloqueio foram registrados; a rota permanece disponível para pesquisa manual futura.


**Arquivo Nacional após resolução do CAPTCHA — bloqueio de segurança**

Após o usuário resolver e enviar o CAPTCHA, a página não liberou a consulta. Ao reabrir a rota, o Arquivo Nacional exibiu `Conteúdo restrito — Acesso Bloqueado por Motivos de Segurança`, atribuído às normas de segurança do MGI. Novo ID de suporte: `10107896255012111148`. A consulta nominal não foi executada e não houve resultado genealógico. O bloqueio anterior e este novo ID foram preservados para eventual chamado institucional.


**Revisão completa do CSV APERS por localidade**

O filtro do CSV nominal `Schell` para Tapes, Cerro Grande, Camaquã, Guaíba, São Jerônimo e Barão do Triunfo retornou apenas três habilitações de casamento locais: `180603` (Ademar Antunes Leal + Alvina Schell, 1947), `180190` (Alvino Paulino de Souza + Rosalina Schell, 1955) e `180674` (Cravilino Nogueira + Celanira Schell, 1953). Não há outro processo Schell local no CSV baixado que possa ser explorado sem uma nova consulta ao APERS ou a outra instituição.


**Busca aberta por Regino/Regina/Carlos Schell — avaliação**

As buscas abertas não localizaram Regino Schell ou um registro genealógico de Regina Schell ligado a Tapes. A ocorrência de `Carlos Schell` no catálogo da Exposição Estadual de 1901 é uma menção comercial a um expositor, sem filiação, local de residência ou ligação com a família pesquisada. A ocorrência de `Laura Regina Schell` em Novo Hamburgo é um cadastro empresarial contemporâneo de 2006 e não tem valor genealógico para a geração de Rosalina. Ambos foram classificados como homônimos/sem vínculo demonstrado e não serão incorporados à árvore.


**Arquidiocese de Porto Alegre — nova rota paroquial gratuita**

A página oficial da Arquidiocese de Porto Alegre informa que o **Arquivo Histórico da Cúria Metropolitana de Porto Alegre (AHCMPA)** guarda e disponibiliza documentação histórica da arquidiocese. O contato público é `arquivo@arquipoa.org.br`, telefone da Cúria `(51) 3228-6199`, endereço Rua Espírito Santo, 95, Centro Histórico, Porto Alegre, com atendimento de segunda a quinta-feira.

A página oficial do **Batistério** oferece o formulário institucional `https://www.servusigreja.com.br/sistema/solicitaBatisterio.php?id_u=1` para solicitações. Essa é uma rota legítima para perguntar pelos registros paroquiais de Tapes/Cerro Grande, mas nenhum pedido foi enviado nesta etapa e não houve cobrança ou contratação.
