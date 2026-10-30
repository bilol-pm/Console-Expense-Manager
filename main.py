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

from expences import load_expences, save_expences, add_expences, total_by_category

if __name__ == "__main__":
    inventory = load_expences()
    print("Loading Expences...")
    while True:
        print("1. Add Expences")
        print("2. Sum by category")
        print("3. See all Expences")
        print("4. Delete Expences")
        print("5. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ")
        if choice == "1":
            adding_amount = int(input("Enter amount to add: "))
            adding_category = input("Enter category to add: ")
            adding_notes = input("Enter note to add: ")
            new_expence = Expences(adding_amount, adding_category, adding_notes)
            inventory = [
                {
                    "added_amount": {adding_amount},
                    "added_category": {adding_category},
                    "added_notes": {adding_notes}
                }
            ]
            expences.save_expences(inventory)
            print("Expences added.")
        elif choice == "2":
            print("")
        elif choice == "3":
            print("")
        elif choice == "4":
            print("")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice.")































