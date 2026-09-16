# Comando LIST DLLS

Exibe continuamente informações sobre funções de biblioteca compartilhada registradas no Visual FoxPro com DECLARE - DLL.

```foxpro
LIST DLLS [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de LIST DLLS para uma impressora. No Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo Print antes de iniciar a impressão. Coloque PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de LIST DLLS para o arquivo especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.
