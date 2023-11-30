#Cada comentário se refere ao código executado a baixo de si.
#Importando as bibliotecas necessárias para o código funcionar:

#Gradio é a biblioteca que executa o chatbot e mostra ele de forma visual, 
#é possivel usá-la com uma API dentro de um site. Ela também possui alguns elementos de HTML e CSS que podem modificar a sua estilização.
import gradio as gr

#Declaração de listas de palavras-chave que o programa irá reconhecer.
ajuda = ['Ajuda', 'ajuda', 'Ajudar', 'ajudar', 'Comandos', 'comandos', 'ajudar?']
informacao = ['Informação', 'informação', 'Informacao', 'informacao', 'info', 'Info', 'Informações', 'informações', 'Informacoes', 'informacoes']
emergencia1 = ['Emergência', 'emergência', 'Emergencia', 'emergencia', 'Emergen', 'emergen', 'Emergente', 'emergente']
emergencia2 = ['Ambulância', 'ambulância', 'Ambulancia', 'ambulancia', 'Socorro', 'socorro', 'Socoro', 'socoro']
otorrino = ['Orelha', 'orelha', 'Ouvido', 'ouvido', 'Chiado', 'chiado', 'Cera', 'cera', 'Nariz', 'nariz', 'Catarro', 'catarro', 'Garganta', 'garganta', 'Guela', 'guela']
psicologo = ['Emoções', 'emoções', 'Emocoes', 'emocoes', 'Emoção', 'emoção', 'Emocao', 'emocao', 'Sentimento', 'sentimento', 'Extresse', 'extresse', 'Ansiedade', 'ansiedade', 'Tristeza', 'tristeza', 'Triste', 'triste', 'Depressão', 'depressão', 'Depresao', 'depresao', 'Pânico', 'pânico', 'Panico', 'panico']
queimaduras = ['Queimaduras', 'queimaduras', 'Fogo', 'fogo', 'Explosão', 'explosão', 'Explosao', 'explosao', 'Quente', 'quente']

