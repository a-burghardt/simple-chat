# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece pra todo mundo)
    # a mensagem que voce entrou no chat
    # o campo e o botao de enviar mensagem
# a cada mensagem que voce envia (aparece pra todo mundo)
    # Nome: Texto da mensagem
# pode-se adicionar a funcao "view=ft.WEB_BROWSER" apos target=main para abrir como website
# start_button = ft.ElevatedButton("Iniciar Chat")

import flet as ft

def main(page):
    chat = ft.Column()
    def send_message_tunnel(infos):
        username = infos["username"]
        if infos["type"] == "entry":
            chat.controls.append(ft.Text(f"{username} entrou no chat", size=12, color=ft.colors.ORANGE_400, italic=True))
        else:
            message = infos["message"]
            chat.controls.append(ft.Text(f"{username}: {message}"))
        page.update()

    page.pubsub.subscribe(send_message_tunnel)

    def send_message(event):
        page.pubsub.send_all({"username": username.value, "message": message_field.value, "type": "message"})
        message_field.value = ""
        page.update()

    message_field = ft.TextField(label="Digite uma mensagem", on_submit=send_message)
    send_message = ft.ElevatedButton("Enviar", on_click=send_message)

    def entrar_chat(e):
        page.add(chat)
        page.add(ft.Row([message_field, send_message]))
        modal.open = False
        page.pubsub.send_all({"username": username.value, "type": "entry"})
        page.remove(start_button)
        page.update()

    username = ft.TextField(label="Escreva o nome do usuário")
    modal = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=username,
        actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

    def open_modal(event):
        page.dialog = modal
        modal.open = True
        page.update()

    start_button = ft.ElevatedButton("Iniciar Chat", on_click=open_modal)

    page.add(start_button)

ft.app(target=main, view=ft.WEB_BROWSER)
