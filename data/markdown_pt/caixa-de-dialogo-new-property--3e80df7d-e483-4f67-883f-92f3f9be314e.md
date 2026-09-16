# Caixa de diálogo New Property

Permite criar uma propriedade personalizada e especificar atributos para essa propriedade.

Esta caixa de diálogo aparece quando você escolhe New Property no menu Form que aparece quando o Form Designer está aberto ou no menu Class que aparece quando o Class Designer está aberto.

Você também pode criar métodos Access e Assign. Para obter mais informações, consulte Access and Assign Methods e How to: Create Access and Assign Methods.
 **Name**
Especifica o nome da nova propriedade.
**Visibility (Class Designer only)**
Especifica o nível de visibilidade da propriedade: Public Access está disponível de qualquer lugar em um aplicativo. Protected Restringe o acesso à propriedade aos membros da classe e subclasses podem acessar propriedades protegidas. Instâncias de objeto não podem acessar esta propriedade. Hidden Restringe o acesso à propriedade apenas aos membros da classe. Instâncias de objeto e subclasses não podem acessar propriedades ocultas. Para obter mais informações, consulte Protecting and Hiding Class Members .
**Access Method**
Especifica se um método Access é criado para a nova propriedade. O código em um método Access é executado sempre que a propriedade é consultada. Selecione esta caixa de seleção para criar um método Access para uma propriedade.
**Assign Method**
Especifica se um método Assign é criado para a nova propriedade. O código em um método Assign é executado sempre que você tenta alterar o valor da propriedade. Selecione esta caixa de seleção para criar um método Assign para uma propriedade.
**Default Value**
Especifica um valor padrão para a propriedade. O valor padrão é predefinido como False (.F.).
**Description**
Contém a descrição do método a ser exibida na parte inferior da janela Properties no Class Designer e, se a propriedade não estiver protegida, no Form Designer.
