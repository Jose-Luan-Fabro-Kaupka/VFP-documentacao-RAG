# Como: salvar o ambiente de impressão para relatórios

Você pode salvar com um relatório as configurações atuais do ambiente de impressão. Elas são gravadas nos campos memo apropriados do registro de cabeçalho e mantidas entre sessões.

> **Observação:** No Visual FoxPro 9, o ambiente não é salvo por padrão. Salvá-lo torna a abertura do relatório para design muito mais lenta, especialmente com impressoras remotas.

> **Observação:** Mesmo para um relatório destinado a uma única impressora, muitas vezes é melhor omitir essas configurações do arquivo .frx ou .lbx.

Em tempo de execução, use SET PRINTER TO NAME antes de REPORT FORM ou LABEL. Isso mantém as configurações externas à definição e permite especificá-las para cada relatório.

### Para salvar as configurações do ambiente de impressão
- Abra o relatório ou rótulo no designer apropriado.
- No menu Report, clique em Printer Environment se ainda não estiver selecionado.

Também é possível usar a guia Reports da caixa Options ou a guia Page Setup das propriedades do relatório. SYS(1037) inicializa as configurações da impressora padrão ou do ambiente do relatório.
