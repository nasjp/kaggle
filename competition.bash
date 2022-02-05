#!/bin/bash

competition=$1

function activate_venv() {
		source .venv/bin/activate
}

function validate_competition() {
		if [ -z "$competition" ]; then
				echo "Please provide a competition name"
				exit 1
		fi
}

function download_competition_data() {
		kaggle competitions download -c $competition
}

function extract_competition_data() {
		kaggle competitions datasets -c $competition
}


activate_venv
validate_competition
download_competition_data
