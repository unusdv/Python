"""
File - bu ma'lum tipdagi baytlar uchun ajratilgan
xotira maydoni.

Stream - qay miqdorda va qachon ma'lumot kelishi aniq bo'lmagan
holda ishlatiluvchi vosita.
"""
"""
C Files
Fopen, Fclose
fprintf, fputc, fputs
fscanf, fgetc, fgets
fseek, ftell

FILE * f = fopen("", "");

w - write
r - read
a - append
"""
f = open("1.txt", "w")

f.write("Foundation\n")
f.write("N19\n" * 4)

print(f.readable())

lst = ["Apple", "Google", "Microsoft"]
f.writelines(lst)

f.close()
