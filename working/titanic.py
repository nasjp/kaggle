import random
import os
import numpy as np
import pandas as pd


def seed_everything(seed=1234) -> None:
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.randoom.seed(seed)
    # torch.manual_seed(seed)
    # torch.cuda.manual_seed(seed)
    # torch.backends.cudnn.deterministic = True


def load_after_processing_titanic_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv("../input/titanic/train.csv")
    test = pd.read_csv("../input/titanic/test.csv")
    gender_submission = pd.read_csv("../input/titanic/gender_submission.csv")

    data = pd.concat([train, test], sort=False)

    data["Sex"].replace(["male", "female"], [0, 1], inplace=True)

    data["Embarked"].fillna(("S"), inplace=True)
    data["Embarked"].replace(["S", "C", "Q"], [0, 1, 2], inplace=True)

    data["Fare"].fillna(np.mean(data["Fare"]), inplace=True)

    age_avg = data["Age"].mean()
    age_std = data["Age"].std()
    data["Age"].fillna(
        np.random.randint(age_avg - age_std, age_avg + age_std), inplace=True
    )

    data["FamilySize"] = data["SibSp"] + data["Parch"] + 1

    data["IsAlone"] = 0
    data[data["FamilySize"] == 1]["IsAlone"] = 1

    delete_columns = ["Name", "PassengerId", "SibSp", "Parch", "Ticket", "Cabin"]
    data.drop(delete_columns, axis=1, inplace=True)

    return (data[: len(train)], data[len(train) :])
