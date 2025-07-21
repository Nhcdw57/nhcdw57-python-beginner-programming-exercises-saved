# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for count in range(99,-1,-1):
        if count == 2:
            print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
        elif count == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif count == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"{count} bottles of milk on the wall, {count} bottles of milk. Take one down and pass it around, {count-1} bottles of milk on the wall.")

number_of_bottles()