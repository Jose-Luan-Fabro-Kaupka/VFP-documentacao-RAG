# Comando RESTORE MACROS

Restaura na memória macros de teclado salvas em um arquivo de macro de teclado ou campo memo.

```foxpro
RESTORE MACROS   [FROM FileName | FROM MEMO MemoFieldName]
```

#### Parâmetros
 **FROM FileName**
Especifica o arquivo de macro do qual as macros são restauradas. Arquivos de macro têm extensão .fky, e essa extensão é assumida se você não especificar uma. Se você atribuiu uma extensão diferente ao arquivo, deve incluir essa extensão em FileName.
**FROM MEMO MemoFieldName**
Especifica o campo memo do qual as macros são restauradas.

# Observações

Use SAVE MACRO para armazenar macros de teclado em um arquivo de macro de teclado ou em um campo memo.

Por padrão, restaurar macros de um arquivo ou campo memo é aditivo — as macros restauradas são anexadas ao conjunto existente de macros na memória. Se um nome de macro no arquivo ou campo memo for o mesmo que um nome de macro existente, a macro no arquivo ou campo memo substitui a macro existente.

Se emitido sem um nome de arquivo ou nome de campo memo, RESTORE MACROS limpa todas as macros da memória e restaura as macros padrão. As macros padrão são restauradas do arquivo de macro de teclado chamado Default.fky. Se Default.fky não puder ser encontrado, o Visual FoxPro restaura as teclas F2 a F9 para as configurações padrão de inicialização do Visual FoxPro.
