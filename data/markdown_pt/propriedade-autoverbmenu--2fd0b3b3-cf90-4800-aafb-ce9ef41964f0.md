# Propriedade AutoVerbMenu

Especifica se um menu de atalho contendo os verbos de um objeto OLE é exibido quando o objeto OLE é clicado com o botão direito do mouse. Disponível somente em tempo de execução.

```foxpro
Control.AutoVerbMenu[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: Configuração Descrição True (.T.) (Padrão) O menu de atalho contendo os verbos do objeto OLE é exibido quando o objeto OLE recebe um clique com o botão direito. False (.F.) O menu de atalho contendo os verbos do objeto OLE não é exibido quando o objeto OLE recebe um clique com o botão direito.

# Observações

Aplica-se a: Enabled Property (Visual FoxPro) | OLE Bound Control | OLE Container Control

Em tempo de execução, se as propriedades AutoVerbMenu e Enabled estiverem definidas como true (.T.), clicar com o botão direito no objeto OLE exibe o menu de atalho contendo os verbos suportados pelo objeto OLE. Se as propriedades AutoVerbMenu e Enabled estiverem definidas como false (.F.) ou o objeto OLE não suportar verbos, o menu de atalho não é exibido quando você clica com o botão direito no objeto OLE.
