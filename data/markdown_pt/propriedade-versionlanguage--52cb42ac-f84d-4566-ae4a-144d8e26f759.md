# Propriedade VersionLanguage

As informações de idioma para um projeto.

```foxpro
Object.VersionLanguage[ = nLanguage]
```

# Valor de retorno
 **nLanguage**
Especifica o ID de idioma para um projeto. FOXPRO.H contém uma listagem dos valores para os IDs de idioma principal e subidioma que podem ser combinados para criar um ID de idioma válido. Por exemplo, o código a seguir define VersionLanguage para inglês dos Estados Unidos (0x09 especifica inglês, 0x0400 especifica inglês dos Estados Unidos) para o projeto atual: Application.ActiveProject.VersionLanguage = 0x09 + 0x0400

# Observações

Aplica-se a: Objeto Project (Visual FoxPro)

A propriedade VersionLanguage corresponde ao valor do item Language ID na caixa de diálogo EXE Version.
