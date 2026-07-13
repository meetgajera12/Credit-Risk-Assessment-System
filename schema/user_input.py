from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field, field_validator


class Applicant(BaseModel):

    CODE_GENDER: str
    NAME_CONTRACT_TYPE: str
    NAME_INCOME_TYPE: str
    OCCUPATION_TYPE: str
    NAME_EDUCATION_TYPE: str
    NAME_FAMILY_STATUS: str
    FLAG_OWN_CAR: str
    FLAG_OWN_REALTY: str
    NAME_HOUSING_TYPE: str
    ORG_GROUP: str

    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    AMT_GOODS_PRICE: float

    CNT_CHILDREN: int
    CNT_FAM_MEMBERS: float

    AGE: float
    YEARS_EMPLOYED: float
    YEARS_CURRENT_PHONE: float

    FLAG_EMAIL: int = 0
    FLAG_WORK_PHONE: int = 0


    HAS_BUREAU_HISTORY: str

    YEARS_CREDIT_mean: float = 0

    DEBT_RATIO_mean: float = 0
    DEBT_RATIO_max: float = 0

    AMT_CREDIT_SUM_sum: float = 0
    AMT_CREDIT_SUM_mean: float = 0
    AMT_CREDIT_SUM_max: float = 0

    AMT_CREDIT_SUM_DEBT_sum: float = 0
    AMT_CREDIT_SUM_DEBT_mean: float = 0

    AMT_CREDIT_SUM_DEBT_MISSING_sum: float = 0
    AMT_CREDIT_SUM_DEBT_MISSING_mean: float = 0

    AMT_CREDIT_SUM_LIMIT_sum: float = 0
    AMT_CREDIT_SUM_LIMIT_MISSING_sum: float = 0
    AMT_CREDIT_SUM_LIMIT_MISSING_mean: float = 0

    CREDIT_UTILIZATION_mean: float = 0

    HAS_DEBT_sum: int = 0
    IS_ACTIVE_sum: int = 0
    IS_CLOSED_sum: int = 0
    IS_SOLD_sum: int = 0
    IS_BAD_DEBT_sum: int = 0
    YEARS_CREDIT_min: float = 0
    YEARS_CREDIT_max: float = 0

    PREV_APP_COUNT: int = 0
    APPROVAL_RATE: float = 0

