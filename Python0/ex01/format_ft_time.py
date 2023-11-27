import time
timestamp = time.time()

scientific_notation = format(timestamp, ".4e")

date_format = time.strftime("%b %d %Y", time.localtime(timestamp))

timestampFinal = "{:,.2f}".format(timestamp)

print(
    "Seconds since January 1, 1970: {} or {} in scientific notation"
    .format(timestampFinal, scientific_notation))
print(date_format)
