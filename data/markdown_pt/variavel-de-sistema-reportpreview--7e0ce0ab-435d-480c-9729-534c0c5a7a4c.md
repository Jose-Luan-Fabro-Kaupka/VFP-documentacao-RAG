# Variável de sistema _REPORTPREVIEW

Especifica o aplicativo usado pelo Visual FoxPro para gerar instâncias de uma interface de usuário de visualização de relatório, a fim de atender solicitações de instâncias da classe ReportListener.

Para obter mais informações sobre visualizações de relatório personalizadas, consulte Extending Report Preview Functionality

```foxpro
_REPORTPREVIEW = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica o aplicativo de fábrica de objetos invocado pelo Visual FoxPro. Observação Se o aplicativo estiver localizado em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do programa.

# Observações

Por padrão, _REPORTPREVIEW refere-se a ReportPreview.App, localizado no diretório principal do Visual FoxPro.

Você também pode especificar um aplicativo a ser usado em _REPORTPREVIEW usando a guia File Locations na caixa de diálogo Options. Para obter mais informações, consulte File Locations Tab, Options Dialog Box.

O aplicativo em _REPORTPREVIEW recebe um parâmetro de referência NULL, no qual deve colocar uma referência de objeto a uma instância de uma classe que suporte a The Preview Container API. O aplicativo deve então encerrar, retornando a referência de objeto do Preview Container:

```foxpro
pc = .NULL.
DO (_REPORTPREVIEW) WITH pc
```

A variável `pc` agora contém uma referência de objeto.

Considere as seguintes instruções:

```foxpro
    rl = NEWOBJECT("Reportlistener")
    rl.ListenerType = 1
    REPORT FORM customers.frx OBJECT rl
```

Quando o Visual FoxPro executa esses comandos, verifica a propriedade PreviewContainer do Reportlistener em busca de uma referência de objeto válida. Se não encontrar uma, obtém uma chamando o aplicativo _REPORTPREVIEW.

O Visual FoxPro gerará um erro se não localizar um aplicativo para _REPORTPREVIEW durante uma visualização de relatório.

> **Observação:** Ao distribuir programas de fábrica de visualização de relatório com seus aplicativos, pode ser conveniente definir explicitamente _REPORTPREVIEW no arquivo de configuração do Visual FoxPro, Config.fpw. Para obter mais informações, consulte Including Report Files for Distribution e Setting Configuration Options at Startup .

# Exemplo

A linha de código a seguir define a variável de sistema _REPORTPREVIEW para o aplicativo padrão de visualização de relatório:

```foxpro
_REPORTPREVIEW = HOME()+"ReportPreview.app"
```
