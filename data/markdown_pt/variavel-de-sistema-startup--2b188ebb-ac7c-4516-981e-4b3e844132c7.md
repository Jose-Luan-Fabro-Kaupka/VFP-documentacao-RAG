# Variável de sistema _STARTUP

Especifica o nome do aplicativo que é executado quando você inicia o Visual FoxPro.

```foxpro
_STARTUP = ProgramName
```

#### Parâmetros
 **ProgramName**
Especifica o aplicativo que é executado quando você inicia o Visual FoxPro. Você deve incluir _STARTUP no arquivo de configuração do Visual FoxPro. Você também pode especificar um comando ou programa a ser executado quando o Visual FoxPro inicia incluindo um dos seguintes no arquivo de configuração: COMMAND = cVisualFoxProCommand - Ou - COMMAND = DO ProgramName Um aplicativo de inicialização especificado com _STARTUP sempre é executado antes de um comando ou programa especificado com COMMAND no arquivo de configuração.

# Observações

Você também pode especificar um aplicativo de inicialização na guia Locais de arquivo da caixa de diálogo Opções.
