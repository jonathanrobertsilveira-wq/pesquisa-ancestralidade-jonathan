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

# The ranking is documentary priority, not a probability of nationality.
# The 2026-08-22 authenticated round downgraded tree-only German attributes
# and elevated the Schell cluster only where a Brazilian parish entry states
# that a Carlos Schell was "da Allemanha" and continuity with Regina is strong.
candidates = [
    Candidato('A37','Joh Tobias Schell','ascendente Schell atribuído, elo ainda não fechado','Batismo alemão direto em 04/04/1763; pais Georg Schell e Anna Barbara Schell; perfil o liga a Johann Nicolaus','alto para localizar registros alemães e comprovar a cadeia até o Brasil','FamilySearch índice alemão QPF7-BFF6 com coleção e páginas 95–96','Joh Tobias → Johann Nicolaus → Karl/Carlos → Regina ainda não demonstrado por atos independentes',5,5,2,5,1),
    Candidato('A23','Karl / Carlos Schell','ascendente de A09','Batismos de Maria (1871) e Regina (1874) show Carlos Schell + Anna Becker; the 1871 page says he was da Allemanha','alto para localizar casamento, filiação e eventual registro alemão','batismos brasileiros autenticados + perfil FamilySearch','atributo Oberbrombach/1843 ainda não tem fonte alemã direta; fonte portuguesa de 1941 é homônimo',5,5,4,4,1),
    Candidato('A13','Carlos Schell','ascendente colateral em investigação','Assento paroquial de 1871 declara Carlos Schell da Allemanha; possível continuidade com o Carlos ligado a Regina e ao ramo Schell','alto, se a continuidade do casal for comprovada','imagem/transcrição paroquial brasileira 1871 + APERS a conferir','Beler/Becker e papel de Carlos em APERS ainda precisam de prova contínua',4,5,3,4,2),
    Candidato('A09','Regina Shell Becker','próxima da direta','Batismo original de 1874 confirma pais Carlos Schell e Anna Becker; pai é possivelmente o Carlos declarado da Allemanha em 1871','alto para fechar pais, avós e cadeia documental, baixo para nascimento próprio na Alemanha','batismo autenticado 1874 + perfis de descendentes','a declaração de Alemanha é do pai, não de Regina; continuidade 1871–1874 ainda deve ser demonstrada',2,5,4,4,1),
    Candidato('A11','Rosalina Schell, 16/12/1906','descendente útil','APERS confirma filiação e avós; pode fechar a ponte brasileira para Carlos/Anna, mas é nascida no Brasil','alto para rastrear ascendentes, baixo para registro alemão próprio','APERS e certidão brasileira','papel de Carlos/Anna no assento ainda requer leitura e não deve ser fundido com Rosalina 1897',1,5,4,4,1),
    Candidato('A12','Regino Schell','ascendente de A11','Pai confirmado de Rosalina 1906; pode conectar o ramo Schell a registros mais antigos','médio-alto até localizar casamento, nascimento e naturalidade','APERS e certidão brasileira','sem cidade, data completa ou fonte migratória; conexão ao Carlos de 1871 não demonstrada',2,4,4,3,1),
    Candidato('A08','Clara Klaus / Clara Hlausf','direta em potencial','Perfil diz Alemanha em 1821, mas fontes visíveis são brasileiras; filiação Johann Klaus/Marina Gesner não localizada na Alemanha','alto para localizar casamento e batismo do casal com A01','perfil/índices brasileiros e buscas autenticadas negativas','muitas variantes, ausência de fonte alemã direta e homônimos',2,5,5,2,2),
    Candidato('A01','João Adão Thomas / Thomaz','direta em potencial','Perfil diz Alemanha em 1815, porém fonte de 1908 com Allemanha é José/Felippe Steir e não A01','alto para casamento/óbito/batismo, mas a origem alemã está não demonstrada','perfil, registros brasileiros e busca autenticada negativa','homônimos de 1852/1908 e atributo alemão sem fonte direta auditada',2,5,5,2,3),
    Candidato('A03','João Thomas / Thomaz','direta em potencial','Filho atribuído de A01/A08; pode fechar ponte entre o casal e Felippe, não há origem alemã própria','médio para documentos dos pais, baixo para nascimento próprio na Alemanha','perfil/árvore e registros de irmãos','nascimento e filiação do próprio alvo sem assento; ligação alternativa não unificada',2,4,5,2,2),
    Candidato('A06','Felippe Thomaz / Thomás','direta em potencial','Núcleo brasileiro; registros de 1901/1949 declaram Felippe e Regina naturais deste Estado','médio para fechar gerações, baixo para registro próprio na Alemanha','registros civis brasileiros autenticados e perfil derivado','idade/paternidade conflitam e nenhuma naturalidade europeia foi localizada',1,3,5,3,2),
    Candidato('A24','Anna Becker','mãe de A09','No assento de 1871, a esposa de Carlos é indicada como “ella desta”; batismo de Regina confirma Anna Becker','médio para localizar casamento e família local, não para origem alemã','batismos brasileiros autenticados + perfil FamilySearch','Beler/Becker é variação a conferir; não há indicação de nascimento na Alemanha',1,4,3,4,1),
    Candidato('A14','Anna Schell','ascendente colateral em investigação','Nome aparece em material APERS ligado ao ramo Schell; a mãe de Regina é Anna Becker, possível conexão ainda não provada','médio para localizar atos colaterais','APERS a interpretar + registros paroquiais','nome/papel exatos precisam de imagem e podem ser homônimos',1,4,3,3,2),
    Candidato('A04','João Thomas / Joao Thom','ascendente atribuído','Casamento atribuído em 1815 na Alemanha, mas nascimento tem 0 fontes e não há cidade','médio teórico; baixa sustentação atual','atributo de árvore','nenhum documento alemão ou brasileiro direto identificado',2,4,3,1,3),
    Candidato('A05','Barbara Miller','ascendente atribuído','Casamento atribuído em 1815 na Alemanha; única fonte é batismo brasileiro de 1857 de outra geração','médio teórico; baixa sustentação atual','atributo de árvore + fonte brasileira não pertinente','nenhum nascimento/casamento alemão e fonte única não sustenta o atributo',2,4,3,1,3),
    Candidato('A02','João Adão indexado como Romale el Verprica Therana','possível homônimo','Ficha de 1908 informa Allemanha','médio, mas depende da identificação do homem','ficha FamilySearch de 1908','nome corrompido e incompatível com óbito de A01 em 1891',5,4,1,2,5),
    Candidato('A10','Rosalina Schell de Souza, perfil 1899–1993','direta em potencial','Pais atribuídos Felippe/Regina; perfil público','baixo para registro alemão próprio','perfil derivado e APERS conflitante','conflito de datas/identidade com Rosalina 1906',1,3,4,2,5),
    Candidato('A15','Rosalina Schell, 16/12/1897','colateral próximo','APERS confirma maternidade/território','baixo para registro alemão próprio','APERS','distinta provisória da Rosalina 1906',1,3,3,4,3),
    Candidato('A16','Alvina Schell','colateral próximo','Filha de Rosalina 1897','baixo para registro alemão próprio','APERS','sem pais além da mãe',1,2,2,3,2),
    Candidato('A17','Celanira Schell','colateral próximo','Filha de Rosalina 1897','baixo para registro alemão próprio','APERS','sem pais além da mãe',1,2,2,3,2),
    Candidato('A18','Rosalina Trott / Schell','colateral','Nascida c.1892 no eixo Gramado–Igrejinha','baixo para registro alemão próprio','FamilySearch/MyHeritage derivado','homônima de Rosalinas Schell de Tapes',2,3,2,2,3),
    Candidato('A19','Theodor Schell','colateral','Cluster Schell/Trott, nascimento c.1888','baixo-médio','perfil secundário','sem filiação primária',2,3,2,2,2),
    Candidato('A20','Helka Schell','colateral','Nascimento 1913 em Igrejinha; pais Theodor/Rosalina','baixo para registro alemão próprio','perfil sem fontes','provável nascida no Brasil',1,2,2,1,1),
    Candidato('A21','Catharina Laurinda Trott / Schell','colateral','Nascimento 1890 em Gramado; pais Trott/Fillmann','baixo para registro alemão próprio','perfil com registros civis brasileiros','provável nascida no Brasil',2,3,2,2,1),
    Candidato('A22','Albin Schell','colateral','Nascimento 1886 em Três Coroas; pais Karl/Anna','baixo para registro alemão próprio','perfil com registros civis brasileiros','provável nascido no Brasil',2,3,2,2,1),
    Candidato('A25','Jacob Friedrich Trott','colateral','Pai atribuído de Catharina; nome germânico','médio teórico, sem fonte','perfil secundário','sem local de nascimento',2,3,2,1,2),
    Candidato('A26','Emilie Fillmann','colateral','Mãe atribuída de Catharina; família Fillmann regional','médio teórico, sem fonte','perfil secundário','sem local de nascimento',2,3,2,1,2),
    Candidato('A07','Margarida Thomas / Thomaz','direta em potencial','Cônjuge atribuída de João Thomas','baixo','árvore e Hemeroteca homônima','sem assento e ocorrência de 1906 não identificada',1,2,3,1,3),
    Candidato('A27','Gertrudes Thomas','colateral da linha Thomas','Filha de João Adão e Clara; casamento em 1874','baixo para origem própria; alto valor de desambiguação','fonte secundária + batismo indexado','origem alemã do marido Hillesheim não é dela',1,3,3,2,1),
    Candidato('A28','Frieda Hoff','colateral incerto','Pista derivada de irmãos Thomaz','baixo','MyHeritage derivado','sem imagem e sem conexão fechada',1,2,1,1,4),
    Candidato('A29','Adolpho Thomaz','colateral incerto','Pista de nome no cluster Thomaz','baixo','índices derivados','homônimos e relação não fechada',1,2,1,1,4),
    Candidato('A30','Carolina Thomaz','colateral incerto','Pista de casamento com Emilio Schelle','baixo','MyHeritage derivado','sem fonte primária',1,2,1,1,4),
    Candidato('A31','Wilbald Thomaz','colateral incerto','Nome raro no cluster Thomaz','baixo','MyHeritage derivado','sem fonte primária',1,2,1,1,4),
    Candidato('A32','Emilio Schelle','colateral incerto','Cônjuge atribuído de Carolina Thomaz','baixo','MyHeritage derivado','sem fonte primária',1,2,1,1,4),
    Candidato('A33','Flauliano Brasil Kenes','ramo paralelo','Sobrenome raro; casamento atribuído em 1948','baixo; passageiro Kenes encontrado é húngaro e distinto','árvore + Bremen para homônimo distinto','nome e eventos brasileiros não localizados',1,3,2,1,3),
    Candidato('A34','Eva Silveira','ramo paralelo','Cônjuge atribuída de Flauliano','muito baixo','árvore derivada','sem indício alemão individual',1,1,1,1,2),
    Candidato('A35','Manoel Geraldo Kenes','ramo paralelo','Casamento atribuído em 1948','baixo','árvore derivada','sem evento primário localizado',1,2,1,1,3),
    Candidato('A36','Dorvalina Ferreira Kenes','ramo paralelo','Cônjuge atribuída de Manoel Geraldo','muito baixo','árvore derivada','sem indício alemão individual',1,1,1,1,2),
]

root = Path(__file__).resolve().parents[1]
out = root / 'docs' / '30_classificacao_candidatos_germanicos_2026-08-22.csv'
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
