# Tela inicial
    # Título - Hashzap
    # Botão: Iniciar Chat
        # Ao clicar, abre popup/modal/alerta
            # Título: Bem vindo ao Hashzap
            # Caixa de Texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # Ao clicar:
                    # Retirar o popup,
                    # Retirar título
                    # Retirar botão iniciar
                    # Carregar chat
                    # Carregar o campo de enviar msg: "Digite sua mensagem"
                    # Botão enviar
                        # Ao clicar:
                            # Enviar mensagem
                            # Apagar caixa de mensagens


# Possíveis ferramentas para criar sites:
# Flask, Django, Kivy, Tkinterl, Streamlit, Flet

# Iremos utilizar Flet - possível criar site, app desktop e app para celular,
# utilizando o mesmo código para todos
# para instalar -> pip install flet

# Flet
# importar flat
# import flet as ft
# criar função principal para rodar o app
# def main():
# executar função com o flet
# ft.app(main)

# criar uma função:
# def nome_da_funcao(parametro):
#    oque essa função vai fazer


#TEMPO - 1:39
import flet as ft

def main(pagina):
    #título e botão inicial
    
    # ElevatedButton pode ser substituido por qualquer tipo de botão
    # Vírgula após o texto pode passar qualquer parâmetro, alterando o botão
    # SEMPRE QUE UMA FUNÇÃO está atribuída a algum evento de click no botão,
    # Necessário passar como parâmetro o evento, mesmo que não seja utilizado.
    # ft.FilePicker - permite enviar arquivos. 
    titulo = ft.Text("Hashzap")

    # criar função que será executada para todos os usuários pelo
    # tubo de comunicação
    # websocket - túnel de comunicação entre 2 ou mais usuários
    def enviar_mensagem_tunel(mensagem):
        # executar tudo oque quero que aconteça para todos os usuários
        # que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    # flet chama o túnel de comunicação de pubsub
    # criando o tunel de comunicação:
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evt):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # texto = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
        # chat.controls.append(texto)
        campo_enviar_mensagem.value=""
        pagina.update()

    #on_submit - função de enviar com enter
    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem",
                                         on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # Retirar o popup,
        popup.open = False
        # Retirar título
        pagina.remove(titulo)
        # Retirar botão iniciar
        pagina.remove(botao)
        # Carregar chat
        pagina.add(chat)
        # Carregar o campo de enviar msg: "Digite sua mensagem"
        # pagina.add(campo_enviar_mensagem)
        # Botão enviar
        # pagina.add(botao_enviar)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        # texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
        # chat.controls.append(texto_mensagem)
        pagina.update()

    # Criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                            actions=[botao_popup])
#para mais de um botão:
    #popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
    #                        actions=[botao_popup, bt2, bt3, ...])

    def abrir_popup(evt):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    pagina.add(titulo)

    botao = ft.ElevatedButton("Inciar Chat", on_click=abrir_popup)
    pagina.add(botao)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)
#ft.app(target=main, view=ft.WEB_BROWSER)