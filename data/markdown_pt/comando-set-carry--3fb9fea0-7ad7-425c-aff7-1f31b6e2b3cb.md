# Comando SET CARRY

Determina se o Visual FoxPro transporta dados do registro atual para um novo registro criado com INSERT, APPEND e BROWSE.

```foxpro
SET CARRY ON | OFF
-or-
SET CARRY TO [FieldList [ADDITIVE]]
```

#### Parâmetros
 **ON**
Transporta dados de todos os campos em todas as áreas de trabalho do registro atual para um novo registro.
**OFF**
(Padrão) Impede que dados de todos os campos sejam passados para um novo registro.
**TO [ FieldList [ADDITIVE]]**
FieldList especifica os campos dos quais os dados são transportados. Separe os nomes dos campos com vírgulas. ADDITIVE especifica que os campos na lista de campos sejam adicionados ao conjunto atual de campos sendo transportados. Emitir SET CARRY TO executa implicitamente SET CARRY ON. Use SET CARRY TO sem FieldList para restaurar a configuração padrão (todos os campos são transportados).

# Observações

Use SET CARRY para habilitar que dados sejam transportados do registro atual para um novo registro ou para impedir que dados sejam transportados. Campos que geralmente permanecem inalterados durante uma sessão de edição podem ser transportados para cada novo registro. Por exemplo, um campo contendo a data atual pode ser transportado para cada novo registro para que uma nova data não precise ser inserida novamente. Observe que o conteúdo de campos do tipo Memo e General não é transportado.

Modificar a estrutura de uma tabela com um SET CARRY TO <fieldlist> ativo chama um SET CARRY TO implícito. Isso resulta na lista de campos contendo todos os campos da tabela. Se você modificar a estrutura de uma tabela, deve emitir novamente SET CARRY TO <fieldlist> para redefinir a lista de campos.

SET CARRY afeta apenas a tabela aberta na área de trabalho atualmente selecionada.

SET CARRY tem escopo na sessão de dados atual.
