# Comando SET SYSFORMATS

Especifica se as configurações do sistema do Visual FoxPro para Windows são atualizadas com as configurações atuais do sistema Microsoft Windows.

```foxpro
SET SYSFORMATS ON | OFF
```

#### Parâmetros
 **ON**
Especifica que as configurações do sistema Visual FoxPro são atualizadas quando as configurações do sistema Windows são alteradas. SET SYSFORMAT ON é idêntico a escolher a caixa de seleção Use System Settings na guia International da caixa de diálogo Options. Observe que emitir SET SYSFORMAT ON altera a configuração SET DATE para SHORT. As configurações são usadas durante a sessão de dados atual ou, se emitidas durante a sessão de dados padrão, durante a sessão do Visual FoxPro.
**OFF**
(Padrão) Especifica que as configurações do sistema Visual FoxPro não são atualizadas quando as configurações do sistema Windows são alteradas. As configurações padrão do Visual FoxPro não são restauradas.

# Observações

As configurações do sistema Windows são especificadas na opção International do Painel de Controle do Windows.

Quando SET SYSFORMATS é ON, os seguintes comandos SET podem ser usados para substituir as configurações atuais do sistema. No entanto, alterar as configurações do sistema Windows quando SET SYSFORMATS é ON substitui esses comandos SET:
 - SET CENTURY
- SET CURRENCY
- SET DATE
- SET DECIMALS
- SET HOURS
- SET MARK TO
- SET POINT
- SET SEPARATOR

Quando o Visual FoxPro é iniciado, as configurações do sistema Visual FoxPro são as configurações padrão desses comandos SET. Para usar as configurações do sistema Windows quando o Visual FoxPro é iniciado, coloque a seguinte linha em seu arquivo de configuração Config.fpw do Visual FoxPro:

```foxpro
SYSFORMATS = ON
```

SET SYSFORMATS tem escopo na sessão de dados atual.
