import datetime
import decimal


def adapt_data_for_json(data):
    """Преобразует полученные данные при запросе из SQL, в формат, удобный для записи в JSON."""
    adapted_data = []
    for item in data:
        adapted_item = []
        for field in item:
            if isinstance(field, decimal.Decimal):
                adapted_item.append(float(field))
            elif isinstance(field, datetime.date):
                # заметка для себя: преобразует в стандарт ISO 8601.
                adapted_item.append(field.isoformat())
                # adapted_item.append(str(field))
            else:
                adapted_item.append(field)
        adapted_data.append(adapted_item)
    return adapted_data
