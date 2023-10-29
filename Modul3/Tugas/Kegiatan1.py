def convert(minggu, hari, jam, menit):
    return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

outputdata = []
for item in data:
    split = item.split()
    minggu = int(split[0])
    hari = int(split[2])
    jam = int(split[4])
    menit = int(split[6])

    result = convert(minggu, hari, jam, menit)
    outputdata.append(result)

print("OutputData =", outputdata)