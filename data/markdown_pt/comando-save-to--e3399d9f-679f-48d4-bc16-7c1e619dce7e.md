# Comando SAVE TO

Armazena variáveis e matrizes atuais em um arquivo de variáveis ou em um campo memo.

> **Observação:** Variáveis do tipo objeto não podem ser salvas em um arquivo de variáveis ou em um campo memo. O comando SAVE TO não suporta o salvamento de matrizes com mais de 65.000 elementos.

```foxpro
SAVE TO FileName | MEMO MemoFieldName
   [ALL LIKE Skeleton | ALL EXCEPT Skeleton]
```

#### Parâmetros
 **FileName**
Especifica o arquivo de variáveis no qual as variáveis e matrizes são salvas. Para um arquivo de variáveis, a extensão de arquivo padrão é .mem.
**MEMO MemoFieldName**
Especifica o campo memo no qual as variáveis e matrizes são salvas.
**ALL LIKE Skeleton**
Especifica que todas as variáveis e matrizes que correspondem ao Skeleton especificado sejam salvas. O skeleton pode incluir os curingas ponto de interrogação (?) e asterisco (*).
**ALL EXCEPT Skeleton**
Especifica que todas as variáveis e matrizes, exceto as que correspondem ao Skeleton especificado, sejam salvas. O skeleton pode incluir os curingas ponto de interrogação (?) e asterisco (*).

# Observações

Para colocar variáveis e matrizes de volta na memória a partir de um arquivo de variáveis ou de um campo memo, use o comando RESTORE FROM. Para obter mais informações, consulte RESTORE FROM Command.

O arquivo de variáveis ou o campo memo é marcado com a página de código atual.

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
