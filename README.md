# README

# setup

```sh
asdf install
python -m pip install -r requirements.txt
```

# init competition

```sh
./competition.bash titanic
```

# directory structure

```sh
kaggle
├── input
│   └── titanic
│       ├── gender_submission.csv
│       ├── test.csv
│       └── train.csv
├── lib
│   └── kaggle
│       └── gcp.py
└── working
    └── titanic.ipynb
```

# dependencies

- cmake
- libomp

```sh
brew install cmake libomp
```
