def remove_dollar_sign(s):
    new_str = s.replace("$","")
    return new_str

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# print(string_with_no_dollars)
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")