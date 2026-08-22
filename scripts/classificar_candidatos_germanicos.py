from dataclasses import dataclass
from pathlib import Path
import csv

@dataclass
class Candidato:
    codigo: str
    nome: str
    linha: str
    indicio: str
    registro: str
    fonte: str
    conflito: str
    # Scores deliberately ordinal, not probabilities.
    german_hint: int
    record_potential: int
    directness: int
    source_quality: int
    homonym_penalty: int

candidates = [
    Candidato('A01','João Adão Thomas / Thomaz','direta em potencial','Perfil diz Alemanha em 1815; núcleo brasileiro e pista Allemanha','alto se a naturalidade do perfil for correta','perfil/índice + registros brasileiros + óbito brasileiro','pai de 1815 e homônimos de 1852/1908',5,5,5,4,2),
    Candidato('A08','Clara Klaus / Clara Hlausf','direta em potencial','Perfil diz Alemanha em 1821; variantes Klaus/Klus/Hlausf','alto se a naturalidade do perfil for correta','perfil/índices de batismo e secundária','variações de grafia e ausência de cidade',5,5,5,3,1),
    Candidato('A02','João Adão indexado como Romale el Verprica Therana','possível homônimo','Ficha de 1908 informa Allemanha','médio, mas depende da identificação do homem','ficha FamilySearch de 1908','nome corrompido e incompatível com óbito de A01 em 1891',5,4,1,2,5),
    Candidato('A03','João Thomas / Thomaz','direta em potencial','Filho atribuído de A01; nascimento c.1845 em Santa Cruz','médio para registro alemão dos pais, baixo para nascimento próprio na Alemanha','perfil/árvore e registros de irmãos','nascimento e filiação do próprio alvo sem assento',3,4,5,2,2),
    Candidato('A04','João Thomas / Joao Thom','ascendente atribuído','Casamento atribuído em 1815 na Alemanha','médio teórico, baixa sustentação atual','atributo de árvore','zero fonte de nascimento e sem cidade',4,4,3,1,2),
    Candidato('A05','Barbara Miller','ascendente atribuído','Casamento atribuído em 1815 na Alemanha','médio teórico, baixa sustentação atual','atributo de árvore','zero/uma fonte não auditada e sem cidade',4,4,3,1,2),
    Candidato('A06','Felippe Thomaz / Thomás','direta em potencial','Filho de João Thomas; família com possível ponte a A01','médio para herança alemã, baixo para registro próprio','registro civil brasileiro indexado e perfil derivado','idade/paternidade conflitam em perfil Guilherme 1853 vs 1864',3,3,5,2,2),
    Candidato('A12','Regino Schell','direta em potencial','Pai confirmado de Rosalina 1906; sobrenome Schell','baixo-médio até localizar naturalidade','APERS e certidão brasileira','sem cidade, data completa ou fonte migratória',3,4,4,3,1),
    Candidato('A10','Rosalina Schell de Souza, perfil 1899–1993','direta em potencial','Pais atribuídos Felippe/Regina; perfil público','baixo para registro alemão próprio','perfil derivado e APERS conflitante','conflito de datas/identidade com Rosalina 1906',2,3,4,2,5),
    Candidato('A11','Rosalina Schell, 16/12/1906','direta em potencial','Certidão APERS confirma filiação e avós Carlos/Anna','baixo para registro alemão próprio; alto para rastrear pais','APERS e certidão','não é imigrante provável por data',2,3,4,4,1),
    Candidato('A13','Carlos Schell','direta em potencial','Nome aparece como ascendência de Rosalina 1906','médio para imigração se geração antiga','APERS','papel e identidade ainda não fechados',3,4,3,3,3),
    Candidato('A14','Anna Schell','direta em potencial','Nome aparece como ascendência de Rosalina 1906','médio para imigração se geração antiga','APERS','nome e papel exatos precisam de imagem',3,4,3,3,3),
    Candidato('A09','Regina Shell Becker','próxima da direta','Filha atribuída de Karl/Anna; mãe de Adolpho e possível Rosalina','baixo-médio','perfis FamilySearch de filhos/irmãos','sem casamento/nascimento original',3,3,4,2,2),
    Candidato('A23','Karl Schell','colateral','Pai atribuído de Albin, Adolf e Johannes','médio para registro de imigração','perfis FamilySearch de três filhos','sem naturalidade europeia',3,4,2,2,1),
    Candidato('A24','Anna Becker','colateral','Mãe atribuída de Albin, Adolf e Johannes','médio para registro de imigração','perfis FamilySearch de três filhos','sem naturalidade europeia',3,4,2,2,1),
    Candidato('A15','Rosalina Schell, 16/12/1897','colateral próximo','APERS confirma maternidade/território','baixo para registro alemão próprio','APERS','distinta provisória da Rosalina 1906',2,3,3,4,3),
    Candidato('A16','Alvina Schell','colateral próximo','Filha de Rosalina 1897','baixo para registro alemão próprio','APERS','sem pais além da mãe',2,2,2,3,2),
    Candidato('A17','Celanira Schell','colateral próximo','Filha de Rosalina 1897','baixo para registro alemão próprio','APERS','sem pais além da mãe',2,2,2,3,2),
    Candidato('A18','Rosalina Trott / Schell','colateral','Nascida c.1892 no eixo Gramado–Igrejinha','baixo para registro alemão próprio','FamilySearch/MyHeritage derivado','homônima de Rosalinas Schell de Tapes',3,3,2,2,3),
    Candidato('A19','Theodor Schell','colateral','Cluster Schell/Trott, nascimento c.1888','baixo-médio','perfil secundário','sem filiação primária',3,3,2,2,2),
    Candidato('A20','Helka Schell','colateral','Nascimento 1913 em Igrejinha; pais Theodor/Rosalina','baixo para registro alemão próprio','perfil sem fontes','provável nascida no Brasil',2,2,2,1,1),
    Candidato('A21','Catharina Laurinda Trott / Schell','colateral','Nascimento 1890 em Gramado; pais Trott/Fillmann','baixo para registro alemão próprio','perfil com registros civis brasileiros','provável nascida no Brasil',3,3,2,2,1),
    Candidato('A22','Albin Schell','colateral','Nascimento 1886 em Três Coroas; pais Karl/Anna','baixo para registro alemão próprio','perfil com registros civis brasileiros','provável nascido no Brasil',3,3,2,2,1),
    Candidato('A25','Jacob Friedrich Trott','colateral','Pai atribuído de Catharina; nome germânico','médio teórico, sem fonte','perfil secundário','sem local de nascimento',3,3,2,1,2),
    Candidato('A26','Emilie Fillmann','colateral','Mãe atribuída de Catharina; família Fillmann regional','médio teórico, sem fonte','perfil secundário','sem local de nascimento',3,3,2,1,2),
    Candidato('A07','Margarida Thomas / Thomaz','direta em potencial','Cônjuge atribuída de João Thomas','baixo','árvore e Hemeroteca homônima','sem assento e ocorrência de 1906 não identificada',2,2,3,1,3),
    Candidato('A27','Gertrudes Thomas','colateral da linha Thomas','Filha de João Adão e Clara; casamento em 1874','baixo para origem própria; alto valor de desambiguação','fonte secundária + batismo indexado','origem alemã do marido Hillesheim não é dela',2,3,3,2,1),
    Candidato('A28','Frieda Hoff','colateral incerto','Pista derivada de irmãos Thomaz','baixo','MyHeritage derivado','sem imagem e sem conexão fechada',2,2,1,1,4),
    Candidato('A29','Adolpho Thomaz','colateral incerto','Pista de nome no cluster Thomaz','baixo','índices derivados','homônimos e relação não fechada',2,2,1,1,4),
    Candidato('A30','Carolina Thomaz','colateral incerto','Pista de casamento com Emilio Schelle','baixo','MyHeritage derivado','sem fonte primária',2,2,1,1,4),
    Candidato('A31','Wilbald Thomaz','colateral incerto','Nome raro no cluster Thomaz','baixo','MyHeritage derivado','sem fonte primária',2,2,1,1,4),
    Candidato('A32','Emilio Schelle','colateral incerto','Cônjuge atribuído de Carolina Thomaz','baixo','MyHeritage derivado','sem fonte primária',2,2,1,1,4),
    Candidato('A33','Flauliano Brasil Kenes','ramo paralelo','Sobrenome raro; casamento atribuído em 1948','baixo; passageiro Kenes encontrado é húngaro e distinto','árvore + Bremen para homônimo distinto','nome e eventos brasileiros não localizados',2,3,2,1,3),
    Candidato('A34','Eva Silveira','ramo paralelo','Cônjuge atribuída de Flauliano','muito baixo','árvore derivada','sem indício alemão individual',1,1,1,1,2),
    Candidato('A35','Manoel Geraldo Kenes','ramo paralelo','Casamento atribuído em 1948','baixo','árvore derivada','sem evento primário localizado',2,2,1,1,3),
    Candidato('A36','Dorvalina Ferreira Kenes','ramo paralelo','Cônjuge atribuída de Manoel Geraldo','muito baixo','árvore derivada','sem indício alemão individual',1,1,1,1,2),
]

out = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan/docs/30_classificacao_candidatos_germanicos_2026-08-22.csv')
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['rank','codigo','nome','linha','score_indicio_alemao','score_potencial_registro','score_prioridade_total','nivel_qualitativo','indicio','fonte','conflito','nota_metodologica'])
    ranked = sorted(candidates, key=lambda c: (c.german_hint + c.record_potential + c.directness + c.source_quality - c.homonym_penalty, c.german_hint + c.record_potential), reverse=True)
    for rank, c in enumerate(ranked, 1):
        total = c.german_hint + c.record_potential + c.directness + c.source_quality - c.homonym_penalty
        if total >= 16:
            level = 'prioridade muito alta'
        elif total >= 12:
            level = 'prioridade alta'
        elif total >= 8:
            level = 'prioridade média'
        else:
            level = 'prioridade baixa'
        w.writerow([rank,c.codigo,c.nome,c.linha,c.german_hint,c.record_potential,total,level,c.indicio,c.fonte,c.conflito,'Score ordinal de pesquisa, não probabilidade estatística nem prova de nacionalidade'])

print(f'Gerados {len(candidates)} candidatos em {out}')
