# Data: har bir harajak expences.json fayliga dict maulumot turida saqlandadi
# Misol: {"amount": 25.5, "category": "food", "note": "lunch"}

# load_expences(): nima qiladi? birinchi expences.json faylini oqidi u yerdan malumotlarni python fayliga otkazadi.
# save_expences(): nima oladi? yangi qoshilgan expence ni faylga saqlaydi.
# add_expences(): bu funksiya ishga tushganda userdan input olinadi, va shu user malumotlari dict ga saqlanadi va buni sva funksiyasi faylga saqlaydi.
# total_by_category(): bu funksiya userni qaysi harajatni kormi=oqchiligini sorab usha categoriya boyicha harajatlarni sum ni topib outputga chiqaradi.
import json

class Expences:
    def __init__(self, amount, category, notes):
        self.amount = amount
        self.category = category
        self.notes = notes

    def display_info(self):
        return f"Amount: {self.amount}, Category: {self.category}, Notes: {self.notes}"


def load_expences():
    try:
        with open("expences.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_expences(expences_dict):
    with open("expences.json", "w") as file:
        json.dump(expences_dict, file, indent=4)

def add_expences(expences_dict, amount, category, notes):
    expences_id = str(len(expences_dict) + 1)
    expences_dict[expences_id] = {
        "amount": amount,
        "category": category,
        "notes": notes
    }
    save_expences(expences_dict)

def total_b


