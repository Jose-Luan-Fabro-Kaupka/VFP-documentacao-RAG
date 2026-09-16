# Comando DISPLAY MEMORY

Exibe o conteúdo atual de variáveis e arrays.

```foxpro
DISPLAY MEMORY [LIKE FileSkeleton]
   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **[LIKE FileSkeleton ]**
Exibe informações sobre variáveis e arrays que correspondem ao padrão esqueleto FileSkeleton . Se você incluir LIKE FileSkeleton , o Microsoft Visual FoxPro exibe somente o conteúdo de variáveis e arrays que correspondem a FileSkeleton . FileSkeleton suporta curingas como ? e *. Por exemplo, para exibir todas as variáveis que começam com a letra A , execute: DISPLAY MEMORY LIKE A*
**[TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY MEMORY para uma impressora. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo antes do início da impressão. Nesta caixa de diálogo, você pode ajustar as configurações da impressora, incluindo o número de cópias e os números de página a imprimir. As configurações da impressora que você pode ajustar dependem do driver de impressora atualmente instalado. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName [ADDITIVE]]**
Direciona a saída de DISPLAY MEMORY para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, você será solicitado a substituir o arquivo. ADDITIVE especifica anexar a saída ao final do arquivo especificado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**[NOCONSOLE]**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

DISPLAY MEMORY exibe o nome, o tipo, o conteúdo, o escopo e o status de todas as variáveis e arrays de variáveis atualmente definidos. Inclui o número de variáveis definidas, o número de bytes usados e o número de variáveis adicionais disponíveis. DISPLAY MEMORY também exibe informações sobre variáveis de sistema, menus, barras de menu, títulos de menu e janelas.

> **Observação:** O número de bytes usados representa a memória usada por variáveis do tipo caractere. Variáveis do tipo caractere são o único tipo de variáveis que requer memória adicional além da alocada pela contagem de variáveis especificada com o item de configuração MVCOUNT.

# Exemplo

No exemplo a seguir, várias variáveis são criadas e recebem valores. DISPLAY MEMORY primeiro exibe todas as variáveis que começam com "sam" e depois exibe todas as variáveis que contêm cinco letras e terminam com "exit."

```foxpro
STORE 'Goodbye' TO sample1
STORE 'Hello' TO sample2
STORE .T. TO texit
STORE .F. TO mexit
CLEAR
DISPLAY MEMORY LIKE sam*
DISPLAY MEMORY LIKE ?exit
```
