# Evento AdjustObjectSize

Ocorre imediatamente antes de o ReportListener começar a renderizar elementos de layout do tipo Shape ou Picture.

```foxpro
PROCEDURE Object.AdjustObjectSize
LPARAMETERS nFRXRecno, oObjProperties
```

#### Parâmetros

O Visual FoxPro passa os parâmetros do evento AdjustObjectSize na seguinte ordem:
 **nFRXRecno**
Tipo de dados Integer, especificando o número do registro no arquivo de definição de relatório ou etiqueta (frx ou lbx) que descreve o elemento de layout sendo renderizado.
**oObjProperties**
Um objeto da classe Empty, com membros que fornecem valores relevantes para ajustar o tamanho de um Shape ou Picture. oObjProperties member Type Usage reload Logical, defaults to .F. Flag to alert the ReportListener if you make changes. Set this value to True ( .T. ) to notify the ReportListener of changes to height or width . height Integer, valid values from 0 to 64000 Height of layout element, in 960ths of an inch. If you change this value and set reload to .T. , the ReportListener renders with the revised value. width Integer, valid values from 0 to 64000 Width of layout element, in 960ths of an inch. If you change this value and set reload to .T. , the ReportListener renders with the revised value. top,left Integer, readonly Coordinates of top- and left-most point of the Shape or Picture element. Provides information about the position of the layout element on the output page, for reference in calculations. reattempt Logical, readonly Indicates whether this element has been pushed to a second page because it did not fit on the previous page. maxheightavailable Integer, readonly Indicates the available room on this page for this element, allowing for the height of subsequent bands (such as the page footer) for which space must be reserved. Note Microsoft reserves the right to invoke AdjustObjectSize for additional report and label layout elements, as needed, and to add to the oObjProperties members appropriately for these additional layout element types. You can use nFRXRecno to test for layout element type, as shown in the sample code in Render Method .

# Observações

Aplica-se a: ReportListener Object.

O VisualFoxPro invoca AdjustObjectSize uma vez para cada elemento de layout do tipo Shape ou Picture, a menos que não encontre código na classe ReportListener derivada em tempo de execução. Também não chama AdjustObjectSize se o elemento estiver em uma banda não marcada como Stretchable (altura de banda fixa). Para mais informações, consulte a caixa de diálogo Report Band Properties.

> **Dica:** Para melhorar o desempenho, o Visual FoxPro não chama AdjustObjectSize nem EvaluateContents se determinar que não há código no ReportListener para o evento. Se você geralmente inclui código de espaço reservado ou código generalizado em cada evento, considere omitir esse código para esses dois eventos, especialmente se o nível da classe é abstrato (nunca instanciado diretamente). Inclua código somente nos níveis de classe que realmente usam essa funcionalidade. O custo de desempenho para AdjustObjectSize aumenta aproximadamente na mesma proporção para cada elemento Shape ou Picture em um relatório; o custo de desempenho para EvaluateContents varia. Para mais informações, consulte o evento EvaluateContents .

Este recurso é principalmente para o uso de ReportListeners que interpretam certos Shapes como espaços reservados para objetos personalizados, que eles desenham no espaço reservado para o Shape no layout.

AdjustObjectSize não é suportado para Shapes ou Pictures que se estendem entre qualquer par de bandas de cabeçalho e rodapé, e não suporta alterações na curvatura da forma.

Embora o parâmetro oObjProperties tenha vários membros, o único valor que afetará o comportamento de renderização base do ReportListener é uma alteração em oObjProperties.height. A alteração em oObjProperties.height é respeitada somente se a nova altura for maior que a altura original. Essa alteração causará uma mudança na altura do elemento conforme renderizado pelo ReportListener e também fará outros elementos de layout flutuantes serem empurrados para baixo, e a banda se estenderá para acomodar a nova altura.

Como não é suportado para Shapes ou Pictures que abrangem bandas, você não pode ajustar a altura de um Shape para continuar por várias páginas. Se o elemento não couber na página após o ReportListener alterar sua altura, o elemento inteiro será empurrado para a próxima página. Em alguns casos, porque nem todas as bandas podem abranger páginas, essa determinação pode resultar na banda inteira sendo empurrada para a próxima página. Consulte Report Bands para mais informações sobre quais bandas podem abranger páginas.

