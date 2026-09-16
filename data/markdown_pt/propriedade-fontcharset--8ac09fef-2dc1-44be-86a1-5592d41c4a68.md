# Propriedade FontCharSet

Especifica o conjunto de caracteres, ou script de idioma, da fonte usada para exibir texto em todo objeto que suporta fontes. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.FontCharSet [ = nFontCharSet ]
```

#### Parâmetros

| Termo | Definição |
| --- | --- |
| nFontCharSet | Especifica um valor numérico para o script de idioma desejado. |

Os valores disponíveis para FontCharSet estão listados no tópico de ajuda da função GETFONT( ).

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | Header Object | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | Page Object | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

O sistema operacional e a fonte determinam a configuração padrão de FontCharSet. Definir FontCharSet como 1 indica ao Visual FoxPro usar a configuração padrão. Se você definir FontCharSet na janela Properties explicitamente escolhendo um script de idioma na caixa de diálogo Font, a janela Properties exibe a fonte específica. Por exemplo, suponha que você defina a propriedade FontCharSet para uma caixa de texto como 1 (Western) na janela Properties. Se você abrir a Font Dialog Box e selecionar 0 (Western), a janela Properties exibe 0 (Western) porque foi definido explicitamente.

> **Dica:** Para redefinir a propriedade para a configuração padrão, clique com o botão direito do mouse na propriedade na janela Properties e clique em Reset to Default.

O Visual FoxPro tenta recuperar o identificador do conjunto de caracteres da fonte que você especifica. Se o Visual FoxPro não encontrar o identificador do conjunto de caracteres ou se você passar um valor FontCharSet inválido para um conjunto de fontes específico, o gerenciador de fontes do Windows faz a substituição apropriada usando o conjunto de caracteres Default, geralmente ANSI ou Symbol.

As fontes suportam apenas determinados scripts de idioma. Para escolher um script de idioma que uma fonte pode suportar, selecione a propriedade FontCharSet na janela Properties e clique no botão de reticências (...) que aparece para abrir a caixa de diálogo Font. Você pode selecionar um script de idioma na lista suspensa Script. Você também pode alterar a fonte, o tamanho e o estilo. O Visual FoxPro atualiza as propriedades de fonte com os valores alterados.

Se você alterar a fonte para uma na qual o valor atual de FontCharSet não é suportado, o Visual FoxPro redefine a propriedade FontCharSet.

Se a propriedade Style de um Label estiver definida como 3 (Themed), a propriedade FontCharSet é ignorada. Se a propriedade Themes estiver definida como True (.T.) para uma grade, a propriedade FontCharSet do Header da grade é ignorada. Para exibir o Header da grade usando a propriedade FontCharSet, defina Themes da grade como False (.F.).

A função GETFONT( ) suporta a passagem ou recuperação de um script de fonte.
