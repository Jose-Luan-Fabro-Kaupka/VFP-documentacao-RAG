# Recursos de relatório para aplicações internacionais

Este tópico discute recursos do Sistema de Relatórios do Visual FoxPro 9 que facilitam o desenvolvimento de relatórios para uso em aplicações internacionais.

> **Observação:** Alguns dos recursos discutidos aqui estão disponíveis apenas no modo de relatório assistido por objetos do Visual FoxPro. Se você não ver algumas das melhorias descritas neste tópico, use o comando SET REPORTBEHAVIOR 90 , ou inclua a cláusula OBJECT no comando REPORT FORM ou LABEL. Para obter mais informações, consulte Comando SET REPORTBEHAVIOR .

# Usando script de idioma em relatórios

Assim como você pode escolher fontes individualmente para elementos de layout de relatório, pode escolher um script de idioma para cada elemento individualmente. Para obter mais informações, consulte Como: alterar configurações de fonte em controles de relatório.

Se você não escolher um script de idioma para um elemento específico, ele recebe suas informações de script de idioma, como suas informações de fonte, do padrão do relatório. Você usa a opção Default Font… no menu Report para essa finalidade. Também é possível definir os padrões de fonte e de script de idioma de um relatório usando a guia Page Layout da caixa de diálogo Report Properties. Para obter mais informações, consulte Como: alterar configurações de página para relatórios.

Ao criar um novo relatório, a fonte padrão e o script de idioma do relatório são determinados pela sua preferência global, conforme definido na caixa de diálogo Tools Options. Para obter mais informações, consulte Guia Reports, caixa de diálogo Options.

> **Dica:** A escolha global da caixa de diálogo Options, a guia Page Layout do Report Builder e as opções do Report Builder para definir fontes para elementos de layout individuais oferecem a opção de omitir o script de idioma das configurações de fonte. Quando você escolhe essa opção, o script de idioma dos elementos do relatório corresponde às configurações regionais padrão do computador. Esse comportamento é compatível com versões anteriores do Visual FoxPro.

O script de idioma com o qual o Sistema de Relatórios do Visual FoxPro gera a saída para elementos de layout de relatório está automaticamente disponível para formas adicionais de saída de relatório que você pode criar com classes derivadas de ReportListener. O texto de origem fornecido no parâmetro eContentsToBeRendered do método Render do ReportListener é Unicode, e o Sistema de Relatórios nativo já converteu os dados para o conjunto de caracteres apropriado. Para obter mais informações, consulte Método Render.

A Classe Foundation ReportListener XML fornece um exemplo de um tipo de saída alternativo que aproveita esse recurso. A classe usa o valor Unicode do seu método Render para lidar automaticamente com scripts de idioma mistos na saída do relatório. Ela converte os valores Unicode para construir documentos codificados em UTF-8. Para obter mais informações sobre a saída XML da classe, consulte Usando XML de saída de relatório VFP.

> **Cuidado:** Esse recurso pode parecer funcionar em relatórios quando você não usa o modo assistido por objetos, ao visualizar os relatórios na pré-visualização. No entanto, a impressão não será como esperado, e o recurso é suportado apenas no modo assistido por objetos.

# Localizando Report Builder, ReportPreview e componentes de saída de relatório

Os componentes de origem distribuíveis do Sistema de Relatórios do Visual FoxPro fornecem cada um um arquivo de cabeçalho (.h) que você pode alterar para localizar todas as cadeias de feedback ao usuário. Você pode recompilar os aplicativos e redistribuí-los separadamente, para fornecer um componente de relatório compartilhado externo. Também é possível vincular sua versão ajustada de cada componente diretamente ao arquivo .exe ou .app da sua aplicação.

A tabela a seguir lista o arquivo de cabeçalho apropriado para cada componente e fornece um tópico de ajuda que você pode ler para saber mais sobre como especificar o arquivo de componente de relatório ajustado para uso na aplicação.

| Nome do arquivo do componente | Uso em aplicações | Nome do arquivo de cabeçalho de localização | Tópico de ajuda com informações adicionais |
| --- | --- | --- | --- |
| ReportBuilder.app | Aprimora a experiência do usuário na criação e modificação de layouts de relatório e etiqueta. | frxbuilder_loc.h | Como: especificar e distribuir ReportBuilder.App |
| ReportPreview.app | Fornece uma interface de usuário flexível para pré-visualizações de relatório renderizadas com GDI+. | frxpreview_loc.h | Como: especificar e distribuir ReportPreview.App |
| ReportOutput.app, _reportlistener.vcx | Fornece classes ReportListener para relatórios assistidos por objetos. | reportoutput_locs.h, reportlisteners_locs.h | Como: especificar e distribuir componentes de aplicativo de saída de relatório Classes Foundation ReportListener |
| _frxcursor.vcx | Fornece algoritmos úteis para criar e ajustar relatórios programaticamente. | _frxcursor.h | Classe Foundation FRX Cursor |

Para obter mais informações, consulte Incluindo arquivos de relatório para distribuição.

Cada componente também inclui interfaces de programação de aplicativos (APIs) apropriadas para alterar mensagens de feedback ao usuário em tempo de execução, para personalizar fins regionais, bem como outras necessidades específicas da aplicação. Por exemplo, a Classe Foundation ReportListener User Feedback, a classe derivada de ReportListener padrão para saída de impressão e pré-visualização, fornece membros públicos que você usa para definir suas várias mensagens de status de texto e legendas. O Aplicativo Report Preview expõe uma propriedade Caption e uma API extensa para ajustar seu menu de contexto. Para obter mais informações, consulte Aproveitando o contêiner de pré-visualização padrão.

# Tratando a ordem de leitura (da direita para a esquerda e da esquerda para a direita) de vários idiomas

O Report Designer suporta idiomas da direita para a esquerda com as propriedades Text Alignment e Reading Order. Você pode criar elementos de layout de etiqueta e texto (expressão) para corresponder aos resultados desejados da direita para a esquerda, definindo ambas as propriedades para os elementos selecionados, usando as seguintes opções no menu Format:
 - Defina o Text Alignment do elemento de layout como Right
- Defina a propriedade Reading Order como Right to Left .

> **Observação:** A opção Reading Order no menu Format está desabilitada, a menos que você tenha definido as configurações regionais do Windows para exibir um idioma da direita para a esquerda, como árabe ou hebraico, para aplicativos não Unicode. Depois de habilitar a configuração, você pode definir valores de Reading Order diferentes para itens de relatório individuais conforme necessário para um relatório com idiomas mistos.

Em tempo de execução, o novo sistema de renderização GDI+ do Visual FoxPro 9 oferece tratamento mais flexível e preciso do alinhamento para idiomas da direita para a esquerda. Ele também renderiza o alinhamento de forma mais consistente entre a saída de pré-visualização e impressão.

Classes derivadas de ReportListener têm acesso às configurações de alinhamento e ordem de leitura armazenadas no seu relatório ou etiqueta, e podem tomar ações baseadas nessas configurações. Por exemplo, a Classe Foundation ReportListener HTML usa essas opções para determinar os componentes `text-align` e `direction` dos atributos `style` para elementos de texto HTML individuais.
