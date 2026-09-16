# A API Preview Container

Ao visualizar um layout de relatório ou etiqueta no modo assistido por objetos, um ReportListener requer um componente adicional para fornecer a interface do usuário de visualização. Este componente é chamado preview container e é escrito em código Visual FoxPro, sendo portanto completamente personalizável.

Existem duas maneiras de uma instância ReportListener obter um preview container quando precisa de um:
 - Seu código atribui explicitamente uma referência de objeto à propriedade PreviewContainer do ReportListener.
- O objeto ReportListener solicita uma referência de objeto ao aplicativo Preview Container Object Factory referenciado pela variável de sistema _REPORTPREVIEW System Variable .

# A API Preview Container

Um objeto da classe ReportListener espera que os seguintes métodos sejam implementados pelo objeto atribuído à sua propriedade PreviewContainer:

| Método PreviewContainer | Parâmetro | Descrição |
| --- | --- | --- |
| SetReport() | oListenerRef | O objeto ReportListener invocará este método, passando uma referência a si mesmo para que o código do preview container possa chamar de volta métodos do listener. SetReport() pode ser chamado antes que o relatório tenha concluído o processamento, então este método deve armazenar o valor do parâmetro para referência posterior. SetReport() pode ser chamado com um valor .NULL., caso em que o preview container deve limpar quaisquer referências internas a um objeto report listener passado anteriormente e reinicializar-se. |
| Show() | [ iModality ] | O objeto ReportListener chamará este método quando o mecanismo de relatório estiver pronto para exibir a interface de visualização e permitir que o usuário navegue pela saída do relatório ou etiqueta. O parâmetro iModal é o mesmo passado ao Show Method (Visual FoxPro) de um formulário. |

Embora não referenciada por nenhum programa externo, um objeto que implementa a API Preview Container deve ter uma referência interna ao objeto report listener passado ao objeto via o método .SetReport().

| Propriedade PreviewContainer | Tipo | Descrição |
| --- | --- | --- |
| oReport | Object | Os métodos .SetReport() e .Show() são chamados em momentos diferentes. Para que o preview container tenha acesso a várias propriedades do report listener no momento em que o método Show() é chamado, ele deve salvar a referência do report listener passada em SetReport() em uma propriedade interna. |

Um objeto da classe ReportListener também espera receber mensagens de um objeto atribuído à sua propriedade PreviewContainer:

| Método ReportListener | Parâmetro | Descrição |
| --- | --- | --- |
| OnPreviewClose() | lPrint | O ReportListener espera que seu método OnPreviewClose() seja chamado quando a interface do usuário de visualização é fechada ou dispensada pelo usuário. O objeto PreviewContainer pode enviar o parâmetro lPrint para indicar se o usuário escolheu imprimir da visualização. Exatamente qual método PreviewContainer faz a chamada não é importante. Se o objeto PreviewContainer for um formulário, ou tiver uma interface semelhante à de um formulário, alguns métodos candidatos seriam Hide() , Release() , QueryUnload() e Destroy() . |

São necessárias algumas linhas de código para juntar tudo:

```foxpro
* Instantiate your preview container implmentation
oMyPreview = NEWOBJECT("MyPreviewContainer","MyClassLib")
* Instantiate a ReportListener (or your own derived class)
oListener  = CREATEOBJECT("ReportListener")
* Tell the listener to render all pages and use a preview container:
oListener.ListenerType = 1
* Give the listener a reference to your preview container:
oListener.PreviewContainer = m.oMyPreview
* Run the report:
REPORT FORM myreport OBJECT m.oListener
```

Para um exemplo de implementação simples de preview container, consulte Creating a Custom Preview Container.

# A fábrica de objetos _REPORTPREVIEW

O código mostrado acima cobre o caso em que um ReportListener recebe explicitamente uma referência de preview container antes de executar o relatório. Se o ReportListener não tiver uma referência de preview container e precisar de uma, ele obtém uma chamando o aplicativo ou programa referenciado pela variável de sistema _REPORTPREVIEW.

O programa referenciado por _REPORTPREVIEW deve fazer o seguinte:
 - Aceitar um parâmetro, passado por referência do mecanismo de relatório.
- Atribuir ao parâmetro uma referência de objeto a uma instância de uma classe que implementa a API preview container.
- Retornar.

Exemplo:

```foxpro
* Program suitable for _REPORTPREVIEW:
LPARAMETER loRef
loRef = NEWOBJECT("MyPreviewContainer","MyClassLib")
return
```

O programa em _REPORTPREVIEW é invocado quando você emite os seguintes tipos de comandos do Visual FoxPro:
 - REPORT FORM ou LABEL … PREVIEW quando SET("REPORTBEHAVIOR") tem o valor 90.
- REPORT FORM ou LABEL … OBJECT < oRef > quando oRef.ListenerType tem o valor 1 e você não atribuiu um valor a oRef.PreviewContainer.
- REPORT FORM ou LABEL … OBJECT TYPE 1 quando o ReportListener atribuído pela fábrica de listeners especificada por _REPORTOUTPUT não tem já um valor atribuído ao seu membro PreviewContainer.
