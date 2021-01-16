# จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "Python is one of the fastest-growing programming languages"
string1 = "Python is one of the fastest-growing programming languages"
print(len(string1))

# จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "Python is one of the fastest-growing programming languages"
string2 = "Python is one of the fastest-growing programming languages"
print(string2[0])

# จงเขียนคำสั่งเพื่อแสดง "fastest" ของข้อความ "Python is one of the fastest-growing programming languages"
string3 = "Python is one of the fastest-growing programming languages"
print(string3[21:28])

# จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ไม่มี space
string4 = "Python is one of the fastest-growing programming languages"
print(string4.replace(" ", ""))

# จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมใหญ่ทั้งหมด
string5 = "Python is one of the fastest-growing programming languages"
print(string5.upper())

# จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมเล็กทั้งหมด
string6 = "Python is one of the fastest-growing programming languages"
print(string6.lower())

# จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ถูกแทนที่อักษร r ด้วย x ทั้งหมด
string7 = "Python is one of the fastest-growing programming languages"
print(string7.replace("r", "x"))

# จงเติมคำในช่องว่าเพื่อแสดงอายุ
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))