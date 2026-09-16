# Comando SELECT

Ativa a área de trabalho especificada.

```foxpro
SELECT nWorkArea | cTableAlias
```

#### Parâmetros
 **nWorkArea**
Especifica uma área de trabalho a ativar. Se nWorkArea for 0, a área de trabalho não utilizada de menor número é ativada.
**cTableAlias**
Especifica uma área de trabalho que contém uma tabela aberta a ativar. cTableAlias é o alias da tabela aberta. Você também pode incluir uma letra de A a J para cTableAlias para ativar uma das dez primeiras áreas de trabalho.

# Observações

Por padrão, a área de trabalho número 1 está ativa quando você inicia o Visual FoxPro.

> **Observação:** Campos em tabelas abertas em qualquer área de trabalho podem ser incluídos em comandos e funções do Visual FoxPro. Use os seguintes formatos para acessar campos em uma tabela aberta em uma área de trabalho diferente da atual: alias . campo ou alias->campo .

# Exemplo

O exemplo a seguir demonstra formas de selecionar áreas de trabalho.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
SELECT 1     && Work area 1
USE customer  && Opens Customer table
SELECT 2     && Work area 2
USE orders  && Opens Orders table
SELECT customer     && Work area 1
BROWSE
SELECT B     && Work area 2
BROWSE
```
