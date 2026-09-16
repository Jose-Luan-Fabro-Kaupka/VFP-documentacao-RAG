# Exemplo Permitir que usuários escolham valores de lista

Arquivo: ...\Samples\Solution\Forms\Datalook.scx

Este exemplo ilustra como fornecer aos usuários um conjunto de valores, selecionados de outra tabela, em uma list box e em uma combo box. O valor escolhido pelo usuário é armazenado na tabela atual.

Muitas vezes é mais conveniente para o usuário escolher de uma lista de valores predeterminados e, é claro, você minimiza o risco de o usuário digitar incorretamente um valor. Definir algumas propriedades da list box é tudo o que é necessário para fornecer essa capacidade. Por exemplo, as seguintes propriedades foram definidas para cboEmp_id na página Using Combo Box:

| Propriedade | Configuração |
| --- | --- |
| BoundColumn | 2 |
| ColumnCount | 2 |
| ControlSource | orders.emp_id |
| RowSource | SELECT DISTINCT ALLTRIM( employee.first_name) + " " + ALLTRIM( employee.last_name) , EMP_ID FROM employee INTO CURSOR cEmpCombo ORDER BY first_name |
| RowSourceType | 3 – SQL Statement |

Em vez de fazer o usuário escolher um número de identificação de funcionário na lista suspensa, a instrução SELECT permite mostrar ao usuário os nomes e sobrenomes dos funcionários.

Como a instrução SELECT cria um cursor, o código no evento Destroy fecha o cursor.

```foxpro
IF USED("cEmpCombo") THEN
   USE IN cEmpCombo
ENDIF
```
