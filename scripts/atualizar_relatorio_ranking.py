from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
csv_path = root / "docs/30_classificacao_candidatos_germanicos_2026-08-22.csv"
report_path = root / "docs/33_relatorio_consolidado_candidatos_germanicos_2026-08-22.md"

with csv_path.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter=";"))

lines = [
    "## 3. Ranking completo dos 37 candidatos — versão recalculada após a rodada autenticada",
    "",
    "A tabela abaixo substitui a ordem anterior. O campo “prioridade ordinal” é uma prioridade de pesquisa documental e não uma probabilidade de nacionalidade; os scores não são probabilidades.",
    "",
    "| Rank | Código | Pessoa | Relação | Score ordinal | Nível | Indício e ressalva |",
    "|---:|---|---|---|---:|---|---|",
]
for row in rows:
    ind = row["indicio"].replace("|", "/")
    conflict = row["conflito"].replace("|", "/")
    lines.append(f"| {row['rank']} | {row['codigo']} | **{row['nome']}** | {row['linha']} | {row['score_prioridade_total']} | {row['nivel_qualitativo']} | {ind}. **Ressalva:** {conflict}. |")
lines += [
    "",
    "O arquivo CSV `30_classificacao_candidatos_germanicos_2026-08-22.csv` contém os cinco componentes do score e a nota metodológica completa para cada candidato.",
    "",
]
new_section = "\n".join(lines)
text = report_path.read_text(encoding="utf-8")
start = text.index("## 3. Ranking completo dos 37 candidatos")
end = text.index("## 4. Matriz de pesquisas executadas")
text = text[:start] + new_section + text[end:]
text = text.replace("com 84 linhas e os campos", "com 94 linhas de dados e os campos")
text = text.replace("Matriz detalhada das 84 consultas/ações documentadas.", "Matriz detalhada das 94 consultas/ações documentadas.")

if "### 4.2 Achados autenticados da rodada Schell" not in text:
    marker = "## 5. O que foi pesquisado por tipo de fonte"
    addendum = """### 4.2 Achados autenticados da rodada Schell

A evidência mais forte localizada nesta continuação está no ramo Schell. O registro indexado `XJ1K-XPV` informa Maria Schell, nascida em 03/05/1870 e batizada em 10/01/1871 em Santa Cristina, filha de Carlos Schell e Anna Becker. A página original do mesmo evento (`3:1:939N-7CRZ-S`, imagem 159/206) contém a declaração “elle da Allemanha e ella desta”. Em seguida, o assento original de Regina (`3:1:939N-7CR3-Y`, imagem 52/110) confirma Regina nascida em 23/04/1874 e filha legítima de Carlos Schell e Anna Becker, na Capela de Santa Rosa, mesma paróquia.

A sequência 1871–1874 torna fortemente indicada a continuidade do casal e faz de Carlos Schell o principal candidato a primeira geração alemã documentada do cluster. Ainda não é correto declarar que Karl Schell ou Regina nasceram na Alemanha: o assento de 1871 declara a naturalidade de Carlos, enquanto o de 1874 não o faz; a grafia `Beler` no primeiro e `Becker` no segundo precisa de conferência paleográfica. O perfil de Karl atribui nascimento em Oberbrombach em 1843, mas a fonte portuguesa com “Alemanha” anexada ao nascimento é, na realidade, um registro de 1941 de Carlos Sobell S., Ana Schall e Olegina Schell, homônimo distinto.

Para Johann Nicolaus Schell, pai atribuído de Karl, o perfil mostra Oberbrombach em 1812 e imigração após 27/03/1856, mas a única fonte de nascimento é um fólio `Kirchenbuch` sem índice no filme 008162686, imagem 628. A imagem foi preservada apenas como miniatura pública e não foi lida de modo confiável; a geração 1812–1843 permanece hipótese plausível, não comprovação.

"""
    text = text.replace(marker, addendum + marker, 1)
report_path.write_text(text, encoding="utf-8")
print(f"Relatório atualizado com {len(rows)} linhas de ranking e adendo autenticado.")
