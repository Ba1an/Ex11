ean_country_codes = {
    '013': 'Канада',
    '037': 'Франция',
    '380': 'Болгария',
    '383': 'Словения',
    '385': 'Хорватия',
    '400': 'Германия',
    '050': 'Великобритания',
    '045': 'Япония',
    '460': 'Россия',
    '470': 'Киргизия',
    '471': 'Тайвань',
    '474': 'Эстония',
    '475': 'Латвия',
    '476': 'Азербайджан',
    '477': 'Литва',
    '478': 'Узбекистан',
    '479': 'Шри-Ланка',
    '480': 'Филиппины',
    '093': 'Австралия',
    '069': 'Китай',
    '789': 'Бразилия',
    '890': 'Индия',
    '080': 'Италия',
    '084': 'Испания',
    '088': 'Южная Корея',
    '750': 'Мексика',
    '779': 'Аргентина',
    '600': 'Южная Африка'
}


ean_country_codes_swapped = {value: key for key, value in ean_country_codes.items()}
print(ean_country_codes_swapped)