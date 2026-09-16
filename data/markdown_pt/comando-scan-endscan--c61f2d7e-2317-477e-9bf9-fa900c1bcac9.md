# Comando SCAN ... ENDSCAN

Move o ponteiro de registro pela tabela selecionada atualmente e executa um bloco de comandos para cada registro que atende às condições especificadas.

```foxpro
SCAN [NOOPTIMIZE] [Scope] [FOR lExpression1] [WHILE lExpression2]
   [Commands]
   [LOOP]
   [EXIT]
ENDSCAN
```

#### Parâmetros
 **NOOPTIMIZE**
Impede a otimização de consulta Rushmore do SCAN. Para obter mais informações, consulte Comando SET OPTIMIZE e Usando otimização de consulta Rushmore para acelerar o acesso a dados .
**Scope**
Especifica um intervalo de registros a serem escaneados. Somente os registros dentro do intervalo são escaneados. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber e REST. Para obter mais informações sobre cláusulas de escopo, consulte o tópico online Cláusulas de escopo. O escopo padrão para SCAN é todos os registros (ALL).
**FOR lExpression1**
Executa comandos somente para registros para os quais lExpression1 é avaliado como true (.T.). Incluir a cláusula FOR permite filtrar registros que você não deseja escanear. Rushmore otimiza uma consulta criada com SCAN ... FOR se lExpression1 é uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte Comando SET OPTIMIZE e Usando otimização de consulta Rushmore para acelerar o acesso a dados .
**WHILE lExpression2**
Especifica uma condição pela qual os comandos são executados enquanto lExpression2 é avaliado como true (.T.).
**Commands**
Especifica os comandos do Visual FoxPro a serem executados.
**LOOP**
Retorna o controle diretamente de volta ao SCAN. LOOP pode ser colocado em qualquer lugar entre SCAN e ENDSCAN.
**EXIT**
Transfere o controle do programa de dentro do loop SCAN ... ENDSCAN para o primeiro comando após ENDSCAN. EXIT pode ser colocado em qualquer lugar entre SCAN e ENDSCAN.
**ENDSCAN**
Indica o final do procedimento SCAN.

# Observações

SCAN avança automaticamente o ponteiro de registro para o próximo registro que atende às condições especificadas e executa o bloco de comandos.

Você pode colocar comentários após ENDSCAN na mesma linha. Os comentários são ignorados durante a compilação e execução do programa.

SCAN ... ENDSCAN garante que, ao alcançar ENDSCAN, o Visual FoxPro selecione novamente a tabela que estava ativa quando o loop SCAN ... ENDSCAN começou.

# Exemplo

O exemplo a seguir usa um loop SCAN ... ENDSCAN para exibir todas as empresas na Suécia.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
SCAN FOR UPPER(country) = 'SWEDEN'
   ? contact, company, city
ENDSCAN
```
