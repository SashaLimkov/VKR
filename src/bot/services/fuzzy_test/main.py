from simpful import *


def get_fuzzy_ill_system(user_answers: dict):
    FS = FuzzySystem()
    P_1 = FuzzySet(function=Triangular_MF(a=0.1, b=0.5, c=0.9), term="low")
    P_2 = FuzzySet(function=Triangular_MF(a=1, b=1.1, c=1.2), term="high")

    FS.add_linguistic_variable("weakness",
                               LinguisticVariable([P_1, P_2], concept="Слабость", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("temp",
                               LinguisticVariable([P_1, P_2], concept="Температура", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("edema",
                               LinguisticVariable([P_1, P_2], concept="Отечность", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("nausea",
                               LinguisticVariable([P_1, P_2], concept="Тошнота", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("noj", LinguisticVariable([P_1, P_2], concept="НОЖ", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("stiffness",
                               LinguisticVariable([P_1, P_2], concept="Скованность", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("skin_t",
                               LinguisticVariable([P_1, P_2], concept="Проблемы с кожей",
                                                  universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("back_pain",
                               LinguisticVariable([P_1, P_2], concept="Боли в спине", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("lymph",
                               LinguisticVariable([P_1, P_2], concept="Лимфоузлы", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("mus_pain",
                               LinguisticVariable([P_1, P_2], concept="Мыщечная боль", universe_of_discourse=[0, 1.2]))
    FS.add_linguistic_variable("cancer",
                               LinguisticVariable([P_1, P_2], concept="Онкология", universe_of_discourse=[0, 1.2]))

    SMM_1 = FuzzySet(function=Triangular_MF(a=0, b=10, c=33), term="low")
    SMM_2 = FuzzySet(function=Triangular_MF(a=34, b=55, c=66), term="medium")
    SMM_3 = FuzzySet(function=Triangular_MF(a=67, b=88, c=100), term="high")
    FS.add_linguistic_variable("SMM",
                               LinguisticVariable([SMM_1, SMM_2, SMM_3],
                                                  concept="Вероятность  кожных заболеваний",
                                                  universe_of_discourse=[0, 100]))

    LN_1 = FuzzySet(function=Triangular_MF(a=0, b=39, c=40), term="low")
    LN_2 = FuzzySet(function=Triangular_MF(a=41, b=79, c=100), term="high")
    FS.add_linguistic_variable("LN",
                               LinguisticVariable([LN_1, LN_2],
                                                  concept="Вероятность  заболеваний лимфатической системы",
                                                  universe_of_discourse=[0, 100]))
    MJ_1 = FuzzySet(function=Triangular_MF(a=0, b=15, c=20), term="very low")
    MJ_2 = FuzzySet(function=Triangular_MF(a=21, b=35, c=40), term="low")
    MJ_3 = FuzzySet(function=Triangular_MF(a=41, b=55, c=60), term="medium")
    MJ_4 = FuzzySet(function=Triangular_MF(a=61, b=75, c=80), term="high")
    MJ_5 = FuzzySet(function=Triangular_MF(a=81, b=95, c=100), term="very high")
    FS.add_linguistic_variable("MUS",
                               LinguisticVariable([MJ_1, MJ_5, MJ_4, MJ_3, MJ_2],
                                                  concept="Вероятность  заболеваний мышечной системы",
                                                  universe_of_discourse=[0, 100]))
    FS.add_linguistic_variable("JOI",
                               LinguisticVariable([MJ_1, MJ_5, MJ_4, MJ_3, MJ_2],
                                                  concept="Вероятность  заболеваний суставов ",
                                                  universe_of_discourse=[0, 100]))
    BRDUH_1 = FuzzySet(function=Triangular_MF(a=0, b=15, c=25), term="low")
    BRDUH_2 = FuzzySet(function=Triangular_MF(a=26, b=35, c=50), term="medium")
    BRDUH_3 = FuzzySet(function=Triangular_MF(a=51, b=65, c=74), term="high")
    BRDUH_4 = FuzzySet(function=Triangular_MF(a=75, b=90, c=100), term="very high")
    FS.add_linguistic_variable("BON",
                               LinguisticVariable([BRDUH_4, BRDUH_3, BRDUH_2, BRDUH_1],
                                                  concept="Вероятность  заболеваний Костной системы ",
                                                  universe_of_discourse=[0, 100]))
    FS.add_linguistic_variable("RO",
                               LinguisticVariable([BRDUH_4, BRDUH_3, BRDUH_2, BRDUH_1],
                                                  concept="Вероятность  заболеваний дыхательной системы ",
                                                  universe_of_discourse=[0, 100]))
    FS.add_linguistic_variable("DO",
                               LinguisticVariable([BRDUH_4, BRDUH_3, BRDUH_2, BRDUH_1],
                                                  concept="Вероятность  заболеваний пищеварительной системы ",
                                                  universe_of_discourse=[0, 100]))
    FS.add_linguistic_variable("UO",
                               LinguisticVariable([BRDUH_4, BRDUH_3, BRDUH_2, BRDUH_1],
                                                  concept="Вероятность  заболеваний мочеточной системы",
                                                  universe_of_discourse=[0, 100]))
    FS.add_linguistic_variable("HAES",
                               LinguisticVariable([BRDUH_4, BRDUH_3, BRDUH_2, BRDUH_1],
                                                  concept="Вероятность  заболеваний кроветворной системы",
                                                  universe_of_discourse=[0, 100]))

    FS.add_rules([
        "IF (skin_t IS high) AND (temp IS high) THEN (SMM IS high)",
        "IF (skin_t IS low) AND (temp IS high) THEN (SMM IS medium)",
        "IF (skin_t IS high) AND (temp IS low) THEN (SMM IS medium)",
        "IF (skin_t IS low) AND (temp IS low) THEN (SMM IS low)",
        "IF (lymph IS low) THEN (LN IS low)",
        "IF (lymph IS high) THEN (LN IS high)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS high) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS very high)",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS low) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS very low)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS high) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS high)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS high) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS high)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS low) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS high)",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS high) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS high)",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS high) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS high)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS high) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS low) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS high) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS high) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS low) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS high) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS high) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS low) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS medium)",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS low) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS medium)",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS high) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS medium)",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS low) AND (nausea IS high) AND (stiffness IS high) THEN (MUS IS medium)",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS high) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS low) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS low) AND (nausea IS low) AND (stiffness IS high) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS high) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS low) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS low) AND (nausea IS high) AND (stiffness IS low) THEN (MUS IS medium) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS high) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS medium)",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS high) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS medium)",
        "IF (weakness IS high) AND (temp IS high) AND (edema IS low) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS medium)",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS low) AND (nausea IS low) AND (stiffness IS high)  THEN (MUS IS low) ",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS low) AND (nausea IS high) AND (stiffness IS low)  THEN (MUS IS low) ",
        "IF (weakness IS low) AND (temp IS low) AND (edema IS high) AND (nausea IS low) AND (stiffness IS low)  THEN (MUS IS low) ",
        "IF (weakness IS low) AND (temp IS high) AND (edema IS low) AND (nausea IS low) AND (stiffness IS low)  THEN (MUS IS low)",
        "IF (weakness IS high) AND (temp IS low) AND (edema IS low) AND (nausea IS low) AND (stiffness IS low) THEN (MUS IS low)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS very high)",
        "IF (noj IS low) AND (temp IS low) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS very low)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS high)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS high)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS high)",
        "IF (noj IS high) AND (temp IS low) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS high)",
        "IF (noj IS low) AND (temp IS high) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS high)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS high) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS low) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS high) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS low) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS low) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS medium)",
        "IF (noj IS low) AND (temp IS high) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS medium)",
        "IF (noj IS low) AND (temp IS low) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS medium)",
        "IF (noj IS low) AND (temp IS low) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS high) THEN (JOI IS medium)",
        "IF (noj IS low) AND (temp IS low) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS low) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS high) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS low) AND (edema IS high) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS high) AND (temp IS low) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS low) THEN (JOI IS medium) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS medium)",
        "IF (noj IS high) AND (temp IS low) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS medium)",
        "IF (noj IS high) AND (temp IS high) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS medium)",
        "IF (noj IS low) AND (temp IS low) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS high)  THEN (JOI IS low) ",
        "IF (noj IS low) AND (temp IS low) AND (edema IS low) AND (back_pain IS high) AND (stiffness IS low)  THEN (JOI IS low) ",
        "IF (noj IS low) AND (temp IS low) AND (edema IS high) AND (back_pain IS low) AND (stiffness IS low)  THEN (JOI IS low) ",
        "IF (noj IS low) AND (temp IS high) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS low)  THEN (JOI IS low)",
        "IF (noj IS high) AND (temp IS low) AND (edema IS low) AND (back_pain IS low) AND (stiffness IS low) THEN (JOI IS low)",
        "IF (weakness IS high) AND (noj IS high) AND (back_pain IS high) AND (cancer  IS high) THEN (BON IS very high)",
        "IF (weakness IS high) AND (noj IS high) AND (back_pain IS high) AND (cancer  IS low) THEN (BON IS high)",
        "IF (weakness IS high) AND (noj IS high) AND (back_pain IS low) AND (cancer IS high) THEN (BON IS high)",
        "IF (weakness IS high) AND (noj IS low) AND (back_pain IS high) AND (cancer IS high) THEN (BON IS high)",
        "IF (weakness IS low) AND (noj IS high) AND (back_pain IS high) AND (cancer IS high) THEN (BON IS high)",
        "IF (weakness IS low) AND (noj IS low) AND (back_pain IS high) AND (cancer IS high) THEN (BON IS medium)",
        "IF (weakness IS low) AND (noj IS high) AND (back_pain IS low) AND (cancer IS high) THEN (BON IS medium)",
        "IF (weakness IS low) AND (noj IS high) AND (back_pain IS high) AND (cancer  IS low) THEN (BON IS medium)",
        "IF (weakness IS high) AND (noj IS low) AND (back_pain IS high) AND (cancer  IS low) THEN (BON IS medium)",
        "IF (weakness IS high) AND (noj IS high) AND (back_pain IS low) AND (cancer  IS low) THEN (BON IS medium)",
        "IF (weakness IS high) AND (noj IS low) AND (back_pain IS low) AND (cancer IS high) THEN (BON IS medium)",
        "IF (weakness IS low) AND (noj IS low) AND (back_pain IS low) AND (cancer IS high) THEN (BON IS low)",
        "IF (weakness IS low) AND (noj IS low) AND (back_pain IS high) AND (cancer  IS low) THEN (BON IS low)",
        "IF (weakness IS low) AND (noj IS high) AND (back_pain IS low) AND (cancer  IS low) THEN (BON IS low)",
        "IF (weakness IS high) AND (noj IS low) AND (back_pain IS low) AND (cancer  IS low) THEN (BON IS low)",
        "IF (weakness IS low) AND (noj IS low) AND (back_pain IS low) AND (cancer IS low) THEN (BON IS low)",
        "IF (weakness IS high) AND (noj IS high) AND (temp IS high) AND (mus_pain IS high) THEN (RO IS very high)",
        "IF (weakness IS high) AND (noj IS high) AND (temp  IS high) AND (mus_pain IS low) THEN (RO IS high)",
        "IF (weakness IS high) AND (noj IS high) AND (temp  IS low) AND (mus_pain IS high) THEN (RO IS high)",
        "IF (weakness IS high) AND (noj IS low) AND (temp IS high) AND (mus_pain IS high) THEN (RO IS high)",
        "IF (weakness IS low) AND (noj IS high) AND (temp IS high) AND (mus_pain IS high) THEN (RO IS high)",
        "IF (weakness IS low) AND (noj IS low) AND (temp IS high) AND (mus_pain IS high) THEN (RO IS medium)",
        "IF (weakness IS low) AND (noj IS high) AND (temp IS low) AND (mus_pain IS high) THEN (RO IS medium)",
        "IF (weakness IS low) AND (noj IS high) AND (temp IS high) AND (mus_pain IS low) THEN (RO IS medium)",
        "IF (weakness IS high) AND (noj IS low) AND (temp IS high) AND (mus_pain IS low) THEN (RO IS medium)",
        "IF (weakness IS high) AND (noj IS high) AND (temp IS low) AND (mus_pain IS low) THEN (RO IS medium)",
        "IF (weakness IS high) AND (noj IS low) AND (temp IS low) AND (mus_pain IS high) THEN (RO IS medium)",
        "IF (weakness IS low) AND (noj IS low) AND (temp IS low) AND (mus_pain IS high) THEN (RO IS low)",
        "IF (weakness IS low) AND (noj IS low) AND (temp IS high) AND (mus_pain IS low) THEN (RO IS low)",
        "IF (weakness IS low) AND (noj IS high) AND (temp  IS low) AND (mus_pain IS low) THEN (RO IS low)",
        "IF (weakness IS high) AND (noj IS low) AND (temp  IS low) AND (mus_pain IS low) THEN (RO IS low)",
        "IF (weakness IS low) AND (noj IS low) AND (temp IS low) AND (mus_pain IS low) THEN (RO IS low)",

        "IF (weakness IS high) AND (back_pain IS high) AND (temp IS high) AND (nausea IS high) THEN (DO IS very high)",
        "IF (weakness IS high) AND (back_pain IS high) AND (temp  IS high) AND (nausea IS low) THEN (DO IS high)",
        "IF (weakness IS high) AND (back_pain IS high) AND (temp  IS low) AND (nausea IS high) THEN (DO IS high)",
        "IF (weakness IS high) AND (back_pain IS low) AND (temp IS high) AND (nausea IS high) THEN (DO IS high)",
        "IF (weakness IS low) AND (back_pain IS high) AND (temp IS high) AND (nausea IS high) THEN (DO IS high)",
        "IF (weakness IS low) AND (back_pain IS low) AND (temp IS high) AND (nausea IS high) THEN (DO IS medium)",
        "IF (weakness IS low) AND (back_pain IS high) AND (temp IS low) AND (nausea IS high) THEN (DO IS medium)",
        "IF (weakness IS low) AND (back_pain IS high) AND (temp IS high) AND (nausea IS low) THEN (DO IS medium)",
        "IF (weakness IS high) AND (back_pain IS low) AND (temp IS high) AND (nausea IS low) THEN (DO IS medium)",
        "IF (weakness IS high) AND (back_pain IS high) AND (temp IS low) AND (nausea IS low) THEN (DO IS medium)",
        "IF (weakness IS high) AND (back_pain IS low) AND (temp IS low) AND (nausea IS high) THEN (DO IS medium)",
        "IF (weakness IS low) AND (back_pain IS low) AND (temp IS low) AND (nausea IS high) THEN (DO IS low)",
        "IF (weakness IS low) AND (back_pain IS low) AND (temp IS high) AND (nausea IS low) THEN (DO IS low)",
        "IF (weakness IS low) AND (back_pain IS high) AND (temp  IS low) AND (nausea IS low) THEN (DO IS low)",
        "IF (weakness IS high) AND (back_pain IS low) AND (temp  IS low) AND (nausea IS low) THEN (DO IS low)",
        "IF (weakness IS low) AND (back_pain IS low) AND (temp IS low) AND (nausea IS low) THEN (DO IS low)",

        "IF (weakness IS high) AND (edema IS high) AND (temp IS high) AND (nausea IS high) THEN (UO IS very high)",
        "IF (weakness IS high) AND (edema IS high) AND (temp  IS high) AND (nausea IS low) THEN (UO IS high)",
        "IF (weakness IS high) AND (edema IS high) AND (temp  IS low) AND (nausea IS high) THEN (UO IS high)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS high) AND (nausea IS high) THEN (UO IS high)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS high) AND (nausea IS high) THEN (UO IS high)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS high) AND (nausea IS high) THEN (UO IS medium)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS low) AND (nausea IS high) THEN (UO IS medium)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS high) AND (nausea IS low) THEN (UO IS medium)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS high) AND (nausea IS low) THEN (UO IS medium)",
        "IF (weakness IS high) AND (edema IS high) AND (temp IS low) AND (nausea IS low) THEN (UO IS medium)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS low) AND (nausea IS high) THEN (UO IS medium)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS low) AND (nausea IS high) THEN (UO IS low)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS high) AND (nausea IS low) THEN (UO IS low)",
        "IF (weakness IS low) AND (edema IS high) AND (temp  IS low) AND (nausea IS low) THEN (UO IS low)",
        "IF (weakness IS high) AND (edema IS low) AND (temp  IS low) AND (nausea IS low) THEN (UO IS low)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS low) AND (nausea IS low) THEN (UO IS low)",

        "IF (weakness IS high) AND (edema IS high) AND (temp IS high) AND (nausea IS high) THEN (HAES IS very high)",
        "IF (weakness IS high) AND (edema IS high) AND (temp  IS high) AND (nausea IS low) THEN (HAES IS high)",
        "IF (weakness IS high) AND (edema IS high) AND (temp  IS low) AND (nausea IS high) THEN (HAES IS high)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS high) AND (nausea IS high) THEN (HAES IS high)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS high) AND (nausea IS high) THEN (HAES IS high)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS high) AND (nausea IS high) THEN (HAES IS medium)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS low) AND (nausea IS high) THEN (HAES IS medium)",
        "IF (weakness IS low) AND (edema IS high) AND (temp IS high) AND (nausea IS low) THEN (HAES IS medium)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS high) AND (nausea IS low) THEN (HAES IS medium)",
        "IF (weakness IS high) AND (edema IS high) AND (temp IS low) AND (nausea IS low) THEN (HAES IS medium)",
        "IF (weakness IS high) AND (edema IS low) AND (temp IS low) AND (nausea IS high) THEN (HAES IS medium)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS low) AND (nausea IS high) THEN (HAES IS low)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS high) AND (nausea IS low) THEN (HAES IS low)",
        "IF (weakness IS low) AND (edema IS high) AND (temp  IS low) AND (nausea IS low) THEN (HAES IS low)",
        "IF (weakness IS high) AND (edema IS low) AND (temp  IS low) AND (nausea IS low) THEN (HAES IS low)",
        "IF (weakness IS low) AND (edema IS low) AND (temp IS low) AND (nausea IS low) THEN (HAES IS low)",
    ])

    for key, value in user_answers.items():
        FS.set_variable(key, 1.1 if value == "+" else 0.5)

    res = FS.inference()
    return res


if __name__ == '__main__':
    user_answers = {
        "temp": True,
        "skin_t": True,
        "lymph": True,
        "weakness": True,
        "edema": True,
        "nausea": True,
        "stiffness": True,
        "noj": True,
        "back_pain": True,
        "mus_pain": True,
        "cancer": True,
    }
    print(get_fuzzy_ill_system(user_answers=user_answers))
