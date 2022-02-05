#!/bin/bash

competition=$1

if [ -z "$competition" ]; then
	echo "Please provide a competition name"
	exit 1
fi

source .venv/bin/activate
kaggle competitions download -c $competition --force
unzip -f $competition.zip -d input/$competition
cp template.ipynb working/$competition.ipynb
rm $competition.zip