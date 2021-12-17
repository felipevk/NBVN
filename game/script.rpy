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

label start:

    python:
        name = renpy.input("Digite o seu nome")
        name = name.strip() or "Protagonista"

label day1:

    scene bg classroom
    with fade

    "Dia 1 - Segunda-feira"

    "Hoje é meu primeiro dia na Academia Novel Brasil."

    "Este lugar basicamente é o maior formador de talentos de web novels no país inteiro."

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

    p "Serio? Que alívio!"

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

    g "Serei o seu professor durante este ano. Tenho dado aula nesta instituição a mais de dez anos. Apesar disso, a arte da escrita, sobretudo de web novels, ainda tem um enorme espaço de crescimento no nosso país."

    g "Espero ver grandes obras vindo dos escritores desta classe, e que atraiam ainda mais pessoas para este meio."

    g "Como podem ver, minhas expectativas são altas. Mas quero que saibam que nós da Novel Brasil estaremos aqui para ajudar-los durante esta jornada. Conte conosco, e chegaremos longe!"

    "Os alunos começam a murmurar entre si. Apesar do discurso ter sido meio... cafona, não há dúvidas de que causou uma certa impressão na sala."

    "Parando pra pensar, a maioria dos meus amigos da minha escola antiga nunca nem ouviram falar em web novels. Talvez ele esteja certo. "

    g "Agora, eu quero ouvir vocês. Gostaria que cada um se apresente brevemente para a classe!"

    g "Vamos começar pela primeira fileira."

    "Galdino olha em direção à garota que me ajudou anteriormente. Ela se levanta."

    hide galdino

    show nebi armsbehind smiling at center

    n_u "Bom dia! Meu nome é Nebi!"

    n "Meu passatempo favorito é ler livros e web novels, e sempre quis escrever a minha propria história! Conto com a ajuda de todos para nos tornamos grandes escritores!"

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

    g "Iremos abordar os conceitos básicos de web novels e escrita. Não será necessário nenhum conhecimento prévio sobre estes assuntos, podem ficar tranquilos."

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

    g "O assunto de hoje é direto ao ponto: Vamos falar sobre {b}o que é uma web novel.{/b}"

    g "Uma web novel é simplesmente uma novel, um romance, feita para a internet. Diferente de um livro, os capitulos são lançados separadamente."

    g "Muitas pessoas confundem light novels com web novels. A maior diferença é no metodo de publicação."

    g "Light novels são publicadas através de editoras, em formato físico. Enquanto que web novels estão na web, geralmente de forma independente ou não-exclusiva."

    g "Claro, nada impede que um autor de uma web novel popular seja abordado por uma editora, e a sua obra seja publicada como light novel. Isso ocorre bastante, fora do país"

    g "Quanto às semelhanças, ambas web novels e light novels apresentam um estilo de escrita menos rebuscado, comparado com romances tradicionais."

    g "O público-alvo destas mídias é de uma faixa etária de jovens, que buscam uma leitura mais acessivel."

    g "Sobretudo com web novels, que podem ser lidas num celular, acessibilidade é essencial!"

    g "Mantenham em mente que, mesmo que o seu texto pareça curto na tela do computador, ele também precisa ser facilmente lido em uma tela menor de celular."

    g "Perguntas?"

    "Nenhum aluno se pronuncia. Porém, percebo que todos estão claramente concentrados no professor. Alguns estão até fazendo anotacoes, incluindo a Nebi."

    g "Muito bem. Para finalizar a aula de hoje, vamos falar sobre sites brasileiros de web novels."

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
        g "Me responda, o que é uma web novel?"

        "É um romance publicado em bancas.":

            jump q1_a1

        "É uma história publicada na internet, independente de editoras.":

            jump q1_a2

        "São textos feitos fora do brasil que são traduzidos para o português.":

            jump q1_a3

    label q1_a1:

    g "A resposta está... incorreta. Como o nome diz, web novels são postadas na internet."

    jump q2

    label q1_a2:

    $ score += 1

    g "A resposta está correta! Essa é uma definição muito importante para vocês, autores."

    g "Entender os elementos do meio que você se encontra é essencial para que se tire o maior proveito possível dele."

    g "O mesmo vale para filmes, jogos, musica, etc. Faça bom uso da mídia, e sua obra terá apenas a ganhar com isso."

    jump q2

    label q1_a3:

    g "A resposta está incorreta. Web novels podem ser feitas em qualquer idioma, inclusive em português."

    show galdino nobook amused

    g "Se esse não fosse o caso, pra que estaríamos aqui?"

    show galdino nobook neutral

    jump q2

    label q2:

    g "Próxima pergunta!"

    "Tem mais?"

    g "Só mais uma..."

    menu:
        g "Qual a diferença entre web novels e light novels?"

        "Web novels são publicadas na internet, enquanto que light novels são publicadas fisicamente, por editoras.":

            jump q2_a1

        "Nenhuma.":

            jump q2_a2

        "Web novels são publicadas por editoras, e light novels são independentes.":

            jump q2_a3

    label q2_a1:

    $ score += 1

    g "Correto! Que bom que está prestando atenção."

    "Moleza!"

    jump day1_class_end

    label q2_a2:

    g "Errado. Muitas pessoas acham que não tem diferença, mas light novels são publicadas por editoras, em bancas e livrarias, enquanto que web novels estão na... web."

    g "Entendido?"

    p "Entendido..."

    jump day1_class_end

    label q2_a3:

    g "Incorreto. Na verdade é o oposto: web novels são, na sua maioria, independentes; light novels são publicadas por editoras."

    "Verdade..."

    jump day1_class_end

    label day1_class_end:

    "O sino bate."

    g "Bom, com isso concluímos a nossa aula. Este é o primeiro passo nas suas jornadas para se tornarem escritores."

    g "Amanhã falaremos um pouco sobre gêneros de web novels. Tenham um bom descanso, e até a próxima!"

    hide galdino

    "O professor deixa a sala, e os alunos começam a se preparar para sair."

    "Este primeiro dia foi bem interessante. O professor parece entender bem sobre web novels, enquanto os alunos são bem concentrados."

    "Inclusive, o cansaço tá batendo. Hora de pegar o metrô pra casa."

    scene bg classroom
    with fade

    "Antes de voltar para o dormitório, decido fazer umas compras para a semana."

    "O lado bom de ter me perdido de manhã foi que encontrei este supermercado que fica no caminho para a escola."

    "Não tenho o costume de cozinhar, mas fica bem mais em conta do que comer fora, ou pedir delivery."

    "Assim que termino de comprar tudo que preciso, retomo o caminho pra casa."

    scene bg classroom
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

    scene bg classroom
    with fade

    "Enfim, estou no meu quarto."

    "Apesar de ter usado isso como desculpa pra fugir, este dia realmente foi cheio."

    "Uma nova cidade. Uma nova escola. Web novels. Colegas de sala peculiares..."

    "Será que eu vou dar conta de escrever minha própria história? Pra falar a verdade, não sei bem sobre o que eu gostaria de escrever."

    "Bom, as aulas acabaram de começar. Acho que tenho tempo suficiente pra decidir isso. Agora vou dormir."

    jump day2

