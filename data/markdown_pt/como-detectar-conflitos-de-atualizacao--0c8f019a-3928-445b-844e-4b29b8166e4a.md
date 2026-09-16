# Como: detectar conflitos de atualização

Durante operações de atualização de dados, especialmente em ambientes compartilhados, talvez você queira determinar quais campos foram alterados ou quais são os valores originais ou atuais dos campos alterados. O buffer do Visual FoxPro e as funções GETFLDSTATE( ), GETNEXTMODIFIED( ), OLDVAL( ) e CURVAL( ) permitem determinar qual campo mudou, localizar os dados alterados e comparar os valores atuais, originais e editados para decidir como tratar um erro ou conflito.

### Para detectar uma alteração em um campo
- Após uma operação de atualização, use a função GETFLDSTATE( ).

GETFLDSTATE( ) funciona com dados sem buffer; contudo, é ainda mais eficaz quando o buffer de registros está habilitado. Por exemplo, use GETFLDSTATE( ) no código de um botão Skip em um formulário. Quando você move o ponteiro de registro, o Visual FoxPro verifica o estado de todos os campos do registro, como no exemplo a seguir:

```foxpro
lModified = .F.
FOR nFieldNum = 1 TO FCOUNT() && Check all fields
   if GETFLDSTATE(nFieldNum) = 2  && Modified
      lModified = .T.
      EXIT && Insert update/Save routine here.
   ENDIF && See the next example
ENDFOR
```

### Para detectar e localizar um registro alterado em dados com buffer
- Use a função GETNEXTMODIFIED( ).

GETNEXTMODIFIED( ), com zero como parâmetro, localiza o primeiro registro modificado. Se outro usuário alterar a tabela com buffer, quaisquer alterações encontradas por um comando TABLEUPDATE( ) no seu buffer causarão conflitos. Você pode avaliar os valores conflitantes e resolvê-los usando as funções CURVAL( ), OLDVAL( ) e MESSAGEBOX( ). CURVAL( ) retorna o valor atual do registro no disco, enquanto OLDVAL( ) retorna o valor do registro no momento em que foi armazenado no buffer.

### Para determinar o valor original de um campo com buffer
- Use a função OLDVAL( ).

OLDVAL( ) retorna o valor de um campo com buffer.

### Para determinar o valor atual no disco de um campo com buffer
- Use a função CURVAL( ).

CURVAL( ) retorna o valor atual no disco de um campo com buffer antes da execução de qualquer edição.

Você pode criar um procedimento de tratamento de erros que compare os valores atual e original, permitindo decidir se confirma a alteração atual ou aceita uma alteração anterior nos dados de um ambiente compartilhado.

O exemplo a seguir usa GETNEXTMODIFIED( ), CURVAL( ) e OLDVAL( ) para oferecer ao usuário uma escolha fundamentada durante uma operação de atualização. O exemplo continua a partir da detecção do primeiro registro modificado e pode estar contido em um botão Update ou Save de um formulário.
Código do evento Click para um botão Update ou Save
| Código | Comentário |
| --- | --- |
| nCurRec = GETNEXTMODIFIED(nCurRec) DO WHILE nCurRec <> 0 GO nCurRec RLOCK( ) | Percorra o buffer. Bloqueie o registro modificado. |
| FOR nField = 1 TO FCOUNT(cAlias) cField = FIELD(nField) IF OLDVAL(cField) <> CURVAL(cField) nResult = MESSAGEBOX("Data was ; changed by another user. ; Keep changes?", 4+48+0, ; "Modified Record") | Procure um conflito. Compare o valor original com o valor atual no disco e pergunte ao usuário o que fazer com o conflito. |
| IF nResult = 7 TABLEREVERT(.F.) UNLOCK RECORD nCurRec ENDIF ENDIF ENDFOR nCurRec = GETNEXTMODIFIED(nCurRec) ENDDO | Se o usuário selecionar "No", reverta esse registro e remova o bloqueio. Localize o próximo registro modificado. |
| TABLEUPDATE(.T., .T.) | Force a atualização de todos os registros. |

Você pode usar a propriedade CompareMemo para controlar quando campos memo são usados na detecção de conflitos de atualização. Essa propriedade de exibição e cursor determina se campos memo (tipos M ou G) são incluídos na cláusula WHERE de atualização. A configuração padrão, True (.T.), significa que os campos memo são incluídos na cláusula WHERE. Se você definir a propriedade como False (.F), os campos memo não participarão da cláusula WHERE, independentemente das configurações de UpdateType.

A detecção otimista de conflitos em campos Memo é desativada quando CompareMemo está definida como False. Para detectar conflitos em valores memo, defina CompareMemo como True (.T.).
