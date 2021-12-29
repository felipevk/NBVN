define config.name = _("Academia Novel Brasil")

define f = Character("Fábio", color="#c8ffc8")
define g = Character("Galdino", color="#c8c8ff")
define n = Character("Nebi", color="#c8c8ff")
define n_u = Character("????", color="#c8c8ff")
define f_u = Character("????", color="#c8c8ff")
define g_u = Character("Professor", color="#c8c8ff")
define p = Character("[name]")

default score = 0
default likesBread = False
default drinkChoice = 0
default coffeChoice = 0

label start:

    python:
        name = renpy.input("Digite o seu nome")
        name = name.strip() or "Protagonista"

label day1:

    scene bg classroom
    with fade

    "Dia 1 - Segunda-feira"

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

    n_u "Inclusive, é pra lá que estou indo! Também sou da 1-D. Vem comigo!"

    p "Sério? Que alívio!"

    n_u "Bom, assumindo que o e-mail enviado pela escola esteja correto! Também é a minha primeira vez por aqui."

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

    "A reação da turma é parecida com as reações às outras apresentações até então. Talvez seja melhor desse jeito, sem causar uma impressão negativa."

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

    f_u "Saudações! Podem me chamar de Fábio. Tenho bastante experiência com escrita. Dois meses! Qualquer dúvida que tiverem, podem me perguntar!"

    f "Inclusive, Fábio é o meu nome humano. Caso estejam curiosos, o meu nome real foi selado para conter uma grande ameaça!"

    "Lá vem..."

    f "Peço que nunca usem o meu nome selado, senão um grande mal cairá sobre essa escola! Este nome é..."

    "Se não é pra falar, pra que ele fica insistindo tanto nisso?"

    f "...Earth Makai Destroyer-sama!!"

    "..."

    "Pode deixar que ninguém aqui vai ter a coragem de usar esse nome."

    "O resto da classe parece estar pensando o mesmo. Todos se encontram calados, com um misto de confusão e vergonha alheia."

    show galdino nobook frown at right

    g "Vou ter que pedir para que você me entregue esta espada."

    g "Não permitimos armas nesta escola, e provavelmente em nenhuma outra escola."

    f "M-mas... ela é de plástico..."

    show galdino nobook amused

    g "Sendo assim, tudo bem. Mas da próxima, me avise de que ira trazer um brinquedo para a sala."

    f "D-desculpa, professor..."

    "Mas que cena. Normalmente eu acharia graça disso, mas por algum motivo, não consigo."

    hide fabio

    hide galdino

    "As ultimas introduções ocorrem normalmente. Após o último aluno se apresentar, Galdino se levanta."

    show galdino nobook neutral at center

    g "Agora que todos nos conhecemos, vou falar um pouco sobre o que vocês devem esperar da primeira semana na Academia Novel Brasil."

    g "Iremos abordar os conceitos básicos de webnovels e escrita. Não será necessário nenhum conhecimento prévio sobre estes assuntos, podem ficar tranquilos."

    g "Porém, quero que saibam que estarão sendo avaliados durante este processo. Durante as aulas, farei perguntas sobre os tópicos e espero que me respondam corretamente!"

    "De repente, o ar da sala mudou. Os alunos agora claramente passaram a prestar mais atenção no professor."

    show nebi armsbehind smiling at right

    n "A-avaliação?"

    hide nebi

    show galdino nobook amused

    g "De novo, não espero que ninguém aqui já saiba de tudo. Todas as perguntas serão relativas ao assunto da aula."

    g "Desde que prestem atenção, com certeza se sairão bem."

    show galdino nobook neutral

    g "No final desta semana, vocês receberão meus comentários em relação ao seu desempenho."

    show galdino nobook amused

    g "Alguma pergunta?"

    show galdino nobook neutral

    "Nenhum aluno em particular se pronunciou, mas os murmuros tomam conta da sala."

    "Mal botamos os pés aqui e já estamos sendo avaliados. Bom, acho que é isso que se espera de uma escola deste calibre."

    g "Já que vocês não tem nenhuma pergunta, vamos partir para a nossa primeira aula."

    g "O assunto de hoje é direto ao ponto: Vamos falar sobre {b}o que é uma webnovel.{/b}"

    g "Uma webnovel é simplesmente uma novel, um romance, feita para a internet. Diferente de um livro, os capítulos são lançados separadamente."

    g "Muitas pessoas confundem light novels com webnovels. A maior diferença é no metodo de publicação."

    g "Light novels são publicadas através de editoras, em formato físico. Enquanto que webnovels estão na web, geralmente de forma independente ou não-exclusiva."

    g "Claro, nada impede que um autor de uma webnovel popular seja abordado por uma editora, e a sua obra seja publicada como light novel. Isso ocorre bastante, fora do país"

    g "Quanto às semelhanças, ambas webnovels e light novels apresentam um estilo de escrita menos rebuscado, comparado com romances tradicionais."

    g "O público-alvo destas mídias é de uma faixa etária de jovens, que buscam uma leitura mais acessivel."

    g "Sobretudo com webnovels, que podem ser lidas num celular, acessibilidade é essencial!"

    g "Mantenham em mente que, mesmo que o seu texto pareça curto na tela do computador, ele também precisa ser facilmente lido em uma tela menor de celular."

    g "Perguntas?"

    "Nenhum aluno se pronuncia. Porém, percebo que todos estão claramente concentrados no professor. Alguns estão até fazendo anotacoes, incluindo a Nebi."

    g "Muito bem. Para finalizar a aula de hoje, vamos falar sobre sites brasileiros de webnovels."

    g "Minhas recomendações pessoais são a {a=https://kiniga.com}Kiniga{/a} e a {a=https://novelmania.com.br}Novel Mania{/a}"

    g "Em ambos os sites vocês podem ter acesso a múltiplas obras originais brasileiras, ou até obras internacionais, traduzidas para o português."

    show galdino nobook amused

    g "Vocês também podem postar suas obras nestes sites, desde que sejam bem escritas!"

    show galdino nobook neutral

    g "Agora vamos ver quem estava prestando atenção na aula."

    "Galdino observa os alunos, e seu olhar para na minha direção."

    g "[name], certo?"

    p "S-sim, professor!"

    menu:
        g "Me responda, o que é uma webnovel?"

        "É um romance publicado em bancas.":

            jump q1_a1

        "É uma história publicada na internet, independente de editoras.":

            jump q1_a2

        "São textos feitos fora do brasil que são traduzidos para o português.":

            jump q1_a3

label q1_a1:

    g "A resposta está... incorreta. Como o nome diz, webnovels são postadas na internet."

    jump q2

label q1_a2:

    $ score += 1

    g "A resposta está correta! Essa é uma definição muito importante para vocês, autores."

    g "Entender os elementos do meio que você se encontra é essencial para que se tire o maior proveito possível dele."

    g "O mesmo vale para filmes, jogos, musica, etc. Faça bom uso da mídia, e sua obra terá apenas a ganhar com isso."

    jump q2

label q1_a3:

    g "A resposta está incorreta. webnovels podem ser feitas em qualquer idioma, inclusive em português."

    show galdino nobook amused

    g "Se esse não fosse o caso, pra que estaríamos aqui?"

    show galdino nobook neutral

    jump q2

label q2:

    g "Próxima pergunta!"

    "Tem mais?"

    g "Só mais uma..."

    menu:
        g "Qual a diferença entre webnovels e light novels?"

        "webnovels são publicadas na internet, enquanto que light novels são publicadas fisicamente, por editoras.":

            jump q2_a1

        "Nenhuma.":

            jump q2_a2

        "webnovels são publicadas por editoras, e light novels são independentes.":

            jump q2_a3

label q2_a1:

    $ score += 1

    g "Correto! Que bom que está prestando atenção."

    "Moleza!"

    jump day1_class_end

label q2_a2:

    g "Errado. Muitas pessoas acham que não tem diferença, mas light novels são publicadas por editoras, em bancas e livrarias, enquanto que webnovels estão na... web."

    g "Entendido?"

    p "Entendido..."

    jump day1_class_end

