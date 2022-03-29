import random


def fb_connection(group_name):

    intros = [f"Ciao! Ho trovato il tuo profilo su {group_name}. ",
              f"Ciao! Ti ho visto su {group_name}. ",
              f"Hey! Ti ho trovato girando su {group_name}. ",
              f"Hey! Ti ho trovato girando su {group_name}. "]

    mids = ["Assieme a dei miei amici developer vogliamo aiutare i gamer a migliorare le loro skills e diventare pro. Sarebbe molto utile per noi poterti fare qualche domanda per capire le difficoltà che i gamer incontrano ed elaborare una giusta soluzione. ",
            "Con dei miei amici programmatori ci interessa aiutare i player a rankare e migliorare le loro skill. Ci sarebbe molto d’aiuto farti qualche domanda per capire le difficoltà che i gamer incontrano ed elaborare una giusta soluzione. ",
            "Assieme a dei miei amici programmatori vorremmo aiutare i player a migliorare le loro skills e a salire di rank. Ci sarebbe molto utile farti qualche domanda per conoscere la tua esperienza! ",
            "Con dei miei amici developer vorremmo aiutare i giocatori a salire di rank migliorando le loro skill. Ci sarebbe molto d’aiuto farti qualche domanda per conoscere la tua esperienza! ",
            "Con dei miei amici programmatori aiutiamo i player a migliorare le loro skills e a salire di rank. Ci sarebbe molto d’aiuto farti qualche domanda per capire le difficoltà che i gamer incontrano ed elaborare una giusta soluzione. "]

    ends = ["Qual'è il momento migliore in cui potremmo sentirci per una breve intervista informale?",
            "Quando saresti disponibile per una breve intervista informale?",
            "Qual'è il momento migliore per breve intervista?",
            "Quando è che potremmo sentirci per una breve call?",
            "Quando è che potremmo sentirci fare due chiacchiere?",
            "Quando è che potremmo sentirci fare due chiacchiere in call?",
            "Quando è che potremmo sentirci fare una call?"]

    return (intros[random.randrange(0, len(intros) - 1)] +
            mids[random.randrange(0, len(mids) - 1)] +
            ends[random.randrange(0, len(ends) - 1)])
