# Comando SET FIELDS

Especifica quais campos de uma tabela podem ser acessados. Há duas versões da sintaxe.

```foxpro
SET FIELDS ON | OFF | LOCAL | GLOBAL
```

```foxpro
SET FIELDS TO [[FieldName1 [, FieldName2 ...]]
    | ALL [LIKE Skeleton | EXCEPT Skeleton]]
```

#### Parâmetros
 **ON**
Especifica que somente os campos da lista de campos podem ser acessados.
**OFF**
(Padrão) Especifica que todos os campos da tabela atual podem ser acessados.
**LOCAL**
Especifica que somente os campos da área de trabalho atual listados na lista de campos podem ser acessados.
**GLOBAL**
Especifica que todos os campos da lista de campos, inclusive campos de outras áreas de trabalho, podem ser acessados. SET FIELDS GLOBAL permite acessar campos de outras áreas de trabalho sem emitir SET COMPATIBLE TO DB4.
**TO [ FieldName1 [, FieldName2 ...]]**
Especifica os nomes dos campos que podem ser acessados na tabela atual. Você deve incluir um alias com o nome do campo nos seguintes casos: quando o campo está em uma tabela aberta em uma área de trabalho diferente da área de trabalho selecionada no momento; quando os nomes dos campos são iguais em duas ou mais tabelas. Você pode incluir campos de tabelas abertas em outras áreas de trabalho se os campos forem precedidos pelos aliases de suas tabelas. Entretanto, esses campos não poderão ser acessados a menos que você emita SET FIELDS GLOBAL ou SET COMPATIBLE DB4. A lista de campos pode conter instruções para criar campos calculados. Um campo calculado contém dados somente leitura criados com uma expressão. Essa expressão pode assumir qualquer forma, mas deve ser uma expressão válida do FoxPro. Campos calculados não podem ser acessados a menos que você emita SET FIELDS GLOBAL ou SET COMPATIBLE DB4. O formato da instrução usada para criar um campo calculado é: <calculated field name> = <expr> Este exemplo cria um campo calculado chamado LOCATION: CLOSE DATABASES USE customer SET FIELDS TO LOCATION = ALLTRIM(city) + ', ' + state CITY e STATE são os nomes dos campos da tabela selecionada.
**ALL**
Permite acesso a todos os campos da tabela atual.
**ALL LIKE Skeleton | EXCEPT Skeleton**
Você pode acessar campos seletivamente incluindo a cláusula LIKE, a cláusula EXCEPT ou ambas. Se incluir LIKE Skeleton, poderá acessar campos que correspondam a Skeleton. Se incluir EXCEPT Skeleton, poderá acessar todos os campos, exceto os que correspondam a Skeleton. O padrão Skeleton aceita curingas como * e ?. Por exemplo, para acessar campos que começam com as letras A e P, emita: SET FIELDS TO ALL LIKE A*,P* A cláusula LIKE pode ser combinada com a cláusula EXCEPT: SET FIELDS TO ALL LIKE A*,P* EXCEPT PARTNO*

# Observações

SET FIELDS TO é aditivo — emitir SET FIELDS TO com uma lista de campos adiciona os campos especificados aos que estão acessíveis no momento.

Emitir SET FIELDS TO executa implicitamente SET FIELDS ON. Emita SET FIELDS TO sem incluir uma lista de campos nem ALL para remover todos os campos da lista de campos da tabela atual.

SET FIELDS tem escopo na sessão de dados atual.