Use o membro oObjProperties.maxheightavailable para determinar o tamanho máximo que você pode dar ao Shape ou Picture sem que ele seja empurrado inteiramente para a próxima página.

Quando você define um valor maior que oObjProperties.maxheightavailable para oObjProperties.height e define oObjProperties.reload como True (`.T.`), o evento Render do ReportListener não é chamado para este elemento na página atual. Em vez disso, AdjustObjectPage é chamado novamente para o mesmo elemento na próxima página.

Na próxima página, oObjProperties.height é definido de volta ao seu valor original, oObjProperties.reattempt é definido como True (`.T.`) e oObjProperties.maxheightavailable tem um novo valor, baseado no novo valor de oObjProperties.top nesta página. Neste ponto, você pode reavaliar a altura desejada para o elemento na nova página.

> **Cuidado:** Se você definiu um valor de altura muito grande para qualquer página, o elemento não será exibido. Nenhum erro imediato ocorre, mas atribuições continuadas desse valor farão o elemento ser empurrado repetidamente para páginas subsequentes. Use oObjProperties.reattempt para evitar tentar recarregar o mesmo valor repetidamente, após sua tentativa inicial.

Alterações no valor oObjProperties.width não afetam o comportamento de renderização base do ReportListener; porém, serão passadas à sua classe derivada para uso em Render se oObjProperties.reload for True (`.T.`).

Tanto oObjProperties.height quanto oObjProperties.width têm um intervalo válido de 0 a 64000. Se qualquer valor for definido fora do intervalo, ele é ajustado para 0 ou 64000 e nenhum erro ocorre.

oObjProperties.top e oObjProperties.left são somente leitura. Eles são passados para referência da sua classe derivada, pois não há outra forma para o ReportListener determinar onde no layout da página esta instância do elemento será renderizada.

# Exemplo

Este exemplo ajusta a altura de um elemento de layout em um relatório para exibir uma imagem de tamanho diferente para cada registro em uma tabela. O nome do arquivo da imagem é armazenado em uma coluna da tabela e a altura desejada da imagem (em polegadas) é armazenada em uma segunda coluna da tabela. As imagens referenciadas em cada registro podem ter alturas diferentes, e alguns registros não incluem arquivo de imagem. No layout do relatório, o elemento de imagem é definido com apenas alguns pixels de altura; uma expressão que representa a coluna da tabela que contém o nome do arquivo de imagem está associada a este elemento de layout. Elementos na mesma banda abaixo desta região são definidos para flutuar e estender.

No código BeforeReport, o ReportListener determina qual registro na definição de layout FRX descreve a imagem e salva essas informações para uso posterior. Quando o evento AdjustObjectSize ocorre, o ReportListener verifica seu argumento nFRXRecno para ver se o elemento FRX sendo avaliado corresponde ao número de registro armazenado para o elemento de imagem. Se corresponder, o ReportListener ajusta a altura do elemento de imagem para corresponder à imagem associada a este registro.

> **Dica:** Observe que o código AdjustObjectSize multiplica o valor de altura armazenado na tabela por 960. A tabela armazena suas medidas em polegadas, e o código de renderização do ReportListener trata medidas em 960 pontos por polegada (DPI).

```foxpro
DEFINE CLASS rl AS ReportListener
   FrxPic = 0

  PROCEDURE BeforeReport()
     SET DATASESSION TO (THIS.FRXDataSession)
     SELECT FRX
     LOCATE FOR ObjType = 17 && image
     IF EOF()
        THIS.FrxPic = 0
     ELSE
        THIS.FrxPic = RECNO()
     ENDIF
   ENDPROC
   PROCEDURE AdjustObjectSize(nFrxRecno,oProps)
       IF nFrxRecno = THIS.FrxPic
          SET DATASESSION TO (THIS.CurrentDataSession)
          IF (NOT EMPTY(MyTable.picFile))
             * express in DPI units:
             oProps.Height = MyTable.picInches * 960
             oProps.Reload = .T.
          ENDIF
       ENDIF
   ENDPROC

ENDDEFINE
```
