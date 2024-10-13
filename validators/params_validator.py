from lexicon import lexicon


def params_validator(params):
    if len(params) != 2:
        raise Exception(lexicon.PARAMS_VALIDATOR)
