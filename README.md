Aplicativo desktop para el departamento de tesorería de MINED v4.0.0

## Table of Contents

1. [Pre-requisites](#pre-requisites)
2. [Local Setup](#a-local-setup)

## Pre-requisites

- OS WINDOWS
- Python3.9
- Pyinstaller

## A. Local Setup

### Step 1: Clone the Repository & activate the virtual environment

### Step 2: Install Dependecies

### Step 3: Use the file config.py.template to set users

### Steps 1-2: Sumarized commands

```bash
git clone https://github.com/mined-academy/mass_payouts_binancepay.git
cd mass_payouts_binancepay/
git remote rename origin github
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

```

## Users

### We have two users in config

- admin
- viewer

## Create .exe

```bash
.\venv\Scripts\activate
pyinstaller.exe gui.spec
```

# Pyinstaller Commands

### Step 1: Activate the virtual environment

### Step 2: Run pyinstaller

```bash
.\venv\Scripts\activate
pyinstaller.exe gui.spec
```

<!--
old version
pyinstaller.exe -F .\gui.py
-->
