import redis

conn = redis.Redis(host="localhost", port=6379, db=0)

# conn.set("phone_number", "+998905660312")
# print(conn.get("phone_number"))



# Uyga vazifa 9 dars



# ===================================================================================


# conn.set("adress", "Fargona")
# print(str(conn.get("adress"), "utf-8"))
#
# # ===================================================================================
#
#
# if conn.exists("adress"):
#     conn.set("adress", "Beshariq")
#     print(f"{"adress"} o'zgartirildi. Yangi qiymat: {"Beshariq"}")
# else:
#     print(f"{"adress"} mavjud emas.")
#
# # ===================================================================================
#
# conn.setex("q", "300", "400")
# print(str(conn.get("q"), "utf-8"))

# ===================================================================================


# a = conn.getset("adress", "Fargona")
#
# if a:
#     print(f"Eski qiymat: {str(conn.get("adress"), "utf-8")}")
# else:
#     print(f"{"adress"} uchun qiymat mavjud emas edi.")
#
# print(f"{"adress"} ning yangi qiymati: {"Beshariq"}")


# ===================================================================================

# conn.incrby("q", "100")
# print(str(conn.get("q"), "utf-8"))

# ===================================================================================

# conn.decrby("q", "100")
# print(str(conn.get("q"), "utf-8"))

# ===================================================================================

# print(conn.ttl("q"))

# ===================================================================================

# data = {
#     "ism1": "Asilbek1",
#     "ism2": "Asilbek2",
#     "ism3": "Asilbek3"
# }
#
# conn.mset(data)
# print(conn.mget("ism1", "ism2", "ism3"))

# ===================================================================================

# conn.append("adress", " viloyati Beshariq tumani.")
# print(str(conn.get("adress"), "utf-8"))

# ===================================================================================


# print(str(conn.getrange("adress", "0", "31"), "utf-8"))

# ===================================================================================

# conn.setrange("adress", 7, " viloyati Beshariq tumani.")
# print(str(conn.get("adress"), "utf-8"))

# ===================================================================================

# conn.delete("adress")
# print(str(conn.get("adress"), "utf-8"))

# ===================================================================================

# print(f"Eski qiymat: {str(conn.get("name"), "utf-8")}")
# old_value = conn.getset("name", "Rustamov")
# print(f"Yangi qiymat: {str(conn.get("name"), "utf-8")}")

# ===================================================================================

# print(conn.strlen("name"))

# ===================================================================================

# conn.delete("name")
# result = conn.set("name", "Asilbek", nx=True)
# if result:
#     print(f"name kalitiga {str(conn.get("name"), "utf-8")} qiymati o'rnatildi.")
# else:
#     print(f"name kaliti allaqachon mavjud, qiymat o'zgarmadi.")

# ===================================================================================

# a = conn.getset("name", "Rustamov")
#
# if a:
#     print(f"Eski qiymat: {a.decode('utf-8')}")
# else:
#     print("Kalit mavjud emas, yangi qiymat o'rnatildi.")

# ===================================================================================

# conn.append("name", " Asilbek ")
# print(f"Yangilangan qiymat: { conn.get("name").decode('utf-8')}")

# ===================================================================================

# print(conn.type("name"))

# ===================================================================================

# a = input("qaysi keydi qidirmoqchisiz: ")
# keys = conn.keys()
# if [key.decode('utf-8') for key in keys].count(a) > 0:
#     print("Siz qidirgan kalit bizda mavzud !")
# else:
#     print("Kechirasiz bunday kalit hali qoshilmadian !")

# ===================================================================================
















conn.close()