from PIL import Image

file = raw_input("Nombre del archivo que queres convertir. Ejemplo: imagen.png\n")

im = Image.open(file)
pixels = im.load()


def aRGB(hex):
	h = hex.lstrip('#')
	return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def distance(rgb, hex):
	rgb2 = aRGB(hex)
	a = rgb[0] - rgb2[0]
	b = rgb[1] - rgb2[1]
	c = rgb[2] - rgb2[2]
	return abs(a) + abs(b) + abs(c)

def mamboColor(rgb, colors):
	closest = 1
	closestDistance = 999999
	for i in range(len(colors)):
		if distance(rgb,colors[i]) < closestDistance:
			closestDistance = distance(rgb,colors[i])
			closest = i
	#print closestDistance
	return closest + 1

def sinA(rgba):
	return (rgba[0], rgba[1], rgba[2])

colors = [
"#FFFFFF",
"#FFB3B3",
"#FFD1B3",
"#FFF0B3",
"#FFF7B3",
"#FFFFB3",
"#D7FFB3",
"#B3FFB3",
"#B3FFDF",
"#B3FFFF",
"#B3E0FF",
"#B3B3FF",
"#D0B3FF",
"#E9B3FF",
"#FFB3DA",
"#FFB3C3",
"#C8C8C8",
"#FF6666",
"#FFA366",
"#FFE066",
"#FFFF66",
"#DCFF66",
"#AFFF66",
"#66FF66",
"#66FFBF",
"#66FFFF",
"#66C0FF",
"#6666FF",
"#A066FF",
"#D266FF",
"#FF66B5",
"#FF6687",
"#969696",
"#FFFF00",
"#FF6600",
"#FFCC00",
"#FFFF00",
"#C5FF00",
"#7AFF00",
"#00FF00",
"#00FF94",
"#00FFFF",
"#0096FF",
"#0000FF",
"#6100FF",
"#B400FF",
"#FF0084",
"#FF0037",
"#494949",
"#7C0000",
"#7C3100",
"#7C6300",
"#7C7C00",
"#607C00",
"#3B7C00",
"#007C00",
"#007C48",
"#007C7C",
"#00497C",
"#00007C",
"#2F007C",
"#57007C",
"#7C0040",
"#5D0013",
"#000000",
"#3E0000",
"#3E1900",
"#3E3200",
"#3E3E00",
"#303E00",
"#1E3E00",
"#003E00",
"#003E24",
"#003E3E",
"#00243E",
"#00003E",
"#17003E",
"#2D003E",
"#3E0020",
"#3E000C",
"#7A7A7A",
"#D10000",
"#D15200",
"#D1A600",
"#D1D100",
"#A0D100",
"#64D100",
"#00D100",
"#00D178",
"#00D1D1",
"#007AD1",
"#0000D1",
"#4F00D1",
"#9200D1",
"#D1006B",
"#D1002D"]

salida = ""
for i in range(48): 
	for j in range(16): 
	    rgb = sinA(pixels[i, j])
	    mambo = mamboColor(rgb, colors)
	    salida += str(mambo) + ", "

text_file = open(file.split(".")[0] + ".mbo", "w")
text_file.write("%s" % salida)
text_file.close()

print ("Archivo generado: " + file.split(".")[0] + ".mbo\n")
