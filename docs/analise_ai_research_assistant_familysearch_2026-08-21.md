# Análise do AI Research Assistant do FamilySearch

**Autor:** Manus AI
**Data da inspeção:** 21 de agosto de 2026
**Página principal analisada:** [FamilySearch Research Portal](https://www.familysearch.org/en/home/portal/) [1]

## Resumo executivo

O **AI Research Assistant** observado na página inicial do FamilySearch é, principalmente, um mecanismo de descoberta de oportunidades para ampliar a árvore genealógica. Ele não apresentou uma árvore pronta nem uma conclusão genealógica definitiva; apresentou **cinco pistas baseadas em registros existentes**, cada uma associada a uma possível relação ausente — sobretudo filho, mas também cônjuge — e encaminhou o usuário para revisão humana antes de qualquer inclusão.

Minha avaliação é **positiva para descoberta exploratória e triagem de fontes**, mas **cautelosa para confirmação genealógica**. O recurso economiza tempo ao destacar relações que poderiam passar despercebidas e conecta a pista diretamente ao registro, à visualização da relação e às ferramentas de anexação. Em contrapartida, a interface não mostrou um grau de confiança numérico nem uma explicação detalhada do algoritmo de correspondência. A sugestão deve ser tratada como **hipótese documentada**, nunca como prova de identidade.

Há ainda uma segunda experiência, em `/en/match/ade/aiassistant/chat`, apresentada como **“Chat with AI About Your Ancestors”**. Ela permite perguntas sobre pessoas da árvore, relacionamentos, eventos de vida e possíveis descobertas, mas o próprio FamilySearch a classifica como produto experimental do Labs, sujeito a erros, dados limitados e indisponibilidade. [6]

## O que foi observado na sessão

A sessão estava autenticada e o portal exibiu o cartão **“AI Research Assistant found new ancestors who could grow your family tree”**. Foram apresentadas cinco recomendações, exatamente dentro do limite descrito pelo FamilySearch em sua documentação oficial. [2]

| Relação sugerida | Pessoa-base mostrada no cartão | Evidência exibida ao abrir a sugestão | Ações disponíveis |
|---|---|---|---|
| Possível filho | Anna Joaquina de Souza | Maria Rita Souza Oliveira aparece como filha em um registro civil e não está na árvore | Review & Add, View Relationship, View Record, Ignore, Attach |
| Possível filho | Jeremias Antonio de Oliveira | Maria Rita Souza Oliveira aparece como filha em outro registro do mesmo conjunto | Review & Add, View Relationship, View Record, Ignore, Attach |
| Possível filho e cônjuge | Bibiano Costa Oliveira | Antonio Ignácio de Oliveira aparece como filho e Maria Ignacia Paulino de Souza como cônjuge, ambos ausentes | Review & Add, View Relationship, View Record, Ignore, Attach |
| Possível filho | Maria Luiza de Oliveira | A relação sugerida ainda não foi aberta nesta inspeção | Review & Add |
| Possível filho | Silvano Goulart Pinto | A relação sugerida ainda não foi aberta nesta inspeção | Review & Add |

O cartão não adiciona pessoas automaticamente. O fluxo exige que o usuário escolha **Review & Add** e, depois, decida se deve consultar o registro, conferir a relação e anexar a fonte. Essa separação entre descoberta e alteração é uma característica importante de segurança operacional.

## Como funciona o fluxo

O fluxo observado pode ser resumido em quatro etapas. Primeiro, o sistema examina a árvore e as correspondências de registros já disponíveis no FamilySearch. Segundo, destaca registros que, além de corresponderem potencialmente a alguém da árvore, contêm um possível pai, filho ou cônjuge ainda não representado. Terceiro, mostra a evidência e permite abrir o registro ou visualizar o caminho genealógico. Quarto, deixa a decisão final nas mãos do pesquisador, que pode ignorar, anexar ou continuar a verificação.

| Etapa | O que o usuário vê | Interpretação correta |
|---|---|---|
| Descoberta | Um cartão com “Possible child” ou “Possible child and spouse” | Uma pista gerada a partir de uma possível correspondência de registro |
| Revisão | Nome da pessoa ausente, registro associado e explicação da relação | Evidência inicial, ainda não uma confirmação |
| Contexto | Visualização do caminho entre a pessoa-base e o usuário | Ajuda a entender onde a sugestão se encaixa na árvore |
| Verificação | Página do registro, transcrição, imagem e metadados | Etapa necessária para testar identidade, datas, locais e relações |
| Decisão | Ignore, Attach ou continuidade pelo Source Linker | O usuário controla a alteração da árvore |

A documentação oficial confirma esse desenho: o FamilySearch afirma que os nomes são derivados de **record hints** já existentes e que cada pista deve ser revisada cuidadosamente antes de ser adicionada. [2] A página de ajuda descreve o recurso como uma lista de registros que parecem corresponder de perto a pessoas da linha familiar. [3]

> “All record hints (including the AI-driven, home-page hints) need careful review to make sure they are accurate.” — FamilySearch. [2]

## Verificação de uma fonte concreta

A primeira recomendação conduziu a um registro do conjunto **“Brasil, Rio Grande do Sul, Registro Civil, 1810–2022”**, relacionado a Maria Rita Souza Oliveira e Jeremias de Souza. A página mostrou Anna Joaquina Paulina de Souza como pessoa mencionada no registro e listou Maria Rita como filha. Também ofereceu a opção de abrir o documento original e comparar a possível correspondência com a árvore. [7]

O registro apresentou dados indexados como nome, sexo, idade, ano de nascimento, local, ocupação, raça e evento de falecimento. A página alertou explicitamente que o registro havia sido **indexado por computador** e que o usuário deveria utilizar a edição para corrigir eventuais erros. A imagem original era um documento manuscrito digitalizado, com visualizador, transcrição, metadados e possibilidade de alternar entre páginas.

A inspeção também revelou um ponto de atenção documental: a página do visualizador apresentou o título **“Sentinela do Sul. Death Records August 1969”**, enquanto a citação do registro mencionou uma entrada de 6 de março de 1977 e os detalhes indexados indicaram um evento em 3 de junho de 1977. Isso pode decorrer do título do item arquivístico, de metadados da coleção ou de inconsistência da indexação; não é possível concluir, apenas com a interface, que o documento esteja incorreto. É, porém, um excelente exemplo de por que a imagem original e a transcrição precisam ser conferidas.

## O que o assistente faz bem

A principal qualidade é a **priorização de pistas potencialmente úteis**. Em vez de exigir que o pesquisador procure manualmente todos os registros, o sistema apresenta oportunidades de extensão já contextualizadas na árvore. A descoberta de relações ausentes pode ser especialmente valiosa quando uma linha familiar parece “travada”.

Outra qualidade é a **rastreabilidade da sugestão**. O cartão não mostrou apenas um nome; mostrou a pessoa-base, a relação provável e o registro que sustentava a hipótese. A opção de visualizar a relação também apresentou o caminho genealógico entre a conta autenticada e a pessoa-base.

O recurso também lida com **mais de um tipo de relação**. No caso de Bibiano Costa Oliveira, um único registro produziu uma sugestão de filho e outra de cônjuge. Isso pode acelerar a reconstrução de um núcleo familiar inteiro, embora aumente a necessidade de validação individual.

Por fim, a experiência incorpora **controle humano antes da alteração**. O usuário pode ver a fonte, ignorar a pista ou prosseguir para anexação. Segundo o FamilySearch, o Source Linker permite comparar as pessoas do registro com a árvore e adicionar novos indivíduos somente após essa revisão. [2]

## Limitações e riscos

A primeira limitação é a falta de transparência sobre o cálculo da correspondência. Na interface observada, não apareceu pontuação de confiança, lista de critérios ponderados ou explicação detalhada de por que um nome foi preferido a outros. O sistema explica qual relação foi encontrada no registro, mas não explica integralmente por que considera aquela pessoa do registro compatível com aquela pessoa da árvore.

A segunda é o risco de **homônimos, relações incorretas e propagação de erros**. A indexação automática pode conter grafias equivocadas, idades erradas, datas inconsistentes ou relações transcritas incorretamente. Se o pesquisador aceitar uma sugestão sem comparar a imagem, um erro pode ser anexado à fonte e servir de base para novas sugestões.

A terceira é o risco de **contagem duplicada de evidência**. Nesta sessão, duas recomendações diferentes apontaram para a mesma possível filha, utilizando registros associados a dois pais diferentes no mesmo conjunto documental. Isso pode ser uma confirmação coerente da estrutura familiar, mas também pode ser o mesmo evento apresentado por duas rotas de correspondência. As duas pistas não devem ser tratadas automaticamente como duas provas independentes.

A quarta é a dependência de cobertura e qualidade dos dados do próprio FamilySearch. O anúncio oficial informa que o assistente utiliza record hints e bases de registros da plataforma; consequentemente, ele pode deixar de encontrar pessoas quando a documentação ainda não está digitalizada, indexada ou disponível na coleção consultada. [2]

A quinta é a maturidade do chat experimental. A interface conversacional declara que pode apresentar erros e dados limitados, não é garantida como sempre disponível e não conta atualmente com suporte para esse produto. [6] Portanto, o chat deve ser usado para formular perguntas e caminhos de investigação, não para substituir a análise documental.

## Privacidade e uso responsável

A política global de privacidade do FamilySearch, atualizada em 24 de março de 2026, declara que a plataforma processa dados enviados pelo usuário, dados enviados por outros usuários, dados registrados automaticamente e dados obtidos de terceiros ou de fontes públicas. Ela inclui dados genealógicos, relações familiares, biografias, fotos e informações históricas entre os dados que podem ser submetidos. Também informa que o processamento pode ser automático, manual ou misto e que o FamilySearch não toma decisões sobre o usuário baseadas exclusivamente em processamento automatizado com efeitos significativos. [5]

Para este recurso, a prática mais segura é trabalhar apenas com os dados necessários e evitar inserir ou compartilhar informações sensíveis de pessoas vivas, sobretudo quando não houver autorização. A própria política recomenda cautela com informações como origem étnica, raça, nacionalidade, religião, saúde ou imigração de terceiros vivos. [5] A análise da sessão não exigiu inserir novos dados pessoais nem iniciar o experimento conversacional.

## Avaliação qualitativa

| Dimensão | Avaliação | Justificativa |
|---|---|---|
| Utilidade para descobrir pistas | **Alta** | Prioriza possíveis filhos, pais e cônjuges ausentes e apresenta a fonte correspondente |
| Transparência da fonte | **Boa** | O cartão leva ao registro, à imagem original e ao Source Linker |
| Transparência do raciocínio | **Média** | Mostra a relação sugerida, mas não exibiu score ou critérios detalhados de matching |
| Controle do usuário | **Bom** | Ações de revisão, visualização, ignorar e anexar aparecem antes da alteração |
| Risco de erro genealógico | **Médio a alto** | Indexação automática, homônimos e possíveis inconsistências de datas exigem conferência |
| Cobertura | **Condicionada** | Depende de registros digitalizados, indexados e disponíveis no FamilySearch |
| Maturidade do chat experimental | **Baixa a experimental** | O próprio produto alerta para erros, dados limitados e indisponibilidade |

## Recomendação prática de uso

Recomendo usar o AI Research Assistant como uma **fila priorizada de hipóteses**. Para cada cartão, o pesquisador deve abrir primeiro a fonte, conferir a imagem original, comparar nomes alternativos, datas, locais, idade, cônjuge e filiação, e só depois utilizar o Source Linker. Quando a informação for insuficiente ou contraditória, a ação apropriada é ignorar a pista e registrar mentalmente o motivo da rejeição.

Para as recomendações observadas nesta sessão, eu começaria pelo registro que mostra simultaneamente os pais ou o casal e verificaria a imagem original antes de anexar qualquer relação. Em seguida, conferiria se os dois cartões que apontam para Maria Rita Souza Oliveira realmente se referem ao mesmo núcleo familiar. Não recomendaria anexar automaticamente nenhuma das sugestões apenas com base no nome e na relação exibida.

## Conclusão

O AI Research Assistant do FamilySearch é melhor entendido como um **sistema de descoberta assistida por registros**, não como um genealogista autônomo. Seu valor está em encontrar e organizar pistas que o pesquisador poderia não localizar sozinho. Sua confiabilidade depende da qualidade da indexação, da disponibilidade das fontes e, principalmente, da revisão humana.

A conclusão operacional é simples: **use a IA para encontrar onde olhar; use a fonte original para decidir no que acreditar**. Essa regra é coerente com a própria documentação do FamilySearch, que recomenda verificar as respostas, consultar o documento original quando possível e manter atenção a erros, privacidade, transparência e vieses. [2] [4]

## Referências

[1] [FamilySearch Research Portal](https://www.familysearch.org/en/home/portal/) — página inicial autenticada analisada em 21 de agosto de 2026.

[2] [Introducing Tree Extending Hints from the AI Research Assistant](https://www.familysearch.org/en/blog/ai-research-assistant-home-page-hints) — FamilySearch Blog, 22 de dezembro de 2025.

[3] [FamilySearch AI Help Features](https://www.familysearch.org/en/help/helpcenter/article/familysearch-ai-help-features) — FamilySearch Help Center, 13 de maio de 2026.

[4] [AI Developments in Genealogy and How They Impact You](https://www.familysearch.org/en/blog/ai-developments-genealogy) — FamilySearch Blog, 19 de fevereiro de 2026.

[5] [FamilySearch Privacy Notice](https://www.familysearch.org/en/legal/privacy) — aviso global de privacidade, atualizado em 24 de março de 2026.

[6] [Chat with AI About Your Ancestors](https://www.familysearch.org/en/match/ade/aiassistant/chat) — experiência experimental do FamilySearch Labs, acessada em 21 de agosto de 2026.

[7] [Anna Joaquina Paulina de Souza — Brasil, Rio Grande do Sul, Registro Civil, 1810–2022](https://www.familysearch.org/ark:/61903/1:1:XSFM-LTH1?aihint=&lang=en) — registro consultado a partir de uma recomendação do AI Research Assistant.
