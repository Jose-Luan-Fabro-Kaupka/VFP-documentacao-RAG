# DefOLELCID Propriedade

Especifica o padrão OLE Locale ID para um formulário ou janela principal do Visual FoxPro. Disponível em tempo de design e tempo de execução.

```foxpro
Form.DefOLELCID[ = nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor padrão OLE Locale ID para um formulário ou a janela principal do Visual FoxPro. Este valor padrão determina o local ID para OLE controles vinculados e OLE controles de contêiner quando são colocados no formulário ou na janela principal do Visual FoxPro.

# Observações
Aplica-se a: Form Objeto | _SCREEN Variável de sistema

Se o valor padrão OLE Locale ID para um formulário ou a janela principal do Visual FoxPro for alterado para um novo valor, OLE Os controles vinculados e OLE Controles de contêiner colocados no formulário ou na janela principal do Visual FoxPro após o novo valor padrão de Locale ID entrarem em vigor usarão o novo valor.

Se DefOLELCID for definido como zero para um formulário ou a janela principal do Visual FoxPro, SYS(3004) determinará o local padrão ID para OLE controles vinculados e OLE controles de contêiner colocados no formulário ou na janela principal do Visual FoxPro.

Consulte SYS(3005) - Definir local ID para obter uma lista de IDs de local.

> **Nota:** A propriedade DefOLELCID afeta apenas o idioma da interface do usuário, que OLE controla a exibição, e não o idioma dos comandos de automação. A linguagem de comando Automation é afetada apenas pelo Global LocaleID, definido com SYS(3005).
