# Evento QueryUnload

Ocorre antes de um formulário ser descarregado.

```foxpro
PROCEDURE Form.QueryUnload
```

# Observações

Aplica-se a: Form Object

O evento QueryUnload ocorre antes do evento Destroy. A propriedade ReleaseType é definida antes de o evento QueryUnload ser chamado.

O evento QueryUnload ocorre quando CLEAR WINDOWS, RELEASE WINDOWS ou QUIT é executado em código, ou quando o usuário clica duas vezes no ícone do menu pop-up da janela ou escolhe Close no menu pop-up da janela de um formulário.

> **Observação:** O evento QueryUnload não ocorre se você emitir o comando RELEASE no formulário em código ou invocar o método Release do formulário.

Emitir NODEFAULT no procedimento do evento QueryUnload impede que o formulário seja descarregado.
