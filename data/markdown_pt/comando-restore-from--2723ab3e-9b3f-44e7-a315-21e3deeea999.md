# Comando RESTORE FROM

Recupera variáveis e matrizes de variáveis salvas em um arquivo de variáveis ou em um campo memo e as coloca na memória.

```foxpro
RESTORE FROM FileName | MEMO MemoFieldName   [ADDITIVE]
```

#### Parâmetros
 **FileName**
Especifica o arquivo de variáveis do qual as variáveis e matrizes são restauradas. Arquivos de variáveis recebem a extensão .mem.
**MEMO MemoFieldName**
Especifica o campo memo do qual as variáveis e matrizes são restauradas.
**ADDITIVE**
Impede que variáveis ou matrizes atualmente na memória sejam apagadas. Se o número de variáveis ou matrizes adicionadas com ADDITIVE, somado ao número das existentes, exceder o limite de variáveis, o Microsoft Visual FoxPro coloca na memória o máximo possível de variáveis e matrizes do arquivo de variáveis ou campo memo. Se você restaurar uma variável ou matriz com o mesmo nome de uma existente, o valor existente será substituído pelo valor restaurado.

# Observações

Quando RESTORE FROM é executado em um programa, todas as variáveis e matrizes PUBLIC e PRIVATE são restauradas como PRIVATE; todas as variáveis e matrizes LOCAL são restauradas como LOCAL. Se RESTORE for executado na janela Command, variáveis e matrizes PUBLIC e PRIVATE serão restauradas como PUBLIC; variáveis e matrizes LOCAL serão restauradas como LOCAL.

RESTORE FROM limpa quaisquer variáveis ou matrizes atualmente na memória, a menos que você inclua a palavra-chave ADDITIVE. RESTORE FROM não afeta variáveis do sistema.

Observe que variáveis do tipo objeto não podem ser restauradas de um arquivo de variáveis ou campo memo.

# Exemplo

No exemplo a seguir, duas variáveis são criadas. Elas são salvas em um arquivo de variáveis e restauradas sem limpar as variáveis existentes.

```foxpro
gnVal1 = 50
gcVal2 = 'Hello'
SAVE TO temp
CLEAR MEMORY
gdVal3 = DATE()
RESTORE FROM temp ADDITIVE
CLEAR
DISPLAY MEMORY LIKE g*
```