label q2_a3:

    g "Incorreto. Na verdade é o oposto: webnovels são, na sua maioria, independentes; light novels são publicadas por editoras."

    "Verdade..."

    jump day1_class_end

label day1_class_end:

    "O sino bate."

    g "Bom, com isso concluímos a nossa aula. Este é o primeiro passo nas suas jornadas para se tornarem escritores."

    g "Amanhã falaremos um pouco sobre gêneros de webnovels. Tenham um bom descanso, e até a próxima!"

    hide galdino

    "O professor deixa a sala, e os alunos começam a se preparar para sair."

    "Este primeiro dia foi bem interessante. O professor parece entender bem sobre webnovels, enquanto os alunos são bem concentrados."

    "Inclusive, o cansaço tá batendo. Hora de pegar o metrô pra casa."

    scene bg classroom
    with fade

    "Antes de voltar para o dormitório, decido fazer umas compras para a semana."

    "O lado bom de ter me perdido de manhã foi que encontrei este supermercado que fica no caminho para a escola."

    "Não tenho o costume de cozinhar, mas fica bem mais em conta do que comer fora, ou pedir delivery."

    "Assim que termino de comprar tudo que preciso, retomo o caminho pra casa."

    scene bg kitchen
    with fade

    "Este é o dormitório que irei ficar durante a escola. Ele foi feito para estudantes de fora desta cidade."

    "Acredito que a maioria do pessoal que está aqui são de outras escolas, já que não vi ninguém pegando o mesmo caminho que eu peguei para a Novel Brasil."

    "Me dirijo a geladeira da cozinha. Cada um tem um espaço reservado nela. Coloco as compras que fiz na minha prateleira."

    "Quando termino de arrumar, percebo que ainda sobrou uma prateleira vazia. Acho isso meio estranho, pois tenho certeza de que este lugar estava sem vagas após a minha inscrição."

    "Bom, tanto faz. Pego o que vou jantar, e como lá mesmo na cozinha."

    "Ao terminar de comer, decido subir para o meu quarto. Mas antes que eu possa sair da cozinha, uma figura familiar surge."

    show fabio sheathed smug at center

    f "!!"

    p "Hum? Você não é o... Fábio?"

    f "O Próprio! Fez bem em não usar o meu nome selado, hehehe!"

    "Nunca que vou falar um nome ridículo daqueles! Deve ser por isso que foi selado."

    p "É… Pode deixar."

    f "E você se chama [name], certo?"

    p "Isso."

    "Estou surpreso que ele se lembrou do meu nome."

    f "E aí?"

    p "O que?"

    f "O que você já escreveu? Me mostre aí!"

    p "Ah! Eu não tenho nada aqui comigo..."

    f "Nada? Que chato, hein?"

    p "Bom, ainda quero aprender mais nas aulas. Daí eu vejo de escrever algo. Aliás, você disse que já escreve a dois meses, certo?"

    f "Isso! Já evoluí bastante nesse tempo! Me considero um autor de rank S, ou pelo menos rank A!"

    p "Como assim? O que isso significa?"

    "Fabio pára por um momento para pensar na minha pergunta."

    f "Não importa! O que importa é que você tem muito a aprender comigo! Além de escrever, também já assisti e analisei centenas de animes!"

    p "Ah, é? Também curto animes!"

    "Espero que ele seja menos chato sobre isso"

    f "Qual o tamanho do seu MyAnimeList?"

    p "Hum? Ah, aquele site pra catalogar o que você assistiu? Nunca usei ele."

    f "Como assim? E se considera um otaku? Qual é a sua waifu? Não me diga que é a..."

    p "Já tá meio tarde, né? A viagem pra cá também foi meio cansativa, então acho que to indo dormir. Até mais!"

    f "Até..."

    scene bg bedroom night
    with fade

    "Enfim, estou no meu quarto."

    "Apesar de ter usado isso como desculpa pra fugir, este dia realmente foi cheio."

    "Uma nova cidade. Uma nova escola. webnovels. Colegas de sala peculiares..."

    "Será que eu vou dar conta de escrever minha própria história? Pra falar a verdade, não sei bem sobre o que eu gostaria de escrever."

    "Bom, as aulas acabaram de começar. Acho que tenho tempo suficiente pra decidir isso. Agora vou dormir."

label day2:
    scene bg classroom
    with fade

    "Dia 2 - Terça-feira"

    show galdino nobook neutral at center

    g "Quero que me respondam: O que vocês gostariam de escrever?"

    "O que???"

    g "Estamos em uma academia de escritores, eventualmente vocês irão escrever webnovels. Talvez alguns até já tenham começado."

    g "Levante a mão caso você já esteja escrevendo algo."

    "Cerca de cinco ou seis pessoas levantaram a mão, incluindo o Fábio."

    g "Agora levante a mão caso você já tenha uma ideia para a sua história."

    "Desta vez, muitos outros ergueram suas mãos. Acho que mais da metade da sala já sabe sobre o que quer escrever."

    g "Muito bem. A aula de hoje será sobre tipos de webnovels. Abordaremos alguns dos mais populares, e discutiremos o porque de serem tão populares."

    g "Para os escritores que ainda não se sabem sobre o que querem escrever, espero que essa aula sirva de incentivo para vocês."

    g "Vamos começar deixando uma coisa clara: webnovels podem ter os mesmos gêneros de quaisquer outras obras de ficção."

    g "Ação, aventura, fantasia, romance, terror, comédia, drama, sci-fi. webnovels ainda podem ter características de todos estes grupos."

    g "Porém, ao longo dos anos, certos sub-gêneros passaram a aparecer mais e mais entre as webnovels mais populares."

    g "Um exemplo perfeito são as obras de {b}isekai{/b}."

    g "webnovels de Isekai são aquelas onde o protagonista, geralmente uma pessoa de um mundo normal, é transportada ou reencarnada em um mundo de fantasia."

    g "Os poderes do protagonista dependem de cada autor."

    g "Em algumas obras, ele pode renascer exatamente como estava no mundo real, ou seja, sem nenhum poder especial. Ou então ele pode ser tão ou mais poderoso do que os seres deste mundo."

    g "Isekai é claramente derivado de histórias de fantasia. A maior vantagem narrativa deste sub-gênero é a facilidade que o autor tem para apresentar o seu mundo para o leitor."

    show nebi armsbehind smiling at left

    n "Como assim, professor?"

    hide nebi

    g "Digamos que eu esteja escrevendo uma história de fantasia. Nesta história, eu tenho um mundo completamente diferente do mundo real, onde o protagonista nasceu e viveu."

    g "Digamos que neste mundo, a chuva é verde devido ao excesso de um certo elemento químico no ar. Como eu poderia apresentar esta informação para o leitor?"

    g "Talvez eu possa criar uma cena onde algum cidadão pergunta para o protagonista sobre o fenômeno... Mas será que isso seria certo?"

    "Alguns alunos começam a murmurar."

    g "Eu estabeleci que esta chuva ocorre normalmente neste mundo. Então pra que o protagonista precisaria explicar isso para alguém deste mundo? Não faz muito sentido, concordam?"

    g "Já em histórias de isekai, nós temos um personagem que ainda está se habituando com o mundo à sua volta, exatamente como o leitor!"

    g "Faz todo o sentido que coisas comuns daquele lugar precisem ser explicadas para o protagonista, e por consequência, para o leitor."

    "Após a explicação, Galdino vai a sua mesa e toma um copo d'água. Ao terminar, ele retoma a aula."

    g "O próximo sub-gênero que iremos abordar é o de {b}sistema{/b}."

    g "Histórias de sistemas são aquelas em que as regras, o sistema de poder, é claramente definido para os personagens e para o leitor."

    g "Mas o que isso significa? Primeiro, precisamos entender o que são sistemas de poderes."

    g "Sistemas de poderes estão presentes em diversos meios. É um conjunto de regras que dita o que pode e o que não pode ser feito com os poderes e habilidades do mundo onde se passa a obra."

    g "Por exemplo, em uma história de magos, geralmente o autor tem em mente como uma magia pode ser feita, quais são suas limitações, e o que não pode ser resolvido com magia."

    g "Um sistema de poder pode ser algo que apenas o autor esteja ciente, ou pode ser exposto para o leitor. Contudo, uma vez que esteja definido, o autor precisa mantê-lo consistente durante a obra."

    g "Mesmo que o autor não aborde o sistema em detalhes durante a história, falhar em seguí-lo pode causar inconsistências na narrativa, e potencialmente frustar quem estiver lendo."

    g "No caso de histórias de sistemas, as regras e mecânicas estão explicitamente expostas para o leitor e para o personagem principal. "

    g "Geralmente, mas não sempre, estas histórias se passam em um mundo com mecânicas similares a um videogame. O protagonista e outros personagens podem ter acesso a um menu com seus atributos, poder, pontos de vida, etc."

    g "Existem pessoas que se interessam em entender os mínimos detalhes de uma habilidade, ao ponto de querer saber até os valores numéricos envolvidos no cálculo de dano. Estes serão os seus leitores mais fiéis."

    g "Tendo dito tudo isso, lhes pergunto: É permitido quebrar as regras, em uma história de sistema?"

    "A classe começa a debater entre si. A maioria das pessoas parece acreditar que não. Eu não tenho muita certeza."

    g "Sim, você pode. Porém, caso faça, é bom que tenha um motivo muito convincente para isso! Senão seus leitores podem achar que você estava apenas sendo preguiçoso e procurando um atalho para continuar a história!"

    g "Então tenham muito cuidado ao fazerem isso. Mas saibam que, sim, é possível."

    g "E pra finalizar o assunto desta aula, falarei sobre histórias de {b}cultivo{/b}."

    g "Quem aqui conhece ou já leu uma novel de cultivo?"

    "A maioria dos alunos levanta a mão."

    g "E quem aqui pode me explicar o que é uma história de cultivo?"

    "Todas as mãos se abaixaram."

    g "Pois bem. O cultivo é um modelo de narrativa muito visto em webnovels chinesas. Esse tipo de novel se foca na {b}fantasia de progressão{/b}."

    g "No cultivo, vocês verão o protagonista evoluir constantemente. Mas essa evolução geralmente segue conceitos de filosofia orientais, principalmente taoísta "

    g "No modelo \"ocidental\", o crescimento geralmente ocorre ao se interagir com o ambiente externo. Ao derrotar inimigos, ou realizar missões."

    g "Já no cultivo, o crescimento ocorre de forma interna, através do aperfeiçoamento de seu corpo e de sua alma. Se tornar mais forte com meditação, ao ponto de se alcançar a imortalidade, é algo relativamente comum neste meio."

    g "Artes marciais e conflitos envolvendo deuses também são recorrentes. Neste tipo de novel, os leitores desejam ver o protagonista sempre tornando-se mais e mais forte."

    show fabio sheathed smug at left

    f "Cultivo é brabo demais! Hehehe!"

    hide fabio

    g "Muito bem. Agora que falamos dos sub-gêneros mais populares, vamos para as perguntas!"

    g "[name]! Gostaria de responder essa?"

    p "Claro!"

    menu:
        g "O que é uma webnovel de sistema?"

        "É uma história onde o protagonista vai para outro mundo.":

            jump q3_a1

        "São webnovels onde o sistema de regras e poderes é mostrado para o leitor.":

            jump q3_a2

        "São histórias de romance com várias garotas afim de um rapaz.":

            jump q3_a3