label day2:
    scene bg classroom
    with fade

    "Dia 2 - Terça-feira"

    show galdino nobook neutral at center

    g "Quero que me respondam: O que vocês gostariam de escrever?"

    "O que???"

    g "Estamos em uma academia de escritores, eventualmente vocês irão escrever web novels. Talvez alguns até já tenham começado."

    g "Levante a mão caso você já esteja escrevendo algo."

    "Cerca de cinco ou seis pessoas levantaram a mão, incluindo o Fábio."

    g "Agora levante a mão caso você já tenha uma ideia para a sua história."

    "Desta vez, muitos outros ergueram suas mãos. Acho que mais da metade da sala já sabe sobre o que quer escrever."

    g "Muito bem. A aula de hoje será sobre gêneros de web novels. Abordaremos alguns dos mais populares, e discutiremos o porque de serem tão populares."

    g "Para os escritores que ainda não se sabem sobre o que querem escrever, espero que essa aula sirva de incentivo para que se decidam."

label day2_afterclass:
    "Os alunos começam a se arrumar para sair. Antes que Galdino saia da sala, me dirijo a ele."

    p "Com licença, professor?"

    show galdino nobook neutral at center

    g "Alguma dúvida, [name]?"

    p "Sim. Sobre o que o senhor falou no começo da aula..."

    "Pouco a pouco os alunos saem da sala. Ao final da minha frase, a maioria das pessoas já se retiraram."

    p "Pra falar a verdade, mesmo gostando de ler web novels, eu não faço a mínima ideia sobre que tipo de história eu quero escrever."

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

    g "Você parece estar com muitos pensamentos na cabeça. Alguns ajudam, outros nem tanto. Por isso a minha recomendaçao é que você vá dar uma volta pra espairecer."

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

    n "É muito legal ver este meio sendo valorizado. Como o professor Velasco disse, ainda existem poucas web novels brasileiras, se comparado as outros países."

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

    # á à ã é ê É í ô ó õ ú ç
    # não está

label day3:

    scene bg classroom
    with fade

    "Dia 3 - Quarta-feira"

label day4:

    "Dia 4 - Quinta-feira"

label day5:

    "Dia 5 - Sexta-feira"

    return
