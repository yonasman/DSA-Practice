def date_slicer(date):
    year = date[0:4]
    month = date[5:7]
    day = date[8]
    return f"Year: {year} Month: {month} day:{day}"
print(date_slicer("2020-23-4"))
