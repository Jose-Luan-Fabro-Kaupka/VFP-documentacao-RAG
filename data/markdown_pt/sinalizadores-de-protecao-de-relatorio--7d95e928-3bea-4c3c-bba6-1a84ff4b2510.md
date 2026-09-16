# Sinalizadores de proteção de relatório

O Visual FoxPro 9.0 introduz uma nova palavra-chave no comando MODIFY REPORT | LABEL: PROTECTED. Quando um layout de relatório ou etiqueta é aberto no modo protegido, várias capacidades do designer são desabilitadas ou restritas dependendo das configurações de proteção definidas pelo desenvolvedor.

Há dois tipos de configurações de proteção: aquelas que se aplicam ao layout de relatório inteiro; e aquelas que se aplicam a elementos de relatório específicos (um controle ou faixa).

No Visual FoxPro 9.0, você ajusta as configurações de proteção para um layout na interface de usuário fornecida pelo aplicativo Report Builder padrão. As caixas de diálogo nativas do Report Designer não expõem uma maneira de editar sinalizadores de proteção.

# Sinalizadores de proteção

### Tipos de sinalizadores de proteção

As seguintes constantes são definidas no arquivo foxpro_reporting.h, localizado no diretório ..\FFC\.

Observe que esses valores de constante representam a posição de bit de cada sinalizador, não o valor inteiro real do sinalizador.

#### Sinalizadores de proteção para controles de relatório

| Constante em foxpro_reporting.h | Valor | Descrição |
| --- | --- | --- |
| FRX_PROTECT_OBJECT_LOCK | 0 | Um controle de relatório com este sinalizador definido não pode ser movido (em relação à sua faixa) ou redimensionado usando o mouse ou o teclado. Ele pode ser selecionado, clicado duas vezes e editado pelas caixas de diálogo nativas do Report Designer. Redimensionar uma faixa acima daquela em que o objeto está localizado ainda resultará no objeto sendo movido em relação ao topo do relatório, conforme esperado. |
| FRX_PROTECT_OBJECT_HIDE | 1 | Um controle de relatório com este sinalizador definido não é visível no designer. |
| FRX_PROTECT_OBJECT_NO_DELETE | 2 | Um controle de relatório com este sinalizador definido não pode ser excluído ou cortado. Você pode selecioná-lo, copiá-lo para a área de transferência de edição com Ctrl-C e colar um novo controle no layout de relatório. Importante Sem nenhum report builder ativo, os sinalizadores de proteção serão mantidos junto com os outros atributos do controle de relatório. Isso significa que você não poderá remover o controle de relatório recém-colado. Por este motivo, o report builder padrão, ReportBuilder.App, remove automaticamente os sinalizadores de proteção do controle de relatório recém-criado durante a operação de colar. Este comportamento é implementado na classe PasteUnprotectFilter, registrada por padrão na tabela de manipuladores do Report Builder. Consulte Tabela de registro de manipuladores de eventos do Report Builder para obter mais informações. |
| FRX_PROTECT_OBJECT_NO_EDIT | 3 | Para controles de relatório com este sinalizador definido, clicar duas vezes não tem efeito, e você não pode exibir o menu de contexto do objeto com um clique com o botão direito. Basicamente não há acesso à caixa de diálogo Properties do objeto. |
| FRX_PROTECT_OBJECT_NO_SELECT | 6 | Um controle de relatório com este sinalizador definido não pode ser selecionado com o mouse ou a tecla TAB. As alças de redimensionamento não aparecem. Este sinalizador implicitamente tem o mesmo efeito que OBJECT_NO_EDIT + OBJECT_LOCK. |

De modo geral, para a maioria dos propósitos práticos:
 - A proteção NO_SELECT efetivamente inclui o comportamento de proteção LOCK + NO_EDIT + NO_DELETE, mesmo se esses sinalizadores não estiverem explicitamente definidos.
