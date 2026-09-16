# Exemplo Manipulate Objects Programmatically

Arquivo: ...\Samples\Solution\Forms\Objects.scx

Este exemplo mostra como definir propriedades em tempo de execução para objetos em um form set. O form set de exemplo contém dois formulários. O código associado ao evento Click de controles em ambos os formulários altera as configurações de propriedade de outros controles.

Ao definir propriedades de controles em tempo de execução, lembre-se de referenciar o controle por meio de sua hierarquia de contêineres. Por exemplo, para definir a propriedade Value de um controle em um formulário a partir de código em um método de outro formulário, referencie o contêiner de nível mais alto (o form set) e todos os contêineres subsequentes.

```foxpro
THISFORMSET.frmLeft.chkBold.Value = .F.
```
