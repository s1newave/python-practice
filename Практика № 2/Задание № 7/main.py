file = open("klinika.txt", "r")

lines = [x.replace("\n", "") for x in file.readlines()]

keys = ["Фамилия", "Пол", "Возраст", "Город", "Диагноз"]
patients = [dict(zip(keys, x.split())) for x in lines]

youngest = min(patients, key=lambda x: x.get("Возраст"))
print(
    youngest.get("Фамилия"),
    youngest.get("Возраст"),
    youngest.get("Диагноз")
)
