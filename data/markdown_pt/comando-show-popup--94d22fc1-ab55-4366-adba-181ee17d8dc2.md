# Comando SHOW POPUP

Exibe um ou mais menus definidos com DEFINE POPUP sem ativá-los.

```foxpro
SHOW POPUP MenuName1 [, MenuName2 ...] | ALL    [SAVE]
```

#### Parâmetros
 **MenuName1 [, MenuName2 ...]**
Especifica o nome de um ou mais menus a exibir.
**ALL**
Exibe todos os menus atualmente definidos.
**SAVE**
Mantém uma imagem dos menus especificados sem ativá-los. As imagens do menu podem ser limpas com CLEAR .

# Observações

Os menus são exibidos, mas não podem ser usados. Antes de poderem ser mostrados, os menus devem primeiro ser criados com DEFINE POPUP.
