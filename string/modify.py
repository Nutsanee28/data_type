string = " hello, world! "

print(string.upper())  # กลายเป็นพิมพ์ใหญ่ทั้งหมด
print(string.lower())  # กลายเป็นพิมพ์เล็กทั้งหมด
print(string.strip())  # ตัดช่องว่างหัวเเละท้ายข้อความทิ้ง
print(
    string.replace("h", "j")
)  # เเทนที่โดยตัวหน้าคือตัวที่ต้องการทับ ตัวหลังคือตัวที่ต้องการเอามาเเทน
print(string.split(","))  # ตัดประโยคที่มีเครื่องหมายที่กำหนดออกจากกัน
print(len(string))  # นับจำนวนอักขระทั้งหมด
