# Propriedade _MemberData

Especifica uma cadeia de caracteres XML que contém configurações de extensibilidade para o Visual FoxPro no nível da classe. Por exemplo, você pode especificar um editor de propriedades personalizado, exibir uma propriedade na guia Favorites ou alterar a capitalização. Leitura/gravação somente em tempo de design.

```foxpro
Class._MemberData = [cXMLstring]
```

# Valor de retorno
 **cXMLString**
Cadeia de caracteres XML representando uma personalização.

# Observações

Você pode anotar o XML MemberData com detalhes de personalização. A personalização que você adiciona a _MemberData está nos níveis da classe e global. O nível da classe sempre substitui o nível global. No nível da classe, o suporte é tratado pela propriedade _MemberData. A propriedade contém uma cadeia de caracteres XML com os metadados reais do membro. Como propriedade, ela é herdada e substituída por subclasses.
