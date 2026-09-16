# Função MEMLINES( )

Retorna o número de linhas em um campo memo.

```foxpro
MEMLINES(MemoFieldName)
```

#### Parâmetros
 **MemoFieldName**
Especifica o nome do campo memo. Se o campo memo estiver em uma tabela que não está aberta na área de trabalho atual, anteceda o nome do campo memo com o alias da tabela e um ponto.

# Valor de retorno

Numeric

# Observações

O número de linhas em um campo memo é determinado pelo valor atual de SET MEMOWIDTH.

# Exemplo

O exemplo a seguir percorre três registros na tabela `employee` e usa MEMLINES( ) para determinar se há dados no campo memo `notes` e quando as quebras de página devem ocorrer. Os dados de `last_name` do registro aparecem, junto com `notes` (se houver dados no campo memo) ou uma mensagem indicando que não há `notes` para esse registro.

```foxpro
CLOSE DATABASES
CLEAR
SET TALK OFF
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee  && Open Employee table
SET MEMOWIDTH TO 65
gnLine = 1
GOTO 2
SCAN NEXT 3
   gnMemoSize = MEMLINES(notes)
   IF gnMemoSize = 0
      STORE .T. TO glNoMemo
      STORE 1 TO gnMemoSize
   ELSE
      STORE .F. TO glNoMemo
   ENDIF
   IF gnLine + gnMemoSize > 65
      EJECT
      gnLine = 1
   ENDIF
   @ gnLine,2 SAY 'Last Name: '+ last_name
   gnLine = gnLine +1
   @ gnLine ,2 SAY 'Notes: '
   ?? IIF(glNoMemo, 'No notes ',notes)
   gnLine = gnLine + gnMemoSize + 2
   IF gnLine > 24
      gnLine = 1
      CLEAR
   ENDIF
ENDSCAN
```
