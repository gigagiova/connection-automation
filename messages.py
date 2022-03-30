import random


def fb_connection_ita(group_name):
    intros = [f"Ciao! Ho trovato il tuo profilo su {group_name}. ",
              f"Ciao! Ti ho visto su {group_name}. ",
              f"Hey! Ti ho trovato girando su {group_name}. "]

    mids = [
        "Assieme a dei miei amici developer vogliamo aiutare i gamer a migliorare le loro skills e diventare pro. Sarebbe molto utile per noi poterti fare qualche domanda per capire le difficoltà che i gamer incontrano ed elaborare una giusta soluzione. ",
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


def fb_connection_en(group_name):
    intros = [f"Hi! I found your profile on {group_name}. ",
              f"Hi! I saw you on {group_name}. ",
              f"Hey! I found you browsing on {group_name}. "]

    mids = [
        "Together with some developer friends of mine we want to help gamers to improve their skills and become pros. It would be very helpful for us to be able to ask you a few questions to understand the difficulties gamers face and develop the right solution. ",
        "With some programmer friends of mine we are interested in helping players to rank up and improve their skills. It would be very helpful for us to be able to ask you a few questions to understand the difficulties gamers face and come up with the right solution. ",
        "Together with some programmer friends of mine we would like to help players improve their skills and rank up. It would be very helpful for us to ask you some questions to know your experience! ",
        "With some developer friends of mine we would like to help players rank up by improving their skills. It would be very helpful for us to ask you some questions and understand your experience! ",
        "With some developer friends of mine we would like to help players improve their skills and rank up. It would help us a lot to ask you some questions to understand the difficulties that gamers face and work out the right solution. "
    ]

    ends = [
        "What is the best time we could hear from you for a brief informal interview?",
        "When would you be available for a brief informal interview?",
        "When would you be available for a brief chat?",
        "What is the best time for a short interview?",
        "When can we get in touch for a brief interview?",
        "When would be a good time for a chat?",
        "When is the best time to have a brief call together?",
        "When might we get in touch to have a call?"
    ]

    return (intros[random.randrange(0, len(intros) - 1)] +
            mids[random.randrange(0, len(mids) - 1)] +
            ends[random.randrange(0, len(ends) - 1)])
