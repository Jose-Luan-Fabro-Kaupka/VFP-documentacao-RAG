# Exemplo Pass Parameters Between Forms

Arquivo: ...\Samples\Solution\Forms\Param.scx

Esta solução ilustra a passagem de parâmetros para um formulário e o retorno de um valor.

# Formulário PARAM

Este formulário faz o usuário inserir uma pergunta e possíveis respostas. Em seguida, no evento Click do botão cmdAsk, o formulário ParamAsk é aberto passando Question e Possible responses.

```foxpro
cParam1 = THISFORM.txtPassValue1.value
nParam2 = THISFORM.opgPassValue2.value
DO FORM LOCFILE("ParamAsk.scx") WITH cParam1, nParam2 TO nRetValue
```

# Formulário PARAMASK

Os PARAMETERS são passados ao Init do formulário onde são processados.

```foxpro
PARAMETERS cQuestion, nButtons
THISFORM.txtQuestion.caption = cQuestion
```

No evento Unload do formulário, o valor armazenado em retvalue é retornado ao formulário chamador:

```foxpro
RETURN THISFORM.retValue
```
