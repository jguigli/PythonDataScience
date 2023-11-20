import time

# Obtenez le timestamp Unix actuel en secondes
timestamp = time.time()

# Convertissez le timestamp en notation scientifique
scientific_notation = format(timestamp, ".4e")

# Convertissez le timestamp en une date lisible
date_format = time.strftime("%b %d %Y", time.localtime(timestamp))

timestampFinal = "{:,.2f}".format(timestamp)

# Affichez les résultats
print("Seconds since January 1, 1970: {} or {} in scientific notation".format(timestampFinal, scientific_notation))
print(date_format)
