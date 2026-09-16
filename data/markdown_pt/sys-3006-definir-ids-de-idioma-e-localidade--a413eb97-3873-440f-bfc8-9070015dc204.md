# SYS(3006) - Definir IDs de idioma e localidade

Define o Language ID e o Locale ID.

```foxpro
SYS(3006, nLanguageID)
```

#### Parâmetros
 **nLanguageID**
Especifica o Language ID.

# Valor de retorno

Character

# Observações

SYS(3006) define o Visual FoxPro Language ID (LangID) e, em seguida, define o Locale ID (LCID) com base no Language ID e no valor atual do Sort ID.

> **Observação:** Usar a propriedade DefOLELCID é o método preferido para definir um Locale ID para um formulário ou para a janela principal do Visual FoxPro.

Para obter informações adicionais sobre Language, Locale e Sort IDs, consulte a documentação do Microsoft Windows Software Development Kit.
