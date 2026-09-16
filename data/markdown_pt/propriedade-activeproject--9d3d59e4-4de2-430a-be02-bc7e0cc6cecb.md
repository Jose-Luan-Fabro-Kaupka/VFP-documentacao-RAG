# Propriedade ActiveProject

Contém uma referência de objeto para o objeto Project da janela Project Manager atualmente ativa. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.ActiveProject
```

# Observações

Aplica-se a: Objeto Application | Variável de sistema _VFP

A propriedade ActiveProject contém uma referência de objeto para o objeto Project da janela Project Manager em primeiro plano quando mais de uma janela Project Manager está aberta. Um erro é gerado se você tentar acessar a propriedade ActiveProject quando uma janela Project Manager não está aberta.

Para obter mais informações sobre projetos, consulte Project Manager Hooks e Ferramentas de produtividade de desenvolvimento.

# Exemplo

O exemplo a seguir usa a propriedade ActiveProject para obter uma contagem de relatórios e etiquetas em um projeto ativo. Se o projeto MyApp não existir, ele será criado quando MODIFY PROJECT for executado.

```foxpro
MODIFY PROJECT myApp NOSHOW NOWAIT
nRptsLbls=0
FOR EACH oFile IN _VFP.ACTIVEPROJECT.FILES
   IF INLIST(oFile.Type, "R", "B")  && Report and Label
      nRptsLbls=nRptsLbls+1
   ENDIF
ENDFOR
```