label q3_a1:

    g "Incorreto. Estas são histórias de isekai."

    g "webnovels de sistema ocorrem quando o protagonista está completamente ciente das regras e mecânicas dos poderes do mundo da história."

    jump q4

label q3_a2:

    $ score += 1

    g "Correto!"

    g "Em histórias de sistema, vocês verão o protagonista acessando suas informações de forma semelhante a um jogador de rpg."

    jump q4

label q3_a3:

    g "Incorreto. Estas são histórias de harém."

    g "webnovels de sistema ocorrem quando o protagonista está completamente ciente das regras e mecânicas dos poderes do mundo da história."

    jump q4

label q4:

    g "Próxima pergunta!"

    menu:
        g "Qual destas alternativas melhor descreve uma história de isekai?"

        "São webnovels onde o personagem principal evoluí através de meditação.":

            jump q4_a1

        "É quando o protagonista se torna super poderoso.":

            jump q4_a2

        "São histórias onde o protagonista é transportado para um mundo alternativo.":

            jump q4_a3

label q4_a1:

    g "Errado. Talvez você esteja pensando em webnovels de cultivo."

    g "Em isekais, o protagonista certamente pode evoluir. Mas o conceito principal deste sub-gênero é o de que o personagem principal é transportado para um mundo diferente do seu."

    g "A partir desta premissa, se o protagonista evoluirá ou não, depende do autor."

    jump q5

label q4_a2:

    g "Incorreto."

    g "Enquanto que é verdade que muitos protagonistas de isekais eventualmente se tornam super poderosos, esta não é uma característica essencial."

    g "Em muitas obras de isekai, o personagem principal mantém as mesmas capacidades físicas de quando estava no mundo real, resolvendo problemas usando sua inteligência ou criatividade."

    g "O conceito principal do isekai é o de uma pessoa que foi transportada para um mundo diferente do seu, e aprendendo a viver neste mundo."

    jump q5

label q4_a3:

    $ score += 1

    g "Correto!"

    g "Este sub-gênero também é popular em animes e light novels. A maior vantagem de isekais está na facilidade de introduzir conceitos de um mundo novo, tanto para o protagonista quanto para o leitor."

    jump q5

label q5:

    g "Agora, para a última pergunta..."

    menu:
        g "Como você define uma webnovel de cultivo?"

        "São webnovels chinesas.":

            jump q5_a1

        "É uma história que se passa em um videogame.":

            jump q5_a2

        "São histórias onde o protagonista constantemente evoluí seu corpo e espírito.":

            jump q5_a3

label q5_a1:

    g "Incorreto."

    g "Apenas ser chinesa não categoriza uma obra como cultivo."

    g "Obras de cultivo se tratam de fantasias de progressão, onde o personagem principal busca o aperfeiçoamento de corpo e alma, em muitos casos alcançando a imortalidade."

    g "O desenvolvimento do personagem segue um modelo de progressão oriental, muito visto em novels chinesas, mas atualmente existem diversas webnovels de cultivo que não são chinesas."

    jump day2_classend

label q5_a2:

    g "Incorreto."

    g "Obras de cultivo se tratam de fantasias de progressão, onde o personagem principal busca o aperfeiçoamento de corpo e alma, em muitos casos alcançando a imortalidade."

    g "Histórias de cultivo podem se passar em um videogame, mas isto não é o suficiente para definir o gênero."

    jump day2_classend

label q5_a3:

    $ score += 1

    g "Resposta correta!"

    g "webnovels de cultivo são perfeitas para leitores que gostam de acompanhar o crescimento de um personagem. A diferença de poder entre o protagonista no começo e no final da obra são gritantes."

    g "Contudo, uma crítica comum a este gênero é a constante repetição do ritmo. Alguns leitores podem achar obras de cultivo, especialmente as mais longas, entediantes e não muito criativas."

    show fabio sheathed smug at left

    f "Hunf! Bando de nerds!"

    hide fabio

    jump day2_classend

label day2_classend:

    g "E com isso, terminamos nossa segunda aula. "

    g "Certamente existem outros sub-gêneros, mas esta aula ficaria muito longa se falássemos de todos."

    g "Temos harém, dungeon attack, mmo's, realidade virtual, slice of life, e muitos outros."

    g "Sugiro que, quando forem ler suas webnovels favoritas, prestem atenção nas tags as quais elas pertencem. Procurem por outras histórias com a mesma tag, e tentem identificar os elementos em comum entre elas."

    g "Que fique de tarefa de casa para a turma. Obrigado, e tenham uma boa tarde!"

    hide galdino

