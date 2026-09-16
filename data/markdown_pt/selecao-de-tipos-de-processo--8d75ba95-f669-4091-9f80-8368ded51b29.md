# Seleção de tipos de processo

Servidores in-process e out-of-process fornecem serviços diferentes, especialmente em relação à interface do usuário da aplicação.

# Interfaces do usuário

Embora versões anteriores do Visual FoxPro permitissem usar formulários como elementos somente de saída em uma aplicação de servidor Automation, as duas bibliotecas de tempo de execução no Visual FoxPro tratam essa situação de forma diferente para servidores out-of-process e in-process.

# Servidores in-process

O suporte a threading no modelo apartment exige que servidores Automation .dll in-process não tenham interfaces do usuário. No Visual FoxPro 5.0, era possível (embora não recomendado) criar um servidor Automation .dll in-process com interface do usuário, como um formulário. Você podia usar o formulário apenas para exibição, pois os eventos do formulário não eram suportados. Desde o Visual FoxPro 6, se você tentar criar uma interface do usuário em um .dll in-process, o Automation gera um erro. Isso é chamado de modo não assistido.

# Servidores out-of-process

Um servidor Automation out-of-process (.exe) pode ter interface do usuário. A função SYS(2335) - Unattended Server Mode do Visual FoxPro permite desabilitar a interface do usuário e eventos modais para um servidor Automation .exe out-of-process, para que possam ser tratados remotamente sem intervenção do usuário. Eventos modais são criados por formulários modais definidos pelo usuário, caixas de diálogo do sistema, a função MESSAGEBOX( ) e o comando WAIT, entre outros, e normalmente exigem entrada do usuário.
