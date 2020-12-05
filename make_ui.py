#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform


def gen_ui(win, name):
    print(f'Generate UI {name}')
    if win:
        os.system('.\\venv\\Scripts\pyside2-uic.exe ui\\' + name + '.ui -o ui\\ui_' + name + '.py')
    else:
        os.system('pyside2-uic ui/' + name + '.ui -o ui/ui_' + name + '.py')


s = platform.platform()

w = False
if 'Windows' in s:
    print('Platform is windows')
    w = True
else:
    print('Platform is not windows')

gen_ui(w, 'MainWindow')
gen_ui(w, 'CharacterWidget')
gen_ui(w, 'PhaseWidget')
gen_ui(w, 'EncounterWidget')
gen_ui(w, 'NewGameWidget')
gen_ui(w, 'ActionWidget')
gen_ui(w, 'ActionsWidget')
gen_ui(w, 'TravelDecisionWidget')

print('Generate RC')
if w:
    os.system(".\\venv\\Scripts\pyside2-rcc.exe qrc\\badminapp.qrc -o badminapp_rc.py")
else:
    os.system('pyside2-rcc qrc/unbroken.qrc -o unbroken_rc.py')

print('locale')
os.system('pybabel extract .  --project unbroken -F babel.cfg -o locales/base.pot')
#os.system('pybabel init -l fr -i locales/unbroken.pot -d locales')
os.system('pybabel update -i locales/base.pot -d locales')
os.system('pybabel compile -d locales')

