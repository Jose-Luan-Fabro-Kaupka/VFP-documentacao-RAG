# Propriedade MaxTop

Especifica a distância de um formulário maximizado da borda superior da janela principal do Visual FoxPro. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MaxTop[ = nMaxTop]
```

# Valor de retorno
 **nMaxTop**
Especifica a distância da borda superior da janela principal do Visual FoxPro até a borda superior do formulário maximizado, na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: objeto Form | variável de sistema _SCREEN

Esta propriedade é ignorada no Visual FoxPro para Macintosh.

Use a propriedade MaxTop para garantir que um formulário maximizado não seja movido muito próximo ao topo da janela principal do Visual FoxPro em tempo de execução.
