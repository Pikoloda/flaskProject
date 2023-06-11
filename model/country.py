import json

def load_db():
    with open('country_info.json', encoding='utf-8') as mock_database:
        return json.load(mock_database)


def find_by_name(name: str):
    for country_data in db:
        if country_data['country'].casefold() == name.casefold():
            return country_data
    raise ValueError(f"Country {name} not found")

def find_by_index(index: int):
    return db[index]


db = load_db()