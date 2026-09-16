# Classe base ReportListener XML Display-Style

A classe XmlDisplayListener ajusta as configurações padrão do esquema XML de relatório VFP do XmlListener de forma adequada para necessidades de saída de apresentação. Para informações completas sobre o Esquema XML de Relatório VFP e suas opções, consulte Usando XML de saída de relatório VFP.

O XmlDisplayListener também adiciona capacidades de publicação de arquivos de imagem:
 - Você pode copiar os arquivos de imagem usados no seu relatório para um novo local.
- Você pode salvar imagens renderizadas durante o relatório a partir de campos General ou referências de controle de imagem, que não eram baseadas em arquivos, em arquivos no disco.

Essas capacidades são úteis quando você está preparando a saída de relatório para ser publicada ou empacotada para exibição na Web ou para processamento adicional por outro aplicativo de publicação.

Consulte Classe base ReportListener HTML para código de exemplo.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | XmlDisplayListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | XmlListener ( Classe base ReportListener XML ) |

# XmlDisplayListener, campos General e controles Image

Ao processar imagens que não vieram de um arquivo no disco, o XmlDisplayListener sempre fornece uma cópia no disco para seu uso. Por padrão, esses arquivos são colocados no mesmo local do arquivo de saída de relatório gerado, mas você pode definir esse local para uma pasta diferente, usando a propriedade XmlDisplayListener.externalFileLocation. A pasta que você indicar para esse uso deve existir; caso contrário, o XmlDisplayListener ignora a instrução.

> **Dica:** Ao preparar documentos para publicação na Web, você frequentemente desejará definir o local dos arquivos de imagem em um diretório separado do arquivo de saída principal. É uma boa ideia definir o local como uma referência relativa, como ".\images . " O XmlDisplayListener entende essas referências como relativas ao arquivo de saída principal.

O XmlDisplayListener deve salvar uma imagem separada no disco sempre que o relatório renderiza uma imagem. Como essas imagens podem ser diferentes para cada registro do seu relatório, ele usa uma convenção de nome de arquivo gerado para nomear os arquivos. Você pode ajustar esses nomes de arquivo adicionando um nome de arquivo base, ao qual o XmlDisplayListener adiciona sua porção gerada como sufixo. Isso distingue seus arquivos de imagem de outros arquivos de execuções de relatório diferentes.

Por padrão, a classe base ReportListener não envia informações completas de imagem para suas classes derivadas. Você deve solicitar as informações apropriadas, usando a propriedade ReportListener.SendGDIPlusImage.

No início de uma execução de relatório, o XmlDisplayListener verifica se há campos General no design do seu relatório. Se encontrar referências a campos General, ele define .SendGDIPlusImage temporariamente, se necessário, e restaura o valor posteriormente.

No Visual FoxPro 9, designs de relatório podem incluir expressões que referenciam controles Image, bem como campos general e arquivos de imagem no disco. Se o Report Engine encontrar uma expressão representando um objeto Image control associado a um controle de layout Image enquanto processa seu relatório, ele usa as informações de imagem na propriedade PictureVal do controle Image. Para obter mais informações, consulte Propriedade PictureVal.

O XmlDisplayListener não pode saber que as expressões de layout do seu relatório podem representar controles Image (em vez de referências indiretas a arquivos de imagem no disco) quando avalia seu FRX. Por esse motivo, se você usar expressões representando controles Image, a menos que também haja campos General no seu relatório, você deve definir explicitamente seu XmlDisplayListener.SendGDIPlusImage. Essa instrução explícita fará com que o ReportListener forneça as informações de imagem necessárias ao renderizar seu relatório. Com essa propriedade definida, o XmlDisplayListener detecta o identificador GDPlusImage na primeira vez que recebe um e, se ainda não tiver feito isso anteriormente, definirá os outros atributos associados necessários para salvar os arquivos no disco.

# XmlDisplayListener e imagens baseadas em arquivo

Por padrão, o XmlDisplayListener simplesmente referencia quaisquer imagens baseadas em arquivo no disco usando o nome de arquivo original e fornecendo informações de caminho completo para o arquivo de origem. No entanto, você pode instruir o XmlDisplayListener a publicar uma cópia dos seus arquivos de imagem em seu .externalFileLocation no disco, para que você possa mover os arquivos de imagem com o arquivo de saída XML principal posteriormente. Para informar ao XmlDisplayListener que deseja copiar os arquivos de imagem, use sua propriedade .copyImageFilesToExternalFileLocation.

# Observações

O XmlDisplayListener adiciona as seguintes propriedades públicas à sua classe pai, XmlListener. O XmlDisplayListener não adiciona métodos públicos.

| Propriedades e métodos | Descrição |
| --- | --- |
| Propriedade externalFileLocation | Atribui opcionalmente um caminho UNC ou do sistema de arquivos, relativo ou absoluto, que o resultado XML atribuirá a quaisquer arquivos externos, como imagens, referenciados no arquivo de saída XML principal. Padrão "" |
| Propriedade copyImageFilesToExternalFileLocation | Indica se imagens baseadas em arquivo devem ser copiadas para um local comum a partir de seus locais originais no disco, para referência como fontes de imagem na saída XML. Padrão .F. |
| Propriedade imageSrcAttr | Fornece o nome do atributo XML usado para mostrar o nome de arquivo copiado ou gerado para imagens não baseadas em arquivo, em tempo de execução. Padrão "img" |
| Propriedade formattingChanges | Referência na qual as classes podem armazenar informações sobre ações tomadas para aplicar alterações a atributos de formatação de objetos dinamicamente durante uma execução de relatório. Padrão .NULL. |
