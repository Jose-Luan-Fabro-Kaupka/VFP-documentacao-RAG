# Exemplo de cronômetro

Arquivo: ...\Samples\Solution\Controls\Timer\Swatch.scx

Este exemplo inclui a classe Stopwatch.

# Classe Stopwatch

A classe Stopwatch inclui um timer e vários labels de exibição. O Timer incrementa propriedades personalizadas numéricas da classe e define a propriedade Caption dos labels de acordo.
 Configurações de propriedade para a classe Stopwatch
| Controle | Propriedade | Configuração |
| --- | --- | --- |
| lblSeconds | Caption | 00 |
| lblColon1 | Caption | : |
| lblMinutes | Caption | 00 |
| lblColon2 | Caption | : |
| lblHours | Caption | 00 |
| tmrSWatch | Interval | 1000 |

# Formulário Swatch

O formulário Swatch contém um objeto derivado da classe Stopwatch, junto com alguns botões de comando. O código escrito para o evento Click do primeiro botão de comando no formulário chama os métodos Start e Stop da classe Stopwatch. O segundo botão chama o método Reset da classe Stopwatch.

# Propriedades e métodos protegidos

Este exemplo também ilustra o uso de propriedades e métodos protegidos. A classe Stopwatch contém três propriedades protegidas, nSec, nMin e nHour, e um método protegido, UpdateDisplay.

> **Dica:** Escolha Class Info no menu Class para ver a visibilidade de todas as propriedades e métodos de uma classe.

As propriedades protegidas são usadas em cálculos internos no método UpdateDisplay e no evento Timer. O método UpdateDisplay define os captions dos labels para refletir o tempo decorrido.
 Método UpdateDisplay
| Código | Comentários |
| --- | --- |
| cSecDisplay = ALLTRIM(STR(THIS.nSec)) cMinDisplay = ALLTRIM(STR(THIS.nMin)) cHourDisplay = ALLTRIM(STR(THIS.nHour)) | Converte as propriedades numéricas para o tipo Character para exibição nos captions dos labels. |
| THIS.lblSeconds.Caption = ; IIF(THIS.nSec < 10, ; "0" ,"") + cSecDisplay THIS.lblMinutes.Caption = ; IIF(THIS.nMin < 10, ; "0", "") + cMinDisplay THIS.lblHours.Caption = ; IIF(THIS.nHour < 10, ; "0", "") + cHourDisplay | Define os captions dos labels, mantendo o 0 à esquerda se o valor da propriedade numérica for menor que 10. |

A tabela a seguir lista o código no evento `tmrSWatch.Timer`:
 Evento Timer
| Código | Comentários |
| --- | --- |
| THIS.Parent.nSec = THIS.Parent.nSec + 1 IF THIS.Parent.nSec = 60 THIS.Parent.nSec = 0 THIS.Parent.nMin = ; THIS.Parent.nMin + 1 ENDIF | Incrementa a propriedade nSec sempre que o evento timer é disparado: a cada segundo. Se nSec atingir 60, redefine para 0 e incrementa a propriedade nMin. |
| IF THIS.Parent.nMin = 60 THIS.Parent.nMin = 0 THIS.Parent.nHour = ; THIS.Parent.nHour + 1 ENDIF THIS.Parent.UpdateDisplay | Se nMin atingir 60, redefine para 0 e incrementa a propriedade nHour. Chama o método UpdateDisplay quando os novos valores de propriedade são definidos. |

A classe Stopwatch tem três métodos personalizados que não são protegidos: Start, Stop e Reset. Um usuário pode chamar esses métodos diretamente para controlar o cronômetro.

O método Start contém a seguinte linha de código:

```foxpro
THIS.tmrSWatch.Enabled = .T.
```

O método Stop contém a seguinte linha de código:

```foxpro
THIS.tmrSWatch.Enabled = .F.
```

O método Reset define as propriedades protegidas como zero e chama o método protegido:

```foxpro
THIS.nSec = 0
THIS.nMin = 0
THIS.nHour = 0
THIS.UpdateDisplay
```

O usuário não pode definir essas propriedades diretamente ou chamar este método, mas o código no método Reset pode.
