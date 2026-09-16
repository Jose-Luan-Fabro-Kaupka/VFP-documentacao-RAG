# Estendendo a funcionalidade de visualização de relatórios

Além dos eventos do construtor do Designer de Relatórios, que são pontos de extensão do processo de criação de relatórios, o Visual FoxPro também fornece pontos de extensão no processo de execução. Eles são disponibilizados por meio de ReportListener, cuja instância é usada em relatórios assistidos por objeto.

Há duas maneiras de habilitar relatórios assistidos por objeto:
 - SET REPORTBEHAVIOR 90
- Escrever código que use explicitamente a cláusula OBJECT no comando REPORT FORM.

Os tópicos desta seção apresentam o componente de contêiner de visualização usado pela classe ReportListener ao renderizar visualizações em relatórios assistidos por objeto e explicam como utilizá-lo nos aplicativos.

# Nesta seção
 **A API do contêiner de visualização**
Descreve as propriedades e os métodos que uma classe deve implementar para ser usada como contêiner de visualização.
**Criando um contêiner de visualização personalizado**
Descreve como substituir o contêiner padrão por um componente personalizado capaz de fornecer automaticamente a funcionalidade de visualização de relatórios em todo o aplicativo quando você usa SET REPORTBEHAVIOR 90.
**Utilizando o contêiner de visualização padrão**
Descreve os recursos adicionais do componente fornecido pelo aplicativo Preview Container Object Factory, distribuído com o Visual FoxPro e referenciado por padrão pela variável de sistema _REPORTPREVIEW.
**Como: especificar e distribuir ReportPreview.App**
Explica como distribuir ReportPreview.App, como arquivo App separado ou integrando o código-fonte ao projeto do aplicativo.

# Seções relacionadas

Compreendendo os eventos do construtor de relatórios

Objeto ReportListener

Comando SET REPORTBEHAVIOR

Comando REPORT FORM

Variável de sistema _REPORTPREVIEW

Estendendo a funcionalidade de saída de relatórios

Estendendo relatórios em tempo de design