label day2_afterclass:
    "Os alunos começam a se arrumar para sair. Antes que Galdino saia da sala, me dirijo a ele."

    p "Com licença, professor?"

    show galdino nobook neutral at center

    g "Alguma dúvida, [name]?"

    p "Sim. Sobre o que o senhor falou no começo da aula..."

    "Pouco a pouco os alunos saem da sala. Ao final da minha frase, a maioria das pessoas já se retiraram."

    p "Pra falar a verdade, mesmo gostando de ler webnovels, eu não faço a mínima ideia sobre que tipo de história eu quero escrever."

    "Enquanto eu falo, o professor me observa com atenção, como um médico escutando um paciente falando de seus sintomas."

    p "Mas eu ainda quero escrever uma história! Eu só não sei sobre o que..."

    p "Por acaso o senhor teria uma dica a respeito disso?"

    "O professor está pensativo. Talvez minha pergunta tenha sido muito vaga? Ou talvez ele esteja incomodado por eu estar tirando dúvidas após o horário da aula."

    g "[name], por acaso você conhece o parque municipal?"

    p "Parque? Hum... Não. Na verdade eu me mudei ontem pra cá"

    g "Perfeito. Então esta é a minha dica pra você."

    p "Qual?"

    g "Vá visitar o parque. Dar uma caminhada. Respirar um ar puro."

    p "Ué, mas pra que?"

    g "Você parece estar com muitos pensamentos na cabeça. Alguns ajudam, outros nem tanto. Por isso a minha recomendação é que você vá dar uma volta pra espairecer."

    p "Mas e a minha novel? Eu queria começar o quanto antes."

    g "Por enquanto, o seu foco é limpar a cabeça. É o que faço quando tenho dificuldades. E acredite, acontece bastante!"

    p "Sério? Bom, se o senhor tá falando..."

    g "Depois que fizer isso, a gente conversa, ok?"

    p "Ok!"

    g "Até amanhã, [name]!"

    hide galdino

    "Bom, ainda não entendi exatamente como isso vai me ajudar, mas não custa nada tentar. Decido ir visitar o parque após o almoço."

    scene bg classroom
    with fade

    "Este é o parque municipal que o professor Galdino mencionou."

    "Ele fica meio perto da escola, então foi fácil chegar nele. Nenhum ponto em especial se destaca, mas o local como um todo parece ser muito bem cuidado."

    "Definitivamente é bom ter um pouco de contato com a natureza, estando no meio de uma cidade grande. O ar daqui parece mais leve e pacífico."

    "Como estamos em um dia de semana, não vejo muitas pessoas por aqui. Uma senhora idosa está sentada em um banco, um casal andando de mãos dadas próximo ao jardim, e..."

    p "Nebi?"

    n "Hum?"

    show nebi armsbehind smiling at center

    menu:
        n "Ah! Olá!"

        "Lembra de mim? Meu nome é [name].":

            jump nebi_greeting

        "Você me ajudou quando eu não conseguia encontrar a sala.":

            jump nebi_greeting

        "Não vai me dizer que já se esqueceu do meu rosto...":

            jump nebi_greeting

label nebi_greeting:

    n "Claro que lembro de você, [name]!"

if likesBread:
    jump nebi_remembers_bread
else:
    jump nebi_park_continue

label nebi_remembers_bread:

    n "Você gosta de pão, né? Hihihi!"

    p "É..."

    "Não vão se esquecer disso tão cedo..."

    jump nebi_park_continue

label nebi_park_continue:

    n "Você também veio conhecer o parque?"

    p "Sim! Me falaram bem daqui, então resolvi vir e conferir."

    n "Quer dar uma volta comigo, então?"

    p "Claro!"

    hide nebi

    "Me junto à Nebi e começamos a passear pelo parque."

    "Após uns vinte minutos, percebo que a atmosfera tranquila do local acabou fazendo com que a gente só andasse sem falar quase nada."

    "Talvez a essa altura seria bom puxar algum assunto com ela."

    menu:
        "O que eu faço?"

        "Falo de alguma coisa para quebrar o gelo":

            jump try_talk

        "Continuo sem falar nada":

            jump keep_quiet

label try_talk:

    p "Então, Nebi, você é nova por aqui?"

    show nebi armsbehind smiling at center

    n "Sou sim! Vim do interior do estado, de uma cidadezinha que fica a umas quatro horas daqui."

    jump question_city

label keep_quiet:

    "Decido não falar nada por enquanto. Melhor não forçar conversa e soar esquisito."

    n "Hum... "

    show nebi armsbehind smiling at center

    n "Então, [name], você também se mudou pra cá recentemente?"

    p "Hum? Ah, sim! Hoje é só o meu segundo dia aqui."

    jump question_city

label question_city:

    menu:
        n "E de onde você veio?"

        "De outra cidade, parecida com essa.":

            n "Então você deve se sentir à vontade por aqui! Eu ainda estou me acostumando com cidades grandes..."

        "De uma cidade pequena, em outro estado.":

            n "É mesmo? Deve ser cansativo vir de outro estado e ter aula no mesmo dia, não?"

            p "Foi um pouco, sim. Mas hoje já estou ok!"

        "Também vim do interior do estado.":

            n "Que legal! E fica longe daqui?"

            p "Não muito longe. Duas horas, ou menos."

    p "E o que está achando da Novel Brasil?"

    n "Bom, ainda é meio cedo pra ter uma opinião forte, mas por enquanto está sendo muito divertido!"

    n "Eu nunca achei que um dia iria assistir um professor em uma sala de aula falando sobre as novels que eu leio na internet!"

    n "É muito legal ver este meio sendo valorizado. Como o professor Velasco disse, ainda existem poucas webnovels brasileiras, se comparado as outros países."

    p "E você costuma ler novels em outros idiomas?"

    n "Eu arranho um pouco no inglês, então já li algumas. Mas nada se compara a ler algo na nossa língua materna!"

    n "Por isso eu acho o máximo que a Novel Brasil ajude tantos escritores a começar."

    n "E eu mal posso esperar pra ter uma obra minha publicada e lida por várias outras pessoas!"

    p "Eu também! Aliás, sobre o que você vai escrever?"

    "Ao ouvir a minha pergunta, Nebi rapidamente vira a sua atenção para uns patos que estão na lagoa."

    n "Olha só esses patinhos fofinhos! Será que consigo chegar perto deles?"

    p "Acho que não..."

    hide nebi

    "Nebi se dirige à lagoa com um andar levemente desajeitado. Corro atrás dela, pra me certificar que ela não caia na água."

    scene bg classroom
    with fade

    "O passeio inteiro pelo parque leva algumas horas. Após isso, nos dirigimos para a entrada."

    show nebi armsbehind smiling at center

    n "Eu não fazia ideia de que esse lugar era tão grande! Não esperava encontrar tanta natureza por aqui."

    p "Realmente, por um momento esqueci que estávamos em uma cidade grande."

    n "Pra falar a verdade, eu nem notei o tempo passando. Já está na minha hora!"

    n "Obrigado por me acompanhar hoje! Te vejo amanhã, na escola?"

    p "Sim, nos vemos amanhã!"

    hide nebi

    "Após nos despedirmos, vou até a estação do metrô."

    scene bg classroom
    with fade

    "Foi uma surpresa ter encontrado a Nebi no parque. No começo me senti um pouco de receio de não conseguir conversar com ela, mas ela acabou se mostrando ser uma pessoa bem tranquila."

    "Acabei não pegando nenhuma rede social dela, mas espero que a gente continue se falando."

    "E o passeio realmente ajudou a acalmar um pouco a minha mente. Talvez isso venha em parte pelo atividade fisica, e em parte de ter conversado com a Nebi."

    "Continuo sem nenhuma ideia para uma história, mas tenho a sensacao de vai ficar tudo bem."

    "Sim. Vai ficar tudo bem."

    jump day3

