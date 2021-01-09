#!/bin/sh
python3 scripts/locale_convert.py --input orig-locale/de/strings.txt --output LaserTank-Extended/asset/locale/de.json --lang de
python3 scripts/locale_convert.py --input orig-locale/en/strings.txt --output LaserTank-Extended/asset/locale/en.json --lang en
python3 scripts/locale_convert.py --input orig-locale/es/strings.txt --output LaserTank-Extended/asset/locale/es.json --lang es
python3 scripts/locale_convert.py --input orig-locale/fr/strings.txt --output LaserTank-Extended/asset/locale/fr.json --lang fr
python3 scripts/locale_convert.py --input orig-locale/hr/strings.txt --output LaserTank-Extended/asset/locale/hr.json --lang hr
python3 scripts/locale_convert.py --input orig-locale/nl/strings.txt --output LaserTank-Extended/asset/locale/nl.json --lang nl
python3 scripts/locale_convert.py --input orig-locale/pt/strings.txt --output LaserTank-Extended/asset/locale/pt.json --lang pt
python3 scripts/locale_convert.py --input orig-locale/sr/strings.txt --output LaserTank-Extended/asset/locale/sr.json --lang sr
python3 scripts/locale_convert.py --input orig-locale/sv/strings.txt --output LaserTank-Extended/asset/locale/sv.json --lang sv
python3 scripts/locale_convert.py --input orig-locale/tr/strings.txt --output LaserTank-Extended/asset/locale/tr.json --lang tr
python3 scripts/locale_convert.py --input orig-locale/zc/strings.txt --output LaserTank-Extended/asset/locale/zc.json --lang zc
python3 scripts/locale_convert.py --input orig-locale/zh/strings.txt --output LaserTank-Extended/asset/locale/zh.json --lang zh