#Criação da função Chat, sendo ela a principal parte do programa, tendo em vista que ela executa todas as partes condicionais do código.
#A função recebe dois valores, sendo eles message, que representa a mensagem digitada pelo usuário e history, que nessa aplicação não esta sendo usada no momento porém é utilizada
#como uma lista de listas para armazenar respectivamente o que o usuario escreveu desde o começo do programa e o que o chatbot respondeu a ele.
def chat(message, history):
    
    #Criação da função emergência, a função emergencia será chamada se algum paciente tiver uma pergunta relacionada a algum problema que ele tem, nesse caso só é possivel inserir
    #os itens dentro de otorrino e psicologo, tendo em vista que essa só é uma representação de uma parte do programa, que e extremamente expansivel e outras especializações
    #podem ser adicionadas, ela recebe o valor message, tendo em vista que precisa também reconhecer a pergunta do usuário.
    def emergencia(message):
        
        #A variavel message recebe ela mesma só que são removidos os caracteres: (?), (.), (,), (!) para evitar que palavras chave sejam acompanhadas deles e sejam impedidas
        #de serem identificadas nas listas.
        message = message.strip('?.,!')
        #Criação da variavel msg que recebera uma lista com as palavras da frase contida em message e irá separá-las.
        msg = message.split()
        
        #Criação de um for que percorrerá a variavel y no range da quantidade de itens da lista msg.
        for y in range(len(msg)):
            #Utilização de um if para verificar se o item[y] atual da lista msg está contido na lista otorrino.
            if msg[y] in otorrino:
                #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
                return "Para descobrir informações com os sintomas que você forneceu, você deveria marcar uma consulta com um otorrino."
                #Finalização do for utilizando break
                break
            #Utilização de um if para verificar se o item[y] atual da lista msg está contido na lista psicologo.
            if msg[y] in psicologo:
                #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
                return "Para descobrir informações com os sintomas que você forneceu, você deveria marcar uma consulta com um psicologo."
                #Finalização do for utilizando break
                break
    
    #Continuação da função chat
    
    #A variavel message recebe ela mesma só que são removidos os caracteres: (?), (.), (,), (!) para evitar que palavras chave sejam acompanhadas deles e sejam impedidas
    #de serem identificadas nas listas.
    message = message.strip('?.,!')
    #Criação da variavel msg que recebera uma lista com as palavras da frase contida em message e irá separá-las.
    msg = message.split()
    #Criação de um for que percorrerá a variavel x no range da quantidade de itens da lista msg.
    for x in range(len(msg)):
        #Utilização de um if para verificar se o item[x] atual da lista msg está contido na lista ajuda.
        if msg[x] in ajuda:
            #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
            return "Os comandos disponiveis são os seguintes: \n• Ajuda \n• Informação \n• Emergência \nCaso o comando digitado não for ajuda, tente escrever a pergunta de outra forma \nou escreva as palavras disponiveis a cima" 
            #Finalização do for utilizando break
            break
        #Utilização de um elif, executado se a condição a cima não for atendida, para verificar se o item[x] atual da lista msg está contido na lista informacao.
        elif msg[x] in informacao:
            #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
            return "Sou o assistente virtual da HapvidaAway! No que posso te ajudar hoje? \nPara mais comandos digite ''ajuda''"
            #Finalização do for utilizando break
            break
        #Utilização de um elif, executado se as condições a cima não forem atendidas, para verificar se o item[x] atual da lista msg está contido na lista emergencia1 ou na lista
        #emergencia2.
        elif msg[x] in emergencia1 or msg[x] in emergencia2:
            #Utilização de um if para verificar se o item[x] atual da lista msg está contido na lista emergencia1.
            if msg[x] in emergencia1:
                #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
                return "Como posso ajudar?"
                #Finalização do for utilizando break.
                break
            #Utilização de um elif, executado se a condição a cima não for atendida, para verificar se o item[x] atual da lista msg está contido na lista emergencia2.
            elif msg[x] in emergencia2:
                #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira. A mensagem é apenas visual visto que não temos nenhum meio de realizar um link
                #com os funcionarios do hospital ainda.
                return "Um de nossos agentes será contatado e ira realizar uma ligação dentro de um minuto para o telefone cadastrado nos dados do convênio, \npor favor aguarde para ser atendido." 
                #Finalização do for utilizando break
                break
            #Finalização do for utilizando break
            break
        #Utilização de um elif, executado se as condições a cima não forem atendidas, para verificar se o item[x] atual da lista msg está contido na lista otorrino ou
        #na lista psicologo.
        elif msg[x] in otorrino or msg[x] in psicologo:
            #Retorno criado para chamar a função emergencia explicada no começo do código.
            return emergencia(message)
            #Finalização do for utilizando break
            break
        #Utilização de um elif, executado se as condições a cima não forem atendidas, para verificar se o item[x] atual da lista msg está contido na lista queimaduras
        elif msg[x] in queimaduras:
            #Retorno da seguinte mensagem pelo chatbot se a condição a cima for verdadeira.
            return "Os primeiros socorros de queimaduras são: \n•Não aplicar produtos ''refrescantes'' na area afetada; \n•Não encostar panos molhados ou para apagar o fogo, tendo em vista que eles podem grudar no tecido \n•Lavar com agua corrente em temperatua ambiente \n•Para apagar o fogo oriente que a pessoa role no chão \n•Não ofereça liquidos"
    #Retorno da seguinte mensagem pelo chatbot se nenhuma das condiçoes a cima forem verdadeiras.
    return "Não entendi a pergunta, verifique se o comando foi digitado corretamente. \nDigite ''ajuda'' para mais comandos!"

#Criação de uma variavel para receber a função de criação de chat do Gradio utilizando a função chat.
hapvida_away = gr.ChatInterface(chat)

#Utilizando a variavel a cima para iniciar a interface visual do Gradio
hapvida_away.launch()