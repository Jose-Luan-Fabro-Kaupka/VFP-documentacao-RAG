# vfp.VFPXMLProgId não oferece suporte ao parâmetro cSchemaLocation para XMLUpdateGram(). (Erro 2137)

Ocorre quando o Visual FoxPro tenta usar o parâmetro cSchemaLocation em uma implementação personalizada de XMLUpdateGram com vfp.VFPXMLProgid. O Visual FoxPro não permite o uso do parâmetro cSchemaLocation em implementações personalizadas.
 - Se o parâmetro cSchemaLocation for necessário em sua implementação personalizada de XMLUpdateGram, adicione o valor ao esquema por meio de sua própria implementação.
