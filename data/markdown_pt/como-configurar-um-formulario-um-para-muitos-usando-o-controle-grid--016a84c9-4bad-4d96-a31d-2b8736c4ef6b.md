# Como: configurar um formulário um-para-muitos usando o controle Grid

Um dos usos mais comuns de uma grade é exibir os registros filhos de uma tabela enquanto caixas de texto exibem os dados dos registros pai. Quando o usuário percorre os registros da tabela pai, a grade exibe os registros filhos correspondentes.

Se o ambiente de dados do formulário inclui uma relação um-para-muitos entre duas tabelas, exibir essa relação no formulário é muito simples.

### Para configurar um formulário um-para-muitos com um ambiente de dados
- Arraste os campos desejados da tabela pai do Designer de Ambiente de Dados para o formulário.
- Arraste a tabela relacionada do Designer de Ambiente de Dados para o formulário.

Na maioria dos casos, convém criar um ambiente de dados para o formulário ou conjunto de formulários. No entanto, criar um formulário um-para-muitos sem usar o Designer de Ambiente de Dados não é muito mais complicado.

### Para configurar um formulário um-para-muitos sem criar um ambiente de dados
- Adicione caixas de texto ao formulário para exibir os campos desejados da tabela primária.
- Defina a propriedade ControlSource das caixas de texto como a tabela primária.
- Adicione uma grade ao formulário.
- Defina RecordSource da grade como o nome da tabela relacionada.
- Defina LinkMaster da grade como o nome da tabela primária.
- Defina ChildOrder da grade como o nome da tag de índice da tabela relacionada que corresponde à expressão relacional da tabela primária.
- Defina RelationalExpr da grade como a expressão que associa a tabela relacionada à tabela primária. Por exemplo, se a tag ChildOrder estiver indexada por "lastname + firstname", defina RelationalExpr com a mesma expressão.

Independentemente da forma usada, você pode adicionar controles de navegação para percorrer a tabela pai e atualizar os objetos do formulário. Por exemplo, o código a seguir pode ser incluído no evento Click de um botão de comando:

```foxpro
SELECT orders && if orders is the parent table
SKIP
IF EOF()
   GO BOTTOM
ENDIF
THISFORM.Refresh
```
