# Propriedade Align

Especifica o alinhamento de um controle ActiveX™ (.ocx) em um formulário. Disponível em tempo de design e em tempo de execução.

```foxpro
OLEContainerControl.Align[ = nAlign]
```

# Valor de retorno
 **nAlign**
As configurações da propriedade Align são: Configuração Descrição 0 Alinhamento padrão. O controle ActiveX é colocado na mesma posição que o controle OLE Container no formulário. 1 Superior. O controle ActiveX é colocado na parte superior do formulário. 2 Inferior. O controle ActiveX é colocado na parte inferior do formulário. 3 Esquerda. O controle ActiveX é colocado na borda esquerda do formulário. 4 Direita. O controle ActiveX é colocado na borda direita do formulário.

# Observações

Aplica-se a: OLE Container Control

Um controle ActiveX (arquivo .ocx) é colocado no controle OLE Container.

A propriedade Align está disponível somente para controles ActiveX que suportam alterações em seu alinhamento. Objetos OLE inseríveis, como planilhas do Microsoft Excel, não suportam a propriedade Align.

A propriedade Align está disponível somente para controles ActiveX que são colocados em um formulário.

Se dois ou mais controles ActiveX tiverem a mesma configuração da propriedade Align, os controles são empilhados uns sobre os outros.
