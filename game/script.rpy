define config.name = _("Academia Novel Brasil")

define f = Character("Fábio", color="#c8ffc8")
define g = Character("Galdino", color="#c8c8ff")
define n = Character("Nebi", color="#c8c8ff")
define n_u = Character("????", color="#c8c8ff")
define f_u = Character("????", color="#c8c8ff")
define g_u = Character("Professor", color="#c8c8ff")
define p = Character("[name]")

default likesBread = False

label start:

    python:
        name = renpy.input("Digite o seu nome")
        name = name.strip() or "Protagonista"

label day1:
    scene bg classroom
    with fade

    "Hoje é meu primeiro dia na Academia Novel Brasil."

    "Este lugar basicamente é o maior formador de talentos de webnovels no país inteiro."

    "Depois de muita insistência e convecimento da minha parte, meus pais finalmente concordaram em me matricular aqui!"

    "O prédio se parece bem ordinário. Não que eu estivesse esperando algo de anormal."

    "Talvez o fato de eu ter me mudado de cidade acabou me dando uma expectativa subconsciente sobre a escola."

    "Inclusive, acabei me perdendo no metrô. Isso significa que..."

    "...estou atrasado!"

    "Chega de devaneios! Hora de entrar."

    #scene bg school_hallway
    #with fade

    "O corredor está vazio. Mas ainda escuto vozes de alunos. Provavelmente já estão em sala, mas a aula ainda não deve ter começado."

    "Preciso encontrar a minha sala. Segundo o email enviado pela escola, é a 1-D. Leio as placas das salas ao meu redor."

    p "1-A, 1-B, 1-C... 2-A?"

    "Onde está a sala D? Era só o que me faltava...Será que realmente irei perder aula, justo no primeiro dia?"

    "Uma garota adentra o predio. Pelo jeito que ela caminha, provavelmente não está perdida, que nem eu."

    "Geralmente eu estaria com muita vergonha de perguntar, mas a vergonha de perder a primeira aula por um motivo bobo acaba sendo maior."

    p "C-com licença... Você poderia me ajudar?"

    n_u "Hum?"

    show nebi armsbehind smiling at center

    n_u "Por acaso você tá perdido?"

    p "Sim... Não consigo encontrar a sala 1-D."

    n_u "1-D? Acredito que se encontra no segundo andar."

    n_u "Inclusive, é pra lá que estou indo! Tambem sou da 1-D. Vem comigo!"

    p "Serio? Que alívio!"

    n_u "Bom, assumindo que o e-mail enviado pela escola esteja correto! Tambem é a minha primeira vez por aqui."

    p "...Isso estava no e-mail?"

    "Ops..."

    scene bg classroom
    with fade

    "Chegamos na sala correta. Todos os alunos já se encontram sentados. Restam apenas duas cadeiras vazias. Uma no meio da sala, e outra na primeira fileira."

    "A garota que chegou junto comigo se dirige a cadeira na primeira fileira. O jeito é ir para a do meio. Não estou muito afim de sentar na frente, mesmo"

    "Ao me sentar, percebo que o garoto sentado na minha direita me encara de um jeito meio desconfortável."

    show fabio sheathed smug at right

    f_u "Hunf!"

    p "..."

    f_u "Hunf!"

    p "..."

    p "Algo de errado..?"

    f_u "Odeio pessoas atrasadas! Pontualidade é algo essencial para um autor de sucesso!"

    p "É mesmo?"

    f_u "É!"

    p "E cadê o professor?"

    f_u "Ainda não chegou..."

    hide fabio

    "Enquanto ele diz isso, a porta da sala se abre, e um adulto entra."

    show galdino nobook neutral at center

    g_u "Bom dia a todos!"

    g_u "Peço desculpas pelo atraso. Acabei me perdendo no metrô, acreditam?"

    g_u "Enfim, já que este é o primeiro dia, vamos começar pelas apresentações. Meu nome é Galdino Velasco. Podem me chamar apenas de Galdino."

    "Galdino Velasco..."

    g "Serei o seu professor durante este ano. Tenho dado aula nesta instituição a mais de dez anos. Apesar disso, a arte da escrita, sobretudo de webnovels, ainda tem um enorme espaço de crescimento no nosso país."

    g "Espero ver grandes obras vindo dos escritores desta classe, e que atraiam ainda mais pessoas para este meio."

    g "Como podem ver, minhas expectativas são altas. Mas quero que saibam que nós da Novel Brasil estaremos aqui para ajudar-los durante esta jornada. Conte conosco, e chegaremos longe!"

    "Os alunos começam a murmurar entre si. Apesar do discurso ter sido meio... cafona, não há dúvidas de que causou uma certa impressão na sala."

    "Parando pra pensar, a maioria dos meus amigos da minha escola antiga nunca nem ouviram falar em webnovels. Talvez ele esteja certo. "

    g "Agora, eu quero ouvir vocês. Gostaria que cada um se apresente brevemente para a classe!"

    g "Vamos começar pela primeira fileira."

    "Galdino olha em direção à garota que me ajudou anteriormente. Ela se levanta."

    hide galdino

    show nebi armsbehind smiling at center

    n_u "Bom dia! Meu nome é Nebi!"

    n "Meu passatempo favorito é ler livros e webnovels, e sempre quis escrever a minha propria história! Conto com a ajuda de todos para nos tornamos grandes escritores!"

    hide nebi

    show galdino nobook neutral at center

    "Prazer em conhecer, Nebi. Próximo, por favor?"

    hide galdino

    "Pouco a pouco, os alunos se apresentam. A maioria possui uma história parecida com a da Nebi. Me pergunto se eles realmente sempre quiseram ser escritores, ou se apenas estão imitando a primeira ideia original..."

    "Após alguns minutos, finalmente chega a minha vez. Me levanto, e percebo que minha mente está em branco. E agora? Porque não pensei em algo para falar nesse meio tempo?"

    p "..."

    p "..."

    menu:
        p "Olá! Meu nome é [name]. Eu..."

        "...gosto de ler, mas nunca escrevi nada.":

            jump intro1

        "...nunca li nem escrevi, mas acho que consigo pegar o jeito.":

            jump intro2

        "...gosto de pão!":

            jump intro3

label intro1:

    "A reação da turma é parecida com as reações às outras apresentações até entao. Talvez seja melhor desse jeito, sem causar uma impressão negativa."

    jump intro_continue

label intro2:

    "Os murmuros na classe aumentam. Percebo alguns alunos com um semblante confuso, e outros quase rindo."

    "Talvez eu seja a única pessoa que teve a coragem de vir pra cá sem saber nada. O que será que tenho na cabeça?"

    jump intro_continue

label intro3:

    $ likesBread = True

    show galdino nobook neutral at center

    g "Hum, ok..."

    g "Estava esperando algo mais... literário, mas acho que isso dá pro gasto."

    hide galdino

    "A classe gargalhou em uníssono. Acho que esse foi o pior branco que eu tive na minha vida. Felizmente esse é o tipo de coisa que pessoas esquecem logo..."

    jump intro_continue

label intro_continue:

    "O próximo a se apresentar é o garoto de cabelo verde."

    show fabio sheathed smug at center

    f_u "Saudações! Podem me chamar de Fábio."

    f "Este é o meu nome humano. Caso estejam curiosos, o meu nome real foi selado para conter uma grande ameaça!"

    "Lá vem..."

    f "Peço que nunca usem o meu nome selado, senão um grande mal cairá sobre essa escola! Este nome é..."

    "Se não é pra falar, pra que ele fica insistindo tanto nisso?"

    f "...Earth Makai Destroyer-sama!!"

    "..."

    "Pode deixar que ninguém aqui vai ter a coragem de usar esse nome."

    "O resto da classe parece estar pensando o mesmo. Todos se encontram calados, com um misto de confusão e vergonha alheia."

    show galdino nobook frown at right

    g "Vou ter que pedir para que voce me entregue esta espada."

    g "Não permitimos armas nesta escola, e provavelmente em nenhuma outra escola."

    f "M-mas... ela é de plástico..."

    show galdino nobook amused

    g "Sendo assim, tudo bem. Mas da próxima, me avise de que ira trazer um brinquedo para a sala."

    f "D-desculpa, professor..."

    "Mas que cena. Normalmente eu acharia graça disso, mas por algum motivo, não consigo."

    # á à ã é ê É í ô ó õ ú ç

label day2:

label day3:

label day4:

label day5:

    return
