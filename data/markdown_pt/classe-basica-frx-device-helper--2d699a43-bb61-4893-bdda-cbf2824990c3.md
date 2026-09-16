# Classe básica FRX Device Helper

Esta classe fornece métodos para ler e gravar informações de dispositivo de impressora no ambiente Visual FoxPro.

| Categoria | Utilitários do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Output Helper Classes |
| Classe | frxDeviceHelper |
| Classe base | Custom |
| Biblioteca de classes | _frxcursor.vcx |
| Classe pai | Custom |

# Observações

Esta classe expõe os algoritmos usados por ReportOutput.APP, ReportBuilder.APP e ReportPreview.APP para interpretar vários valores de impressão e valores de tabelas Report (frx) e Label (lbx).

É principalmente útil para desenvolvedores que estendem a funcionalidade de relatórios do Visual FoxPro. Para obter mais informações, consulte Extensão da funcionalidade de relatórios no Visual FoxPro.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade ActualX | Largura física da página em unidades de dispositivo. Padrão: 0 |
| Propriedade ActualY | Comprimento físico da página em unidades de dispositivo. Padrão: 0 |
| Propriedade DpiX | Pixels lógicos por polegada na dimensão X. Padrão: 0 |
| Propriedade DpiY | Pixels lógicos por polegada na dimensão Y. Padrão: 0 |
| Método LoadDeviceInfo | Analisa parâmetros de dispositivo de impressão em propriedades membro, dado informações específicas do dispositivo. Sintaxe: LoadDeviceInfo([cDriver, cDevice, cDEVMODE]) Retorno: valor lógico representando sucesso Argumentos: cDriver especifica o driver de impressora , conforme armazenado em um campo EXPR de tabela Report (frx). cDevice especifica o nome da impressora, conforme armazenado em um campo EXPR de tabela Report (frx). cDEVMODE é uma cadeia de caracteres representando uma estrutura que contém informações adicionais da impressora, conforme armazenada no campo TAG2 de tabela Report . Observações: Se você omitir os argumentos opcionais, este método carrega informações da impressora padrão do VFP atual. |
| Método LoadFromFrx | Carrega parâmetros de dispositivo de impressora de um registro de cabeçalho de cursor FRX. Restaura o número do registro atual e a área de trabalho selecionada depois. Sintaxe: LoadDeviceInfo([cFrxAlias]) Retorno: valor lógico representando sucesso Argumentos: cFRXAlias contém o alias de uma tabela Report (frx) em uso no ambiente. Este método assume um alias de "FRX" se você omitir o argumento opcional cFRXAlias . |
| Propriedade mmX | Tamanho horizontal da página em milímetros. Padrão: 0 |
| Propriedade mmY | Tamanho vertical da página em milímetros. Padrão: 0 |
| Propriedade OffsetX | Margem esquerda física imprimível da página. Padrão: 0 |
| Propriedade OffsetY | Margem superior física imprimível da página. Padrão: 0 |
| Propriedade Orientation | Orientação da página (0=Retrato, 1=Paisagem). Padrão: 0 |
| Propriedade PrintableX | Largura horizontal da página em pixels. Padrão: 0 |
| Propriedade PrintableY | Comprimento vertical da página em pixels. Padrão: 0 |
| Propriedade ErrorMessage | Contém texto de erro se o método LoadDeviceInfo() retornar false. Padrão: "" |

# Exemplo

Neste exemplo, uma instância da classe frxDeviceHelper exibe informações sobre a resolução em pontos (pixels) por polegada para a impressora padrão do VFP atual.

```foxpro
oDeviceHelper = NEWOBJECT( "frxDeviceHelper" )
IF oDeviceHelper.LoadDeviceInfo()
    ? oDeviceHelper.DpiX
    ? oDeviceHelper.DpiY
ELSE
    ? oDeviceHelper.ErrorMessage
ENDIF
```