label day3:

    scene bg classroom
    with fade

    "Dia 3 - Quarta-feira"

    show galdino nobook neutral at center

    g "Bom dia a todos!"

    g "Espero que a aula de ontem tenham lhe deixado com vontade de escrever, pois faremos um pouco disso hoje!"

    g "Para começarmos, vou precisar de dois voluntários. Alguém está disposto a me ajudar?"

    "Algumas mãos se erguem."

    g "Vamos ver... Fábio e Nebi."

    g "Gostaria que ambos escrevessem uma breve cena de diálogo entre dois personagens: Um mecânico e um cliente tendo seu carro consertado. O mecânico irá falar o preço do conserto, o cliente tentará pechinchar, mas o mecânico não aceitará a proposta."

    g "Basta que o trecho tenha três ou quatro falas. Ok?"

    show nebi armsbehind smiling at left

    show fabio sheathed smug at right

    n "C-certo!"

    f "Moleza!"

    "Os dois imediamente começam a escrever."

    hide nebi

    hide fabio

    g "Enquanto isso, vamos iniciar uma conversa sobre discursos em narrativas."

    g "Na língua portuguesa, existem dois tipos de discursos: Direto e indireto."

    "Enquanto fala, Galdino se levanta em direção a lousa para escrever algo."

    g "O discurso direto é a reprodução exata da fala de um personagem. Este é o discurso mais comumente utilizado em narrativas, sobretudo webnovels."

    g "Este é um exemplo de discurso direto."

    "Galdino termina de escrever e dá um passo pro lado, revelando o que escreveu no quadro."

    "{i}— Eu sou inocente, meritíssimo — afirmou o jovem na cadeira do réu.{/i}"

    g "O outro tipo de discurso é o indireto. No discurso indireto, o narrador usa as próprias palavras para contar o que foi dito pelo personagem."

    "Galdino volta a escrever enquanto fala."

    g "O discurso direto soa como se o narrador estivesse realmente relatando o que aconteceu para outra pessoa."

    g "Como podem ver aqui."

    "{i}O jovem na cadeira do réu afirmou para o juiz que era inocente.{/i}"

    g "Como estão indo, Nebi e Fábio?"

    "Fábio se levanta rapidamente."

    show fabio sheathed smug at right

    f "Acabei!"

    show nebi armsbehind smiling at left

    p "Aqui também!"

    g "Excelente. Vamos ver o trecho do Fábio."

    "{i}O mecânico disse \"O preço, é duzentos reais.\", daí o cliente respondeu: \"Que caro! Pode fazer 100?\" e o mecânico falou não...{/i}"

    "Galdino fica pensativo por um minuto."

    g "Posso comentar sobre o que escreveu, Fábio?"

    f "Claro, professor! Curtiu?"

    g "Existem diversos problemas com os discursos neste texto. Os dois primeiros discursos são diretos, mas não estão usando o travessão."

    g "O discurso direto com aspas é comum em narrativas em inglês, mas para português é preferível que se use o travessão."

    "Galdino mais uma vez se dirige ao quadro para escrever."

    g "Aqui está uma versão com os discursos corrigidos. Também tomei a liberdade de corrigir outros erros."

    "{i}— O preço é duzentos reais — disse o mecânico.\n— Que caro! Pode fazer por cem?\n— Não — respondeu o mecânico, enquanto soltava um suspiro.{/i}"

    g "Como podem ver, também alterei a resposta do mecânico para um discurso direto."

    g "Na versão original, o discurso indireto terminava em três pontos, o que deixava incerto se isso fazia parte da reação do mecânico ou se foi uma colocação do narrador."

    g "Para simplificar, transformei os três pontos em um suspiro do mecânico."

    f "Hunf! Estava quase tudo certo!"

    g "Agora vamos ver o trecho da Nebi."

    hide fabio

    "Nebi está claramente ansiosa. Eu também estaria, depois dessa."

    "Galdino reproduz o texto de Nebi no quadro."

    "{i}— Aqui está o preço do serviço. 1000 reais. — Disse o mecânico.\n— Absurdo! Isso tá muito caro. Não podemos negociar um valor mais interessante para nós dois?\nO mecânico respondeu: — Infelizmente, nossos preços são fixos no país inteiro.{/i}"

    g "Hum..."

    g "Esta versão é melhor. Mas ainda não segue completamente a norma."

    g "Alguém aqui conhece o {b}verbo dicendi{/b}?"

    "A turma começa a murmurar. Parece que ninguém está confiante o suficiente para responder o professor."

    "Galdino retorna ao texto de Nebi e sublinha algumas palavras."

    "{i}— Aqui está o preço do serviço. 1000 reais. — {u}Disse{/u} o mecânico.\n— Absurdo! Isso tá muito caro. Não podemos negociar um valor mais interessante para nós dois?\nO mecânico {u}respondeu{/u}: — Infelizmente, nossos preços são fixos no país inteiro.{/i}"

    g "Verbos dicendi indicam o modo que o locutor se expressou durante o discurso direto. "

    g "Dicendi vem do latim, e significa \"dizer\". Também são conhecidos como {b}verbos de elocução{/b} ou {b}declaração{/b}."

    g "Outros exemplos de verbos dicendi incluem: Perguntar, contestar, concordar, exclamar, pedir, ordenar, entre outros."

    g "Porém, a Nebi cometeu um erro ao usar o dicendi. O verbo dicendi usado após o fala é considerado parte do mesmo período. Isso significa que a fala não é pontuada, e o dicendi é escrito com letra minúscula."

    g "O primeiro discurso pode ser corrigido assim:"

    "{i}— Aqui está o preço do serviço. 1000 reais — disse o mecânico.{/i}"

    n "Oh! Não fazia ideia disso!"

    g "Percebem a diferença? Pode até parecer meio esquisito, mas esta é a norma."

    g "Uma coisa importante a se notar é que se o trecho narrativo não começar com o verbo dicendi, o discurso deve ser pontuado, e o trecho narrativo deve ser iniciado com letra maiúscula."

    g "Um exemplo disso seria:"

    "{i}— Aqui está o preço do serviço. 1000 reais. — O mecânico disso ao cliente.{/i}"

    g "Outra coisa que notei no texto da Nebi foi o uso do narrador para introduzir a última fala do mecânico."

    "{i}O mecânico respondeu: — Infelizmente, nossos preços são fixos no país inteiro.{/i}"

    g "Isto não está errado. Mas é incomum de se ver."

    g "Isso é chamado de {b}discurso direto normatizado{/b}. Quando o parágrafo começa com o discurso seguido da narração, no caso do primeiro parágrafo, este é chamado de {b}discurso direto convencionado{/b}."

    g "Por enquanto, minha recomendação é de que você evite este formato. Este trecho poderia ser reescrito da seguinte forma:"

    "{i}— Infelizmente, nossos preços são fixos no país inteiro — respondeu o mecânico.{/i}"

    n "Entendi! Obrigado pela correção, professor!"

    hide nebi

    g "Outra forma de usar o travessão é quando o narrador insere uma informação no meio do discurso direto."

    g "Veja este exemplo:"

    "{i}— Seu poder é incomparável — exclamou o guerreiro, ofegante — e não acredito que ninguém aqui será capaz de detê-lo!{/i}"

    g "Como podem ver, nem mesmo o trecho de narração é pontuado, já que ainda nos encontramos no mesmo período."

    g "A segunda oração é uma oração subordinada à primeira, portanto sendo parte do mesmo período."

    g "Caso a continuação do discurso seja outro período, o trecho narrativo deve ser pontuado. Vejamos outro exemplo."

    "{i}— Não temam, cidadãos — afirmou José. — A ajuda está a caminho!{/i}"

    g "Estamos entendidos? Para mais detalhes neste assunto, recomendo dois artigos do grimório do escritor: Um sobre o {a=https://grimorioescritor.blogspot.com/2021/03/aspas-dois-pontos-ou-hifen-nao-use.html}uso do travessão{/a}. e outro sobre o {a=https://grimorioescritor.blogspot.com/2021/09/dicendi-que-mane-dicendi.html}verbo dicendi{/a}"

    g "Agora vamos para as perguntas! [name]!"

    p "Aqui!"

    menu:
        g "Qual é o símbolo mais recomendado para ser usado no discurso direto?"

        "Travessão.":

            jump q6_a1

        "Aspas.":

            jump q6_a2

        "Ponto e vírgula.":

            jump q6_a3

