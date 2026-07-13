binary_map = {
    'CODE_GENDER':{'F':0,'M':1},
    'FLAG_OWN_CAR':{'No':0,'YES':1},
    'FLAG_OWN_REALTY':{'No':0,'Yes':1},
    'NAME_CONTRACT_TYPE':{'Revolving loans':0,'Cash loans':1},
    'HAS_BUREAU_HISTORY':{'No':0,'Yes':1}
}

def apply_binary_mapping(df):
    df = df.copy()

    for col, mapping in binary_map.items():
        df[col] = df[col].map(mapping)

    return df