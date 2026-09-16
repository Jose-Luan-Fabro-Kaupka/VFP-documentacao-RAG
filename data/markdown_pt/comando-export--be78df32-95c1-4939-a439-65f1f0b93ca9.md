# Comando EXPORT

Copia dados de uma tabela Visual FoxPro para um arquivo em um formato diferente.

```foxpro
EXPORT TO FileName [TYPE]
   DIF | MOD | SYLK | WK1 | WKS | WR1 | WRK | XLS | XL5
   [FIELDS FieldList] [Scope] [FOR lExpression1] [WHILE lExpression2]
   [NOOPTIMIZE] [AS nCodePage]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo para o qual o Visual FoxPro exporta dados. Se você não incluir uma extensão com o nome do arquivo, a extensão padrão para o tipo de arquivo especificado é atribuída.
**TYPE**
Especifica o tipo de arquivo a ser criado. A palavra-chave TYPE é opcional, mas você deve especificar um dos seguintes tipos de arquivo. Tipo de arquivo Descrição DIF Cada campo de uma tabela Visual FoxPro torna-se um vetor (coluna) e cada registro torna-se uma tupla (linha) em um arquivo DIF (Data Interchange Format), usado pelo VisiCalc. O novo nome de arquivo recebe a extensão .DIF se uma extensão não for incluída em FileName. MOD Use a cláusula MOD para exportar para um arquivo no formato Microsoft Multiplan versão 4.01 MOD. O novo nome de arquivo recebe a extensão .MOD se você não incluir uma extensão em FileName. SYLK Um formato de intercâmbio Symbolic Link (usado pelo Microsoft Multiplan) no qual cada campo de uma tabela Visual FoxPro torna-se uma coluna na planilha e cada registro torna-se uma linha. Por padrão, nomes de arquivo SYLK não têm extensão. WK1 Inclua esta opção para criar uma planilha Lotus 1-2-3 a partir de uma tabela Visual FoxPro. Uma extensão .WK1 é atribuída ao nome do arquivo da planilha para uso com Lotus 1-2-3 revisão 2.x. Cada campo da tabela torna-se uma coluna na nova planilha, e cada registro na tabela torna-se uma linha da planilha. WKS Inclua esta opção para criar uma planilha Lotus 1-2-3 a partir de uma tabela Visual FoxPro. Uma extensão .WKS é atribuída ao nome do arquivo da planilha para uso com Lotus 1-2-3 revisão 1-A. Cada campo da tabela torna-se uma coluna na nova planilha, e cada registro torna-se uma linha na planilha. WR1 Inclua esta opção para criar uma planilha Lotus Symphony a partir de uma tabela Visual FoxPro. Uma extensão .WR1 é atribuída à planilha para uso com Symphony versão 1.01. Cada campo da tabela torna-se uma coluna na nova planilha, e cada registro na tabela torna-se uma linha na planilha. WRK Inclua esta opção para criar uma planilha Lotus Symphony a partir de uma tabela Visual FoxPro. Uma extensão .WRK é atribuída ao nome do arquivo da planilha para uso com Symphony versão 1.10. Cada campo da tabela torna-se uma coluna na nova planilha, e cada registro na tabela torna-se uma linha na planilha. XLS Inclua esta opção para criar uma planilha Microsoft Excel a partir de uma tabela Visual FoxPro. Cada campo na tabela selecionada torna-se uma coluna na planilha, e cada registro da tabela torna-se uma linha. Uma extensão de nome de arquivo .xls é atribuída ao arquivo da planilha recém-criado, a menos que você especifique uma extensão diferente. Você pode exportar no máximo 65.535 linhas, que inclui uma linha reservada para o cabeçalho do campo. XL5 Inclua esta opção para criar um arquivo de planilha Microsoft Excel versão 5.0 a partir de uma tabela Visual FoxPro. Cada campo da tabela selecionada atualmente torna-se uma coluna na planilha e cada registro torna-se uma linha. Uma extensão .xls é atribuída à nova planilha se você não incluir uma extensão de arquivo. Você pode exportar no máximo 65.535 linhas, que inclui uma linha reservada para o cabeçalho do campo.
**FIELDS FieldList**
Especifica quais campos são copiados para o novo arquivo. Se você omitir a cláusula FIELDS, todos os campos são copiados para o novo arquivo. Campos memo e general não são copiados para o novo arquivo, mesmo se seus nomes estiverem incluídos na lista de campos.
**Scope**
Especifica um intervalo de registros a copiar para o novo arquivo. Scope Especifica um intervalo de registros a copiar para o novo arquivo. Apenas os registros que estão no intervalo são copiados para o novo arquivo. As cláusulas de escopo são: ALL, NEXT nRecords, RECORD nRecordNumber e REST. Para obter mais informações sobre cláusulas de escopo, consulte o tópico online Scope Clauses. Comandos que incluem Scope operam apenas na tabela na área de trabalho ativa. O escopo padrão para EXPORT é todos os registros.
**FOR lExpression1**
Especifica que apenas registros que satisfazem a condição lógica lExpression1 são copiados para o novo arquivo. Usar este argumento permite filtrar registros indesejados. A otimização de consulta Rushmore otimiza um comando EXPORT ... FOR lExpression1 se lExpression1 for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.
**WHILE lExpression2**
Especifica uma condição pela qual os registros são copiados para o novo arquivo enquanto a expressão lógica lExpression2 for avaliada como true (.T.).
**NOOPTIMIZE**
Desabilita a otimização de consulta Rushmore de EXPORT. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.
**AS nCodePage**
Especifica a página de código para o arquivo que EXPORT cria. O Visual FoxPro copia o conteúdo da tabela selecionada atualmente e, ao copiar os dados, converte automaticamente os dados para a página de código que você especificar para o novo arquivo. Se possível, o Visual FoxPro marca o arquivo recém-criado com a página de código que você especificar. Se você especificar um valor para nCodePage que não seja suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para o arquivo que o Visual FoxPro cria. Se você omitir AS nCodePage, nenhuma conversão de página de código ocorre. Se possível, o Visual FoxPro marca o arquivo recém-criado com a página de código da tabela da qual os dados são copiados. Se nCodePage for 0, nenhuma conversão de página de código ocorre e o arquivo recém-criado não é marcado com uma página de código.

# Observações

Use EXPORT para usar dados do Visual FoxPro em outros pacotes de software.

Se a tabela da qual você está exportando estiver indexada, o novo arquivo é criado na ordem indexada.
