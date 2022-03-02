import telebot
import re
import time
import consultas

# CHAVE DO BOT DO BOTFATHER


CHAVE_BOT = "5048043556:AAE1Qsus9G7H8sZKyp5vXbTtwn5t6XW4KsU"

bot = telebot.TeleBot(CHAVE_BOT)

# COMANDO /TOTAL


@bot.message_handler(commands=["total"])
def total(mensagem):
    bot.reply_to(mensagem, consultas.calcular_total())

# COMANDO CLIENTE


@bot.message_handler(commands=["cliente"])
def cliente(mensagem):
    try:
        # PEGAR NUMERO DO COMANDO
        id_cliente = str(re.findall(r'\d+', mensagem.text)[0])
        # VERIFICAR ID NA TEBELA
        if(consultas.codido_total_venda(id_cliente) == 'ID DO PEDIDO E VALOR:'):
            bot.reply_to(mensagem, 'ID INVALIDO, INFORME OUTRO!\n' +
                         consultas.ver_clientes())
        else:
            bot.reply_to(mensagem, consultas.codido_total_venda(id_cliente))
    except:
        bot.reply_to(mensagem, consultas.ver_clientes())

# COMANDO /ID_CLIENTE


@bot.message_handler(func=lambda mensagem: mensagem.text.replace('/', '') in consultas.ids_clientes())
def cliente_id(mensagem):
    id_cliente = mensagem.text.replace('/', '')
    # RESPONDER /ID_CLIENTE
    bot.reply_to(mensagem, consultas.codido_total_venda(id_cliente))

# VERIFICAR SE FOI ENVIADO UMA MENSAGEM


@bot.message_handler(func=lambda verificar: True)
def responder(mensagem):
    resposta = """
Digite o comando:

/total = Retorna o valor de todas as vendas.

/cliente <cliente_id> = Retorna o código da última venda, valor total da venda e os itens da venda com os seus respectivos valores e quantidade do cliente informado.

Apenas essas opções.
"""
    bot.reply_to(mensagem, resposta)


# LOOP PARA O BOT FICAR ATIVO E RECONECTANDO


while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
