#


# def contains_dublicate_loop(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
#
# result = contains_dublicate_loop([1, 2, 3, ])
# print(result)
#
# assert contains_dublicate_loop([1, 2, 3, 1]) == True
# assert contains_dublicate_loop([1, 2, 3, 4]) == False
# assert contains_dublicate_loop([]) == False
# assert contains_dublicate_loop([5]) == False
# assert contains_dublicate_loop([7, 7]) == True
# print("All tests passed")
#
# def contains_dublicate_set(nums):
#     return len(nums) != len(set(nums))
#
# result = contains_dublicate_set([1,2,3,4,4])
# print(result)
#
# assert contains_dublicate_set([1, 2, 3, 1]) == True
# assert contains_dublicate_set([1, 2, 3, 4]) == False
# assert contains_dublicate_set([]) == False
# assert contains_dublicate_set([5]) == False
# assert contains_dublicate_set([7, 7]) == True
# print("All tests passed")
#
# def count_comparisons(nums):
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             count += 1
#     return count
#
# print(count_comparisons(list(range(1000))))

from expences import load_expences, save_expences, add_expences, total_by_category, delete_expence

if __name__ == "__main__":
    inventory = load_expences()
    print("Loading Expences...")
    while True:
        print("1. Add Expences")
        print("2. See all Expences")
        print("3. Sum by category")
        print("4. Sum all expences")
        print("5. Delete expence")
        print("6. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                try:
                    amount = float(input("Enter amount to add: "))
                    if amount <= 0:
                        print("Invalid amount!")
                        continue
                    break
                except ValueError:
                    print("Invalid amount!")
            category = input("Enter category to add: ")
            notes = input("Enter notes: ")

            add_expences(inventory, amount, category, notes)
            print("Expences added!")
        elif choice == "2":
            if not inventory:
                print("No expences yet!")
            else:
                for key, value in inventory.items():
                    print(f"ID: {key} | Amount: {value["amount"]} | Category: {value['category']} | Notes: {value['notes']}")
        elif choice == "3":
            totals = total_by_category(inventory)
            if not totals:
                print("No categories yet!")
            else:
                print("Total by category: ")
                for cat, total in totals.items():
                    print(f"- {cat}: {total}")
        elif choice == "4":
            total_sum = sum(exp["amount"] for exp in inventory.values())
            print(f"Tatal sum: {total_sum}")
        elif choice == "5":
            if not inventory:
                print("No expences to delete!")
            else:
                for key, value in inventory.items():
                    print(f"ID: {key} | Amount: {value['amount']} | Category: {value['category']} | Notes: {value['notes']}")
                exp_id = input("Enter expense ID: ")
                if delete_expence(inventory, exp_id):
                    print("Expense deleted successfully!")
                else:
                    print("Invalid ID! Expence not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice.")































