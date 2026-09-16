# Amostra Sort or Order a Table at Run Time

Arquivo: ...\Samples\Solution\Db\Order.scx

Esta amostra ilustra a alteração da ordem em que os registros em uma tabela são listados. A tabela customer tem tags de índice nos campos exibidos na grade. No evento MouseUp de cada um dos cabeçalhos da grade, a ordem da tabela é definida para a tag de índice associada ao campo exibido na coluna. Por exemplo, o código a seguir está associado ao evento MouseUp do cabeçalho Company:

```foxpro
LPARAMETERS nButton, nShift, nXCoord, nYCoord
IF nShift = 2 && CTRL
   SET ORDER TO Company DESCENDING
ELSE
   SET ORDER TO Company ASCENDING
ENDIF
GO TOP
THISFORM.Refresh
```
