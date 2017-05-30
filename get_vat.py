def get_vat(payment):
    try:
        payment = float(payment)
        vat = payment / 100 * 18
        return round(vat, 2)
    except (TypeError, ValueError):
        return('Не пра виль ьно все блеа!')


result = get_vat('dfghjk')
print('Сумма НДС: {}'.format(result))