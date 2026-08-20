# Guia de migração da árvore de pesquisa

**Pessoa de referência:** Jonathan Robert Silveira De Souza

**Arquivo-base:** `arvore_pesquisa_jonathan.ged`

**Estado atual:** árvore independente, sem alterações na árvore colaborativa do FamilySearch.

## Conteúdo da versão atual

A árvore foi gerada em GEDCOM 5.5.1, codificação UTF-8, e validada localmente. Ela contém 26 indivíduos, 10 famílias e 15 fontes. As relações estão separadas por níveis de confiança: fatos confirmados por fonte primária, eventos confirmados apenas por índice, hipóteses derivadas da árvore FamilySearch/MyHeritage, conflitos de datas e placeholders não identificados.

O arquivo `pessoas_evidencias.csv` deve ser mantido junto do GEDCOM porque resume o identificador FamilySearch, o status de cada pessoa, datas, fontes e observações. O arquivo `LEIA-ME.md` descreve as regras de confiança e os conflitos. O relatório principal e o diário preservam a justificativa e as buscas negativas; não devem ser descartados após a importação.

## Regras antes da importação

A importação deve ser feita como **árvore privada ou de pesquisa**, nunca como substituição da árvore colaborativa existente. Não se deve aceitar mesclagem automática de pessoas apenas por nome, sobrenome ou ano. Os principais riscos de duplicação são Rosalina Schell, Regino Schell, Alicia Schell e os homônimos Schell de outras localidades.

As datas de Alvino e Rosalina devem ser importadas com uma nota de conflito: a árvore antiga indicava aproximadamente 1891 e 1899, enquanto o processo primário APERS nº 180190 fornece 23/02/1897 e 16/12/1906. A relação Alvino–Rosalina e o casamento de 17/04/1955 estão documentados pelo PDF primário; a filiação de Rosalina a Regino também aparece nesse processo. O nascimento de Rosalvino em 1940 e o casamento de Raimundo/Alicia continuam hipóteses.

## Plataformas candidatas

| Plataforma | Uso recomendado | Cuidados para esta pesquisa |
|---|---|---|
| [Gramps](https://gramps-project.org/) | Cópia local, privada e auditável | Preservar os arquivos Markdown/CSV separadamente; conferir como notas e URLs GEDCOM são importadas |
| [Geneanet](https://www.geneanet.org/) | Árvore online com importação GEDCOM | Configurar privacidade antes de publicar; revisar pessoas vivas e placeholders |
| [MyHeritage](https://www.myheritage.com/) | Árvore online e comparação com a pista já consultada | Não aceitar Smart Matches como prova; revisar duplicações e manter o PDF APERS como fonte primária externa |

A plataforma será escolhida somente depois que Jonathan confirmar se prefere uma cópia local ou uma árvore online. Não foi criada conta nova nem enviada a árvore para terceiros nesta etapa.

## Procedimento recomendado

Primeiro, importar `arvore_pesquisa_jonathan.ged` em um projeto privado. Depois, conferir manualmente Jonathan, seus pais, Rosalvino, Raimundo, Alicia, Alvino, Rosalina e Regino. Em seguida, verificar se cada fonte aparece como URL e se as notas de conflito permanecem legíveis. Por fim, anexar ou guardar separadamente o PDF APERS nº 180190, o CSV de exportação, o relatório principal e o quadro de evidências.

Qualquer sugestão automática de parentesco europeu deve ser mantida como pista até que um documento brasileiro informe explicitamente naturalidade, país de nascimento ou filiação de imigrante. A plataforma posterior deve ser usada para organizar e comparar evidências, não para substituir a leitura das fontes primárias.