- A proteção HIDDEN efetivamente inclui o comportamento de proteção LOCK + NO_EDIT + NO_DELETE + NO_SELECT, mesmo se esses sinalizadores não estiverem explicitamente definidos.

#### Sinalizadores de proteção para faixas de relatório

| Constante em foxpro_reporting.h | Valor | Descrição |
| --- | --- | --- |
| FRX_PROTECT_BAND_NO_EDIT | 4 | A caixa de diálogo Band Properties não está disponível. Clicar duas vezes na faixa não tem efeito. |
| FRX_PROTECT_BAND_NO_RESIZE | 14 | O tamanho vertical da faixa está bloqueado. A faixa não pode ser redimensionada no designer. |

#### Sinalizadores de proteção para controles de relatório

| Constante em foxpro_reporting.h | Valor | Descrição |
| --- | --- | --- |
| FRX_PROTECT_REPORT_NO_PREVIEW | 7 | O layout de relatório não pode ser visualizado em preview. |
| FRX_PROTECT_REPORT_NO_OPTBAND | 8 | A caixa de diálogo Optional Bands não está disponível. |
| FRX_PROTECT_REPORT_NO_GROUP | 9 | A caixa de diálogo Data Grouping não está disponível. |
| FRX_PROTECT_REPORT_NO_VARIABLES | 10 | A caixa de diálogo Report Variables não está disponível. |
| FRX_PROTECT_REPORT_NO_PAGESETUP | 11 | A caixa de diálogo Page Setup não está disponível. |
| FRX_PROTECT_REPORT_NO_DATAENV | 13 | O Data Environment do layout não pode ser modificado. |
| FRX_PROTECT_REPORT_NO_PRINT | 15 | O relatório não pode ser impresso a partir do designer. As opções Run Report e Print… do menu estão desabilitadas. |

### Como os sinalizadores de proteção são armazenados com o layout

Os sinalizadores de proteção são armazenados no campo memo ORDER da estrutura FRX, no registro de cabeçalho e separadamente em cada registro de controle e faixa.

Se você não estiver usando o report builder padrão, pode ajustar os sinalizadores abrindo o arquivo .frx ou .lbx e substituindo o valor armazenado no campo ORDER por um valor alternativo determinado pelo seguinte método:

Os valores dos sinalizadores de proteção são somados e armazenados como dados de caracteres binários no campo ORDER. Por exemplo: FRX_PROTECT_OBJECT_LOCK + FRX_PROTECT_OBJECT_NO_DELETE + FRX_PROTECT_NO_EDIT = 2^0 + 2^2 + 2^3 = 1+4+8 = 13. Portanto, o campo ORDER conterá CHR(13).

A Foundation Class FRX Cursor inclui alguns métodos que são úteis para extrair e substituir sinalizadores de proteção, conforme mostrado no exemplo abaixo.

### Exemplo

```foxpro
#INCLUDE foxpro_reporting.h
LOCAL oFrxHelper, cReport, iFlags
* Create the helper object:
oFrxHelper = NEWOBJECT( "frxCursor", HOME()+ "\FFC\_frxcursor.vcx")
* Select a report file:
cReport = GETFILE("FRX")
* Open a report layout as a table:
USE (m.cReport) ALIAS frx
* Go to the report header record:
LOCATE FOR frx.objtype = FRX_OBJTYP_REPORTHEADER and ;
           frx.objcode = FRX_OBJCOD_REPORTHEADER and ;
           frx.platform = FRX_PLATFORM_WINDOWS
* Extract the current protection setting:
iFlags = oFrxHelper.BinStringToInt( frx.ORDER )
* Prevent access to the Report Variables dialog box:
iFlags = BITSET( iFlags, FRX_PROTECT_REPORT_NO_VARIABLES )
* Save back to the frx record:
REPLACE frx.order WITH oFrxHelper.IntToBinString( iFlags )
USE IN frx
* Edit the report in protected mode:
MODIFY REPORT FORM (cReport) PROTECTED
```
