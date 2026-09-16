# Como: realizar atualizações usando buffers

Depois de escolher o método de buffering e o tipo de bloqueio, você pode habilitar buffering de registro ou de tabela.

### Para habilitar buffering
- Escolha uma das seguintes opções: No Form Designer , defina a propriedade BufferModeOverride do cursor no ambiente de dados do formulário. -OU- Use a função CURSORSETPROP( ) para definir a propriedade Buffering.

Por exemplo, você pode habilitar buffering pessimista de linha colocando o seguinte código na procedure Init de um formulário:

```foxpro
CURSORSETPROP('Buffering', 2)
```

Você então coloca código para as operações de atualização no código de método apropriado para seus controles.

Para gravar edições na tabela original, use a Função TABLEUPDATE( ). Para cancelar edições após uma operação de atualização com falha em uma tabela restrita por regras, use a Função TABLEREVERT( ), que é válida mesmo se o buffering explícito de tabela não estiver habilitado. Para especificar um nível de verificação de integridade de tabela inferior à configuração padrão, você pode usar o Comando SET TABLEVALIDATE.

A amostra a seguir demonstra como atualizar registros quando o buffering pessimista de registro está habilitado.
 Exemplo de atualização usando buffers de registro e tabela
| Código | Comentário |
| --- | --- |
| OPEN DATABASE testdata USE customers CURSORSETPROP('Buffering', 2) | No código Init do formulário, abra a tabela e habilite o buffering pessimista de registro. |
| lModified = .F. FOR nFieldNum = 1 TO FCOUNT() IF GETFLDSTATE(nFieldNum) = 2 lModified = .T. EXIT ENDIF ENDFOR | Percorra os campos, verificando se algum campo foi modificado. Observação Este código pode estar no evento Click de um botão de comando "Save" ou "Update". |
| IF lModified nResult = MESSAGEBOX; ("Record has been modified. Save?", ; 4+32+256, "Data Change") | Localize o próximo registro modificado. |
| IF nResult = 7 TABLEREVERT (.F.) ENDIF ENDIF | Apresente o valor atual e dê ao usuário a opção de reverter a alteração no campo atual. |
| SKIP IF EOF() MESSAGEBOX( "already at bottom") SKIP -1 ENDIF THISFORM.Refresh | SKIP garante que a última alteração seja gravada. |
