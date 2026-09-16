# Comando SAVE MACROS

Salva um conjunto de macros de teclado em um arquivo de macro de teclado ou em um campo memo.

```foxpro
SAVE MACROS TO FileName | TO MEMO MemoFieldName
```

#### Parâmetros
 **TO FileName**
Especifica o arquivo no qual as macros são salvas. Nomes de arquivo de macro de teclado podem conter no máximo oito caracteres e devem começar com uma letra ou sublinhado; não podem começar com um número. Os caracteres subsequentes podem ser qualquer combinação de letras, números e sublinhados. O arquivo recebe a extensão .fky. Se você atribuir uma extensão diferente de .fky, deve incluir essa extensão em RESTORE MACROS.
**TO MEMO MemoFieldName**
Especifica o campo memo no qual as macros são salvas. A tabela que contém o campo memo deve estar aberta; no entanto, não precisa estar na área de trabalho selecionada. Para salvar macros em uma tabela em outra área de trabalho, inclua o alias da tabela ao especificar o campo memo.

# Observações

Ao sair do Visual FoxPro, as macros que você criou são perdidas, a menos que use SAVE MACROS para armazená-las em um arquivo de macro de teclado ou em um campo memo.

# Exemplo

O exemplo a seguir salva o conjunto atual de macros em um arquivo chamado Mymacros.fky.

```foxpro
SAVE MACROS TO mymacros
```
