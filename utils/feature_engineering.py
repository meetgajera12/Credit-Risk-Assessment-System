import numpy as np
import pandas as pd


def create_features(df):

    df = df.copy()

    # =====================================================
    # Application Features
    # =====================================================

    df['CREDIT_INCOME_RATIO'] = np.where(
        df['AMT_INCOME_TOTAL'] > 0,
        df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL'],
        0
    ).round(4)

    df['ANNUITY_INCOME_RATIO'] = np.where(
        df['AMT_INCOME_TOTAL'] > 0,
        df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL'],
        0
    ).round(4)

    df['CREDIT_ANNUITY_RATIO'] = np.where(
        df['AMT_ANNUITY'] > 0,
        df['AMT_CREDIT'] / df['AMT_ANNUITY'],
        0
    ).round(4)

    df['GOODS_CREDIT_RATIO'] = np.where(
        df['AMT_CREDIT'] > 0,
        df['AMT_GOODS_PRICE'] / df['AMT_CREDIT'],
        0
    ).round(4)

    df['INCOME_PER_FAM_MEMBER'] = np.where(
        df['CNT_FAM_MEMBERS'] > 0,
        df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS'],
        0
    ).round(4)

    df['EMPLOYMENT_AGE_RATIO'] = np.where(
        df['AGE'] > 0,
        df['YEARS_EMPLOYED'] / df['AGE'],
        0
    ).round(4)

    df['HAS_DEPENDENTS'] = (df['CNT_CHILDREN'] > 0).astype(int)

    df['IS_SINGLE_PARENT'] = (
        (df['CNT_CHILDREN'] > 0) &
        (df['NAME_FAMILY_STATUS'] == 'Single / not married')
    ).astype(int)

    df['OCCUPATION_TYPE_MISSING'] = df['OCCUPATION_TYPE'].isna().astype(int)

    # =====================================================
    # Bureau Features
    # =====================================================

    if df.loc[0, 'HAS_BUREAU_HISTORY'] == 0:

        bureau_cols = [
            'YEARS_CREDIT_mean',
            'DEBT_RATIO_mean',
            'DEBT_RATIO_max',
            'AMT_CREDIT_SUM_sum',
            'AMT_CREDIT_SUM_mean',
            'AMT_CREDIT_SUM_max',
            'AMT_CREDIT_SUM_DEBT_sum',
            'AMT_CREDIT_SUM_DEBT_mean',
            'AMT_CREDIT_SUM_DEBT_MISSING_sum',
            'AMT_CREDIT_SUM_DEBT_MISSING_mean',
            'AMT_CREDIT_SUM_LIMIT_sum',
            'AMT_CREDIT_SUM_LIMIT_MISSING_sum',
            'AMT_CREDIT_SUM_LIMIT_MISSING_mean',
            'CREDIT_UTILIZATION_mean',
            'HAS_DEBT_sum',
            'IS_ACTIVE_sum',
            'IS_CLOSED_sum',
            'IS_SOLD_sum',
            'IS_BAD_DEBT_sum',
            'YEARS_CREDIT_min',
            'YEARS_CREDIT_max'
        ]

        for col in bureau_cols:
            df[col] = 0

    # =====================================================
    # Previous Application Features
    # =====================================================

    if df.loc[0, 'PREV_APP_COUNT'] == 0:        # counts how many previous applications each customer has made.

        df['APPROVAL_RATE'] = 0



    return df