label q6_a1:

    $ score += 1

    g "Correto! Vocês se surpreenderiam com a quantidade de obras que são recusadas em sites de webnovels por não utilizarem travessão nos diálogos."

    show fabio sheathed smug at right

    f "Então deve ser por isso..."

    hide fabio

    jump q7

label q6_a2:

    g "Errado. Para webnovels, aspas são melhores utilizadas para expressar pensamentos, ou servir como uma citação. Um exemplo disso seria quando o narrador descreve os conteúdos de um bilhete."

    g "Em vez de aspas, a melhor recomendação é que se use o travessão."

    jump q7

label q6_a3:

    g "Errado. Para webnovels, a melhor recomendação é que se use o travessão."

    jump q7

label q7:

    g "Próxima pergunta..."

    menu:
        g "O que é o verbo dicendi?"

        "É um verbo intransitivo.":

            jump q7_a1

        "São verbos em terceira pessoa.":

            jump q7_a2

        "É o verbo que indica como um personagem expressou a sua fala.":

            jump q7_a3

label q7_a1:

    g "Incorreto."

    g "O verbo dicendi indica o modo que o discurso foi emitido. A fala de um personagem pode ter sido {i}dita{/i}, {i}perguntada{/i} , {i}exclamada{/i}, {i}explicada{/i} ou vocalizada de outra forma."

    jump q8

label q7_a2:

    g "Incorreto."

    g "O verbo dicendi indica o modo que o discurso foi emitido. A fala de um personagem pode ter sido {i}dita{/i}, {i}perguntada{/i} , {i}exclamada{/i}, {i}explicada{/i} ou vocalizada de outra forma."

    jump q8

label q7_a3:

    $ score += 1

    g "Correto. O entendimento do verbo dicendi é essencial para se criar diálogos claros de serem lidos. E diálogos são o coração das webnovels."

    jump q8

label q8:

    g "Agora, vamos para a última pergunta do dia."

    menu:
        g "Como é feita a pontuação quando o verbo dicendi segue o discurso direto?"

        "Discurso direto é pontuado e narração começa com letra maiúscula.":

            jump q8_a1

        "Discurso direto começa em primeira pessoa e narração começa com letra maiúscula.":

            jump q8_a2

        "Discurso direto não é pontuado e o trecho narrativo começa com letra minúscula.":

            jump q8_a3

label q8_a1:

    g "Incorreto."

    g "Quando o discurso direto é seguido de um trecho narrativo que se inicia com o verbo dicendi, o discurso não é pontuado e o trecho narrativo com o verbo dicendi começa com letra maiúscula."

    g "Isso se dá ao fato que ambos pertencem ao mesmo período."

    g "Mas é importante notar que caso o trecho narrativo não se inicie com o dicendi, o discurso é pontuado e o trecho narrativo começa em maiúsculo"

    jump day3_classend

label q8_a2:

    g "Incorreto."

    g "Quando o discurso direto é seguido de um trecho narrativo que se inicia com o verbo dicendi, o discurso não é pontuado e o trecho narrativo com o verbo dicendi começa com letra maiúscula."

    g "Isso se dá ao fato que ambos pertencem ao mesmo período."

    g "Mas é importante notar que caso o trecho narrativo não se inicie com o dicendi, o discurso é pontuado e o trecho narrativo começa em maiúsculo"

    jump day3_classend

label q8_a3:

    # score += 1

    g "Correto!"

    g "Mas é importante notar que caso o trecho narrativo não se inicie com o dicendi, o discurso é pontuado e o trecho narrativo começa em maiúsculo"

    jump day3_classend

label day3_classend:

    g "E isso concluí nossa aula sobre discurso direto para webnovels!"

    g "Não se preocupem caso não entendam isso imediatamente. Continuem estudando artigos sobre o assunto, e colocando em prática, e eventualmente conseguirão seguir a norma de forma natural."

    g "Classe dispensada!"

label day3_afterclass:

    scene bg classroom
    with fade

    "Ao sair da sala, vejo alguns dos alunos no corredor, conversando entre si. Nebi também se encontra no corredor, mas ela não parece estar esperando alguém."

    "Assim que ela me vê, ela vem em minha direção."

    show nebi armsbehind smiling at center

    n "[name]! Vamos visitar outro lugar hoje?"

    "A pergunta súbita me pega de surpresa."

    p "Hum, o que? Agora?"

    "Nebi sacode a cabeça positivamente."

    n "Se estiver livre, claro!"

    p "Estou, sim. Mas pra onde vamos?"

    n "É segredo! Hihi!"

    p "Ok, agora quero saber... Aceito o convite!"

    n "Então vamos! Serei sua guia mais uma vez."

    hide nebi

    "E pensar que ambos somos novos na cidade. Ela já parece estar totalmente à vontade."

    scene bg classroom
    with fade

    "Após uma curta viagem de ônibus, e alguns minutos andando, parece que chegamos no nosso destino: Café Memoria."

    "É fácil de perceber a empolgação estampada na cara da Nebi. Talvez este tipo de estabelecimento não seja comum pra ela."

    show nebi armsbehind smiling at center

    n "Caraca! É bem maior do que eu imaginava!"

    p "O que te fez escolher esse café em especial?"

    n "É o que tem as melhores notas da região. Fiz uma pesquisa na noite passada."

    p "Realmente se preparou, hein?"

    n "É claro! Afinal, é aqui que encontraremos a arma secreta para nos tornarmos grandes escritores!"

    p "Como assim? Arma secreta?"

    n "Vamos entrar, [name]?"

    hide nebi

    p "Espera aí!"

    scene bg classroom
    with fade

    "Ao entrar no local, consigo sentir uma atmosfera relaxante e convidativa. Realmente parece fazer jus ao título de café mais bem avaliado."

    "O lugar possui alguns fregueses. Alguns estão bebendo de suas xícaras enquanto conversam, e outros estão comendo. Ninguém parece estar com pressa de ir para outro canto."

    "Vejo que Nebi já está se dirigindo a uma das mesas vazias. Apresso o passo para me juntar a ela."

    show nebi armsbehind smiling at center

    n "O que você vai pedir?"

    p "Deixa eu ver o menu..."

    "Começo a folhear o cardápio. Os preços são até que generosos para um lugar arrumadinho assim. Além de vários tipos de café, eles também tem doces, salgados, e outras bebidas."

    menu:
        p "Acho que vou só pegar algo pra beber."

        "Suco de laranja.":

            $ drinkChoice = 0

        "Milkshake.":

            $ drinkChoice = 1

        "Chá de boldo.":

            $ drinkChoice = 2

    "Assim que decido o que pedir, o garçom aparece. Olho para a Nebi, mas ela ainda está tentando escolher algo."

    n "Er... Eu vou querer..."

    n "Um café! E dois pães de queijo!"

    n "É assim que se pede café? Desculpa, é que eu nunca tomei!"

    p "Bom, geralmente você pede para que coloquem algo..."

    menu:
        n "O que eu coloco? Alguma sugestão?"

        "Leite.":

            $ coffeChoice = 0

        "Açúcar.":

            $ coffeChoice = 1

        "Vai puro, mesmo.":

            $ coffeChoice = 2

    n "Ok! Vou seguir a sua sugestão."

    "O garçom anota nossos pedidos e se retira. Agora é a hora perfeita para matar a minha curiosidade."

    p "Agora me conta, Nebi. Qual é a arma secreta que você tava falando?"

    n "É o café!"

    p "Café? Mas por que?"

    n "Uma fonte confiável me disse que os maiores escritores começam seu dia com uma xícara de café, para ativarem seus neurônios e se manterem criativos durante o dia inteiro!"

    p "É mesmo? Bom, até que faz sentido."

    n "O café também ajuda os seres humanos a desbloquearem parte do potencial oculto de nossos cérebros! Mas eles não querem que saibamos disso!"

    p "Eles, quem?"

    n "Hum... Não tenho certeza."

    "Nebi parece estar orgulhosa de si mesma."

    p "Quem foi que te contou isso? Foi o Galdino?"

    n "Não, foi o Fábio!"

    p "Ah, tá..."

    "E pensar que eu quase tinha comprado essa ideia. A última parte acabou entregando tudo."

    p "Bom, eu acho melhor tomar cuidado com o que o Fábio conta. Ele pode ser bastante... empolgado às vezes."

    n "Você acha que ele tava mentindo??"

    p "Tenho certeza."

    n "Poxa..."

    "Agora ela está claramente chateada. Por que estou me sentindo a pessoa malvada desta conversa?"

    "É... Veja bem... Talvez ele não esteja completamente errado! Acho que já li algo sobre escritores sempre beberem café!"

    n "Sério?"

    p "Sim! Já esse lance de desbloquear o seu cérebro parece abobrinha."

    "O garçom chega com o nosso pedido."

    "Provo um pouco da minha bebida."

    if drinkChoice == 0:
        "O suco veio bem azedo, do jeito que eu gosto."
    elif drinkChoice == 1:
        "O milkshake tem um gosto doce, mas não muito exagerado como os de fast food tradicionais. Nada mal."
    elif drinkChoice == 2:
        "Me surpreendi ao ver que tinham chá de boldo no menu. O gosto é forte e amargo, como esperado."

    "Parece que fiz uma boa escolha. Enquanto isso, Nebi encara o seu café."

    "Ela me olha de volta, e empurra o seu prato levemente em minha direção."

    menu:
        n "Pão de queijo. Pega um, uai!"

        "Aceito.":

            "Aceito a oferta e pego um dos pães de queijo. O gosto é muito bom e a textura é macia. Claramente acabou de ser feito."
            p "Tá muito bom. Obrigado, Nebi!"

        "Recuso.":

            p "Não precisa! Tô guardando espaço pro jantar."
            n "Ok!"

    p "Como está o seu café?"

    n "Vou provar agora!"

    "Nebi pega a xícara com as duas mãos e toma um gole do café."

    n "Hum..."

    if coffeChoice == 0:
        jump coffe_notgreat
    elif coffeChoice == 1:
        jump coffe_great
    elif coffeChoice == 2:
        jump coffe_awful

label coffe_notgreat:
    n "Não é ruim, mas também não é tão bom. Achei que sentiria um gosto mais forte."

    p "Talvez o leite tenha diluído demais o sabor original."

    n "Talvez. Mesmo assim, obrigado pela dica!"

    jump tasting_end

label coffe_great:
    n "Achei bem gostoso! Sinto um pouco de amargura, mas o açúcar faz com que não fique forte demais."

    n "Acho que encontrei o meu tipo de café! Muito obrigado pela dica!"

    p "Hehe, de nada..."

    jump tasting_end

label coffe_awful:
    n "Blergh..."

    n "É bem amargo, né?"

    p "É o que as pessoas costumam falar quando provam café puro."

    n "Pra falar a verdade, não gostei muito..."

    p "Talvez eu deveria ter sugerido que colocasse algo pra melhorar o gosto."

    n "Não tem problema! É sempre bom saber qual é o sabor puro!"

    n "Na próxima, eu escolho algo pra botar nele!"

    jump tasting_end

label tasting_end:

    n "Bom, essa foi uma grande experiência..."

    n "...que acabou não ajudando tanto."

    "Nebi solta um leve suspiro."

    p "Você tá bem?"

    n "Sim, eu só..."

    n "Na verdade, tenho um problema."

    p "Qual problema?"

    n "Pra falar a verdade, eu não sei sobre o que escrever!"

    p "!!!"

    n "Acabei pedindo dicas para o Fábio porque ele já escreve a história dele."

    n "Apesar de ter entrado na Novel Brasil, tento escrever e não consigo. Acredita nisso?"

    p "Claro que acredito! Comigo tem sido a mesma coisa."

    p "Ontem eu fui no parque porque estava tentando ter ideia sobre o que escrever."

    p "Isso estava me incomodando bastante, até que eu encontrei você por lá."

    n "É mesmo? Eu não fazia ideia."

    n "E o que você decidiu?"

    p "Olha, na verdade eu ainda não sei sobre o que escrever. Mas vou continuar me esforçando nas aulas e lendo mais. Eventualmente vou encontrar algo."

    p "E com certeza, você também vai!"

    "Percebo que ela se sente um pouco menos preocupada."

    n "Quer saber? Concordo com você, [name]!"

    n "Irei me focar nos estudos, e não vou deixar que isso me incomode tanto."

    n "Além do mais, mesmo que minha primeira ideia dê errado, as outras 48 sairão ainda melhores!"

    p "Isso aí!"

    p "Peraí, como é??"

    n "Atualmente eu tenho 49 ideias de webnovels, mas não consigo me decidir por qual começar! Isso tava me preocupando bastante, mas com a sua ajuda, me sinto mais tranquila!"

    p "D-de nada..."

    n "Tenho ideias para novels de cultivo, algumas de isekai, uma de romance, uma de artes marciais com sistema de mmo, outra de..."

    hide nebi

    "E isso se alongou por algum tempo. Ela falou de alguns gêneros que nunca ouvi falar."

    "Sinto que vou acabar aprendendo bastante com a Nebi. Sua paixão pela leitura e por webnovels é incomparável."

    "Depois de terminarmos nosso lanche, nos despedimos e retorno para casa."

    scene bg classroom
    with fade

    "Ao chegar no dormitório, preparo algo pra jantar."

    "A geladeira ainda possui um espaço vazio. Antes eu achava que estava faltando um aluno, mas percebi que tem uma pessoa que não toca nela desde o primeiro dia."

    "E falando nele..."

    show fabio sheathed smug at right

    f "Yo!"

    p "Oi, Fábio."

    f "Comendo um rango, aí?"

    p "Estou, sim. Por que não vem comer, também?"

    f "Ah, bem... É que eu já jantei..."

    p "É mesmo? Não vi. Jantou fora?"

    f "Isso..."

    p "E você sempre come fora? Não fica muito caro?"

    f "M-mas é claro que não! Sempre estou cozinhando aqui, v-você que nunca viu!"

    p "Não tem nada seu na geladeira, como que você cozinha assim?"

    "Fábio não conseguia encontrar uma desculpa convincente, e apenas continuou calado."

    p "Você não sabe cozinhar, Fábio?"

    f "Absurdo! E-eu sou um grande cozinheiro! Assisti todos os episódios de Shokugeki no Soma!"

    p "Eu sabia..."

    p "Quer ajuda? Eu não sei fazer tanta coisa, mas consigo te ensinar algo bem básico. O que acha?"

    f "Eu... Eu recuso!"

    p "??"

    f "..."

    f "Eu tenho um Rei Demônio selado dentro de mim! Sua energia me torna 250\% mais forte do que um humano comum. Não preciso destas futilidades!"

    f "Além disso, quando o meu treinamento quântico for completado, serei reconhecido pelos oito grande demônios como o herdeiro da espada suprema! Terei milhares de servos para cozinhar pra mim!"

    f "Os desafios que irei enfrentar são grande demais para perder tempo aprendendo uma arte mundana, e..."

    "Ele não consegue parar de falar. Acho que quebrei o garoto."

    "Vou pedir ajuda pra Nebi, amanhã. Quem sabe ela me ajuda a convencê-lo."

    f "...saiba que eu também sou o campeão das sete estrelas de safira! Assim que eu encontrar as quatro esmeraldas do coração, que estão espalhadas ao redor do mundo, eu irei..."

    "Que sono. Acho melhor ir pra cama por hoje."

    p "Vou dormir. Boa noite, Fábio."

    f "Boa Noite!"

label day4:

    scene bg classroom
    with fade

    "Dia 4 - Quinta-feira"

    # á à ã â é ê É í ô ó õ ú ç
    # não são está ção ções

label day4_afterclass:

    scene bg classroom
    with fade

    "Assim que a aula termina, explico para a Nebi sobre o Fábio. Nebi prontamente vai atrás dele, e nos encontramos mais uma vez na sala de aula."

    show nebi armsbehind smiling at right
    show fabio sheathed smug at left

    n "Fábio, você precisa aprender a cozinhar! Senão você vai gastar muito dinheiro comendo fora!"

    f "Urgh!"

    p "[name] me contou sobre isso. Podemos te ajudar a fazer algo!"

    f "Pois saiba que você está enganada! Minhas habilidades simplesmente foram seladas quando eu enfrentei o príncipe dos vampiros pelo controle do..."

    "Do nada, Nebi pega o Fábio pelo braço e caminha em direção a saída."

    f "M-mas o que é isso? Será o início de uma história de amor entre duas almas predestinadas?"

    n "Fica quieto! Vamos agora no supermercado. E eu não quero ouvir um piu sobre poderes selados, entendido?"

    f "S-sim, senhora!"

    p "Vamos, [name]!"

    "Esse é um lado da Nebi que eu não esperava ver..."

    scene bg kitchen
    with fade

    "Fomos ao supermercado comprar ingredientes, e de lá viemos para o dormitório. Aparentemente, podemos ter visitantes até antes do anoitecer."

    "Desembrulhamos as compras e colocamos tudo no balcão da cozinha. Nebi lava as suas mãos e nos fala para fazermos o mesmo."

    show nebi armsbehind smiling at right
    show fabio sheathed smug at left

    n "Muito bem! Vamos rever o que compramos hoje!"

    n "Peito de frango, alho, mostarda, cogumelos, creme de leite e batata palha!"

    n "O que acha que podemos fazer com isso, Fábio?"

    f "Hum... Meu conhecimento de alquimia está meio enferrujado. Por acaso iremos transmutar a pedra filosofal?"

    p "Minha nossa..."

    n "Errado. Vamos fazer strogonoff de frango."

    n "[name]! Por acaso vocês tem maionese, ketchup, sal e pimenta sobrando?"

    p "Temos, sim!"

    n "Perfeito. Então está decidido. Você vai aprender a fazer um strogonoff decente, esse será o seu primeiro prato!"

    f "Sim... sensei!"

    n "Sensei??"

    f "Me ensine os segredos desta arte proibida! Prometo que serei um discípulo digno!"

    n "Hunf. Muito bem, mãos à obra!"

    "No final das contas, ele acabou dando o braço a torcer, do jeito dele."

    scene bg kitchen
    with fade

    show nebi armsbehind smiling at right

    n "Me passa a panela e a frigideira, [name]?"

    p "Aqui está."

    n "Pode ligar o fogão, Fábio?"

    show fabio sheathed smug at left

    f "Er... meu nível de maestria neste equipamento ainda não é grão-mestre, mas talvez eu..."

    n "Vou te mostrar como ligar. Nunca use um fogão sem saber como funciona!"

    f "Sim, mestre!"

    scene bg kitchen
    with fade

    show nebi armsbehind smiling at right

    n "Fábio, usa o pegador pra virar o frango."

    show fabio sheathed smug at left

    "Fábio se aproxima da frigideira, mas ao sentir o calor, dá um passo pra trás."

    f "As chamas infernais são muito poderosas!"

    n "É só virar com cuidado, sem deixar o azeite respingar."

    f "C-certo!"

    "Parece que de alguma forma a Nebi conseguiu entender como o Fábio funciona!"

    "Lentamente Fábio consegue virar as peças de frango."

    f "Eu dominei as chamas negras do inferno!"

    p "Muito bem."

    scene bg kitchen
    with fade

    "Após alguns minutos, a comida fica pronta. Falo para Nebi e Fábio se sentarem à mesa, e sirvo o strogonoff em três pratos."

    p "Bom apetite, pessoal."

    show nebi armsbehind smiling at right

    n "Hehe!"

    show fabio sheathed smug at left

    f "Itadakimassu!"

    "Damos a primeira garfada, e... está ótimo!"

    "Apesar das medidas terem sido feitas \"no olho\", deu tudo certo."

    "Olho para os dois. Nebi também parece ter gostado, já que ela não parou de comer desde a primeira mordida."

    "Fábio está com os braços cruzados, pensando. Ele fica assim por alguns segundos, e decide falar."

    f "A qualidade deste prato certamente evoluirá as minhas células gourmet. Bom trabalho à todos!"

    p "...De nada?"

    f "Hoje, vocês se mostraram dignos de meu respeito. Acho justo que façamos um pacto!"

    f "Deste dia em diante, esta será oficialmente conhecida como a aliança humano-demônio-jinchuuriki-vampiro-shinigami da Novel Brasil!"

    p "Deixa eu adivinhar: Nós somos os humanos, e você é o resto?"

    f "Muito astuto! Não espero nada menos de um membro da aliança!"

    n "Então quer dizer que somos amigos!"

    f "Sempre que estiverem em apuros, lhes emprestarei um pouco do meu poder selado! Estarão segundos comigo."

    p "Legal..."

    n "Conto com você, Fábio!"

    f "Hehe..."

    "Sinto que esse é o momento perfeito para conhecer o Fábio de verdade."

    p "Tenho uma pergunta, Fábio... Como era a sua antiga escola, antes de você vir pra Novel Brasil?"

    f "Oh! Você gostaria de conhecer a história do seu aliado? Pois bem, lhe contarei."

    p "Ok."

    "Fábio coloca seus talheres no prato, fazendo uma cara pensativa, como se fosse um personagem que está prestes a iniciar um monólogo importante."

    f "Eu estudei em um colégio religioso. O rei dem... O diretor era muito restrito no código de conduta. Não podíamos falar sequer um piu durante as dez horas de aula."

    "Acho que entendi porque a Nebi conseguiu botar ele nos eixos, mais cedo."

    n "Minha nossa! E o que os seus amigos achavam disso?"

    f "Eu não tinha nenhum amigo..."

    n "!!"

    f "Eu tentei interagir com alguns deles, depois das aulas. Perguntava pra eles quais eram suas waifus preferidas e quais animes da temporada eles estavam assistindo."

    f "Acabou que nenhum deles gostava dessas coisas. Eles me achavam estranho. Eu sempre era zoado, depois das aulas."

    f "Os meus pais acabaram me tirando da escola antes do ano terminar. Então eu passei o resto do ano lendo webnovels, e foi aí que comecei a escrever."

    f "Então eles me matricularam na Novel Brasil. Uma escola onde todos escrevem webnovels!"

    f "Finalmente encontrei um lugar onde posso ser reconhecido por quem sou de verdade."

    p "Eu não fazia ideia..."

    "Ao perceber que havia saído do personagem, Fábio pigarreou e retomou sua postura de sempre."

    f "Bom, já que vocês me ensinaram a técnica secreta do strogonoff de frango, acho que isso é o mínimo que posso fazer em troca!"

    p "Obrigado por compartilhar sua história conosco. Viver num ritmo rígido desses, e ser zoado por todos deve ser muito ruim mesmo."

    p "Mas eu acho que você poderia maneirar um pouquinho qua-"

    n "Pode contar com a gente, Fábio! Te aceitamos do jeito que você é! Certo, [name]?"

    p "Certo..."

    f "Hehe! Sabia que havia escolhido os súditos perfeitos para o meu império!"

    p "Achava que fossemos aliados..."

    hide nebi
    hide fabio

    "E a conversa se alongou até o final do dia."

    "Ao anoitecer, Nebi se despediu e foi para sua casa. Fábio e eu ficamos lavando louça por um tempo."

    "Colocamos alguns dos ingredientes restantes na geladeira. Deve ter o suficiente pra fazer outro prato amanhã. Seria bom ele aprender a fazer outra coisa, no fim de semana."

    "Depois disso, vou para o meu quarto, ler algumas webnovels."

    "Amanhã é o final da nossa primeira semana na academia. Também será o dia que o Galdino nos dará o resultado das nossas avaliações iniciais."

    "Mas é melhor não se preocupar com isso, por enquanto. Senão não vou cair no sono."

    "Em vez disso, vou checar os capítulos que foram postados na Kiniga nessa semana. Ainda não li nada desde que cheguei aqui..."

    # á à ã â é ê É í ô ó õ ú ç
    # não são está ção ções

label day5:

    scene bg classroom
    with fade

    "Dia 5 - Sexta-feira"

    return
