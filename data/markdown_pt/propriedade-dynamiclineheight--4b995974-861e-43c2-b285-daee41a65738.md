# Propriedade DynamicLineHeight

Indica se o ReportListener deve usar o espaçamento de linha padrão do GDI+ de acordo com as características da fonte ou o espaçamento de linha fixo compatível com versões anteriores.

```foxpro
ReportListener.DynamicLineHeight [= lExpr]
```

# Valor de retorno

Tipo de dados lógico.
 **True, (.T.)**
(Padrão) Objetos de várias linhas são renderizados usando o comportamento padrão do GDI+. O espaçamento de linha é determinado dinamicamente, de acordo com a fonte. Se o objeto tem preenchimento opaco ou backcolor, essa cor aparece em todo o bloco.
**False, (.F.)**
Modo compatível com versões anteriores. Objetos de várias linhas são renderizados individualmente, com espaçamento fixo. Se o objeto tem preenchimento opaco ou backcolor, essa cor aparece apenas sob o texto renderizado.

# Observações

Aplica-se a: Objeto ReportListener.

Antes do Visual FoxPro 9, o Report Engine usava uma altura de linha fixa para renderizar objetos de texto de várias linhas. A classe ReportListener do Visual FoxPro tem a capacidade de renderizar objetos de várias linhas usando o espaçamento de linha padrão do GDI+, que é ajustado dinamicamente para as características da fonte.

Você pode definir esta propriedade como `.F.` se desejar que o Report Engine renderize objetos de várias linhas linha por linha, usando o mesmo espaçamento das versões anteriores. Esse cálculo de espaçamento de linha é o seguinte:

O Engine obtém a altura do objeto do FRX (em FRUs, 1/10000 de polegada) e divide pelo número de linhas no conteúdo atual do objeto de layout, de acordo com as características da fonte atual. Ele converte o resultado para 960dpi para obter a altura de uma única linha.

Há uma penalidade de desempenho ao definir DynamicLineHeight como `.F.`, porque o Report Engine deve calcular as palavras que cabem em cada linha do objeto de várias linhas antes de adicionar o espaçamento vertical fixo e continuar a renderizar a próxima linha.

Os dois métodos de tratamento de objetos de várias linhas também diferem na forma como exibem preenchimentos opacos ou cores de plano de fundo. Quando DynamicLineHeight é `.T.`, todo o bloco de várias linhas é tratado pelo GDI+ como um único objeto. Quando DynamicLineHeight é `.F.`, cada linha renderizada separadamente contém seu próprio plano de fundo, e cada linha pode ter uma largura diferente.
