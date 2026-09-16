# Como: modificar triggers (Visual FoxPro)

Você pode modificar triggers pelo Table Designer ou pela linguagem.

### Para modificar um trigger
- Na guia Table do Table Designer , insira a nova expressão de trigger nas caixas Insert trigger , Update trigger ou Delete trigger. -ou-
- Emita o comando SET SAFETY OFF e depois use o CREATE TRIGGER Command .

Quando você modifica um trigger emitindo primeiro o comando SET SAFETY Command OFF e depois recriando o trigger, a expressão de trigger antiga é automaticamente excluída e substituída pela expressão de trigger recriada.
