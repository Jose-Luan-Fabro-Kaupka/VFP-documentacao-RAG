# Comando SHOW MENU

Exibe uma ou mais barras de menu definidas pelo usuário sem ativá-las.

```foxpro
SHOW MENU MenuBarName1 [, MenuBarName2 ...] | ALL   [PAD MenuTitleName]
   [SAVE]
```

#### Parâmetros
 **MenuBarName1 [, MenuBarName2 ...]**
Especifica o nome de uma ou mais barras de menu a serem exibidas.
**ALL**
Exibe todas as barras de menu atualmente definidas.
**PAD MenuTitleName**
Especifica um título de menu a ser destacado em uma barra de menu.
**SAVE**
Mantém uma imagem das barras de menu especificadas sem ativá-las. Você pode limpar as imagens da barra de menu com CLEAR .

# Observações

As barras de menu são exibidas, mas não podem ser usadas. Antes de poderem ser exibidas, você deve primeiro criar as barras de menu com DEFINE MENU.

# Exemplo

```foxpro
CLEAR
DEFINE MENU mnuExample BAR AT LINE 2
DEFINE PAD padConv OF mnuExample PROMPT '\<Conversions' COLOR SCHEME 3 ;
   KEY ALT+C, ''
DEFINE PAD padCard OF mnuExample PROMPT 'Card \<Info' COLOR SCHEME 3 ;
   KEY ALT+I, ''
SHOW MENU mnuExample
```
