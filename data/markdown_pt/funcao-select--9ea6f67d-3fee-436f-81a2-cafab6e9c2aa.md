# Função SELECT( )

Retorna o número da área de trabalho atualmente selecionada ou o número da área de trabalho não utilizada com o número mais alto.

```foxpro
SELECT([ 0 | 1 | cTableAlias ])
```

#### Parâmetros
 **0**
Especifica que SELECT( ) retorne o número da área de trabalho atual.
**1**
Especifica que SELECT( ) retorne o número da área de trabalho não utilizada com o número mais alto.
**cTableAlias**
Especifica o alias da tabela para a qual SELECT( ) retorna a área de trabalho.

# Valor de retorno

Numérico

# Observações

SELECT( ) retorna o número da área de trabalho atual se SET COMPATIBLE estiver definido como OFF. Se SET COMPATIBLE estiver definido como ON, SELECT( ) retorna o número da área de trabalho não utilizada com o número mais alto.

Uma área de trabalho pode ser selecionada (ativada) com SELECT.

# Exemplo

```foxpro
CLOSE DATABASES
SET COMPATIBLE ON
OPEN DATABASE (HOME(2) + 'data\testdata')
SELECT 0  && Unused work area
USE customer  && Opens Customer table
SELECT 0  && Unused work area
USE orders  && Opens Orders table
CLEAR
? SELECT()  && Returns 3, lowest available work area
```
