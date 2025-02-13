from random import choice, randint

EXCUSES = [
    f"Fa {randint(2,30)} anys plovia",
    f"Tinc hora a la pelu que nomes hi vaig {randint(1,20)} cops per setmana",
    f"Vaig al gym, la idea es anarhi {randint(1,20)} cops per setmana",
    "Aquest dia justament vaig a donar sang",
    "Casum l'olla! Tinc un dinar familiar",
    "Demà haig d'anar a passar la itv",
    "El metge m'ha dit que no puc menjar aliments rics en sodi",
    "Esque em guardo dies de vacances",
    "Esque se m'ha punxat la roda de la bici estàtica i l'he de canviar",
    "Esque vai demanar un paquet i crec que m'arribarà llavors",
    "Esque fa molt sol i no tinc crema",
    "Esque he d'anar a treure la marmota a passejar",
    "Estic esperant a que el Jefe em doni el contracte que m'ha dit que ara me'l porta",
    "Estic esperant la corda i tamboret que m'he demanat a amazon",
    "He quedat per fer una muntanya",
    "Jo vindira, però es que se m'ha espatllat el GPS del mòbil",
    "Jo vindria, però m'agrada fer motos",
    "Jo vindria, però es que s'em morirà el peix que vaig a comprar ara",
    "Justament aquest dia he quedat per jugar a arrancar cebes",
    "M'he endescuidat de regar el cactus de gisce",
    "Mha semblat veure una gota a la carretera",
    "No puc venir pk la dona m'ha dit que anes a la platja de palafrugell i em quedés un parell d'hores sota l'aigua",
    "No puc venir que he d'afegir excuses de moto al bot",
    "Plou i fa sol, em quedo a casa sol",
    "Se m'ha mort el PC i li fem un funeral. Tenia una 3080ti",
    "Se m'ha mort la PS5 i li fem un funeral. Poques que n'hi han...",
    "Soc un mort de gana",
    "Tinc el rellotge en format 24h",
    "Tinc un conegut que fa casi un any que no veig que té corona, així que faig quarentena per si de cas.",
    "Tu que m'acaben de trucar que d'aqui 20min anem a fer una implantació i no sé quan tornaré.",
    "Volia venir pro no soy 1000itar",
    "Volia venir pro no soy 1000itante",
    "Volia venir pro no soy 100tifiko",
]


def get_random_excuse() -> str:
    """Generate a random text for motos

    Returns:
        str: Moto quote
    """
    return choice(EXCUSES)
