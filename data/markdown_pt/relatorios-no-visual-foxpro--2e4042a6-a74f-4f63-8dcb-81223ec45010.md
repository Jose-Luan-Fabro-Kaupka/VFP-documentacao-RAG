# Relatórios no Visual FoxPro

Você pode usar relatórios para organizar e exibir dados de tabelas em um banco de dados ou aplicativo em um arquivo separado. Por exemplo, você pode criar relatórios simples, como uma lista de endereços de clientes, ou relatórios mais complexos e específicos, como uma fatura. Relatórios simples podem ser baseados em uma única tabela, enquanto relatórios mais complexos podem ser baseados em várias tabelas. Você também pode criar tipos especiais de relatórios, como etiquetas. Etiquetas são relatórios de várias colunas que têm configurações de coluna específicas projetadas para papel de etiqueta.

As seções a seguir contêm mais informações sobre relatórios no Visual FoxPro:
 - Arquivos de layout de relatório
- Tipos de layout de relatório

# Arquivos de layout de relatório

Um arquivo de layout de relatório (.frx) é uma tabela Visual FoxPro que armazena as especificações para exibir dados em um relatório. Cada arquivo de relatório tem um arquivo memo de relatório (.frt) associado. O arquivo .frx especifica campos de fontes de dados, texto e a organização dos dados que você deseja exibir na página do relatório. Um arquivo de layout de etiqueta (.lbx) armazena as especificações para exibir dados em formato de etiqueta. Cada arquivo de layout de etiqueta também tem um arquivo memo de etiqueta (.lbt) associado. Arquivos de layout de relatório e etiqueta têm estruturas de tabela idênticas.

O arquivo de layout não armazena valores dos campos de dados, apenas a organização e o formato dos dados para um relatório ou etiqueta específico. Portanto, dependendo das alterações que possam ter ocorrido nos campos da fonte de dados, os valores no relatório podem mudar cada vez que você executa o relatório ou etiqueta.

# Tipos de layout de relatório

Antes de criar um relatório, considere o layout geral que deseja para o relatório. A tabela a seguir lista descrições de layouts gerais, usos comuns e exemplos.

| Tipo de layout | Descrição | Exemplos |
| --- | --- | --- |
| Formulário | Exibe cada registro com campos colocados verticalmente ao longo da lateral. | Listas Cartas-formulário |
| Coluna | Exibe cada registro em uma linha, com campos organizados horizontalmente na página. | Relatório Group/Total* Relatórios financeiros Inventário Resumo de vendas |
| Várias colunas | Contém mais de uma coluna de registros. Os registros se repetem verticalmente nas linhas da coluna mais à esquerda e depois continuam na próxima coluna. | Lista telefônica Texto estilo jornal |
| Um-para-muitos* | Contém um registro ou um relacionamento um-para-muitos. | Faturas Extratos de conta |
| Etiqueta* | Contém mais de uma coluna de registros. Os registros se repetem horizontalmente nas colunas e depois continuam na próxima linha. | Etiquetas de correspondência* Etiquetas de nome Cartões de visita |

* Layouts que têm um assistente de relatório associado.
