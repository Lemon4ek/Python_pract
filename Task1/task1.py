import re

rad=input("\nРядок: ")

print("\nРядок: ", rad)

el="".join(re.split("[0-9]+", rad))
en="".join(re.split("[a-zA-Z]+", rad))


elk=", ".join(el.split())
enk=", ".join(en.split())


print("\nЧисла: ", str(enk))

print("\nРяд без чисел: ", str(elk))


row_new_list=[]
for let in el.split():
    row_new_list.append(let[0].upper() + let[1:-1].lower() + let[-1].upper())
upper_let=" ".join(row_new_list)
print("\nВелика літера: ", upper_let)


new_num_max=list(map(int, en.split()))


max_num=max(new_num_max)


print("\nМаксимальне значення: ", max_num)



