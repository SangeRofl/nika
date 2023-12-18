from sys import argv

concepts = """concept_inflectional_language-флективный язык;
    concept_agglutinative_language-агглютинативный язык;
    concept_isolating_language-изолюрующий язык;
    concpet_incorporating_language-инкорпорирующий язык;

    concept_active_language-активный язык;
    concept_nominative_language-номинативный язык;
    concept_ergative_language-эргативный язык;

    concept_analytical_language-аналитический язык;
    concept_synthetic_language-синтетический язык;

    concept_independent_part_of_speech-самостоятельная часть речи;
    concept_function_part_of_speech-служебная часть речи;
    concept_noun_part_of_speech-имя существительное;
    concept_adjective_part_of_speech-имя прилагательное;
    concept_adverb_part_of_speech-наречие;
    concept_verb_part_of_speech-глагол;
    concept_numeral_part_of_speech-имя числительное;
    concept_pronoun_part_of_speech-местоимение;
    concept_preposition_part_of_speech-предлоги;
    concept_postposition_part_of_speech-послелоги;
    concept_particle_part_of_speech-частица;
    concept_article_part_of_speech-артикль;
    concept_conjunction_part_of_speech-союз;

    concept_root_morpheme-корень;
    concept_affix_morpheme-аффикс;

    concept_narrative_sentence-повествовательное предложение;
    concept_interrogative_sentence-вопросительное предложение;
    concept_imperative_sentence-побудительное предложение;
    concept_exclamative_sentence-восклицательное предложение;
    concept_sentence-предложение;
    concept_letter-буква;
    concept_morpheme-морфема"""

with open(argv[1], "rt", encoding="utf-8") as f:
    template = f.read()
print(argv)

concepts = concepts.split(";")
concepts = [i.strip().split("-") for i in concepts]
for i in concepts:
    with open(argv[2]+"\\"+i[0]+".scs", "wt", encoding="utf-8") as f:
        data = template.replace("NAME", i[0])
        data = data.replace("NM_IDTF", i[1])
        f.write(data)