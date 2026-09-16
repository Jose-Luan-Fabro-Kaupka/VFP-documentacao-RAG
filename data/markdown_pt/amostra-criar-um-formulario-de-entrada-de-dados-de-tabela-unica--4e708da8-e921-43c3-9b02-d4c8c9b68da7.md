# Amostra Criar um formulário de entrada de dados de tabela única

Arquivo: ...\Samples\Solution\Forms\Single.scx

Esta amostra ilustra o cenário mais simples para um formulário de entrada de dados de tabela única para um único usuário.

A propriedade ControlSource de cada uma das caixas de texto e caixas de combinação no formulário é definida para um campo na tabela Customer.

Um comando APPEND BLANK é emitido no evento Click de cmdNew.

```foxpro
APPEND BLANK
THISFORM.Refresh
```

O comando DELETE é emitido no evento Click de cmdDelete.

```foxpro
* cmdDelete.Click
#DEFINE MSGBOX_YES      6
#DEFINE C_MSGBOX1      36
#DEFINE C_DELETE_LOC   "Are you sure you want to delete this record?"
IF MESSAGEBOX(C_DELETE_LOC,C_MSGBOX1) = MSGBOX_YES
   DELETE
   IF !EOF()
      SKIP 1
   ENDIF
   IF EOF() AND !BOF()
      SKIP -1
   ENDIF
   THISFORM.Refresh
ENDIF
```

# Ampliando o formulário de entrada de dados

Para criar um formulário de entrada de dados mais robusto, que permita ao usuário cancelar alterações ou permita que vários usuários acessem os mesmos dados, você precisa usar transações e bufferização de tabela ou de linha.
