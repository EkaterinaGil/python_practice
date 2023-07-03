var_1 = 37
var_2 = 99
# var_buf = 0

# var_buf = var_1
# var_1 = var_2
# var_2 = var_buf

# print(var_1, var_2)

var_1, var_2 = var_2, var_1
print("var_1 =", var_1, "var_2 =", var_2)
