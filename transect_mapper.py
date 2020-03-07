from tkinter import *
from tkinter.ttk import * 
from PIL import Image
i0 = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
i9 = 0
i10 = 0
i11 = 0
i12 = 0
i13 = 0
i14 = 0
i15 = 0
i16 = 0
i17 = 0
i18 = 0
i19 = 0
i20 = 0
i21 = 0
i22 = 0
i23 = 0
i24 = 0
i25 = 0
i26 = 0
root = Tk()

root.title("Transect Mapper Window")

root.geometry("1000x1000")

mpt = PhotoImage(file = r"C:\Users\Dhruv\Pictures\mpt.png")
ycrc = PhotoImage(file = r"C:\Users\Dhruv\Pictures\ycrc.png")
bcrc = PhotoImage(file = r"C:\Users\Dhruv\Pictures\bcrc.png")
gcrc = PhotoImage(file = r"C:\Users\Dhruv\Pictures\gcrc.png")
ovu = PhotoImage(file = r"C:\Users\Dhruv\Pictures\ovu.png")
ovd = PhotoImage(file = r"C:\Users\Dhruv\Pictures\ovd.png")
ovr = PhotoImage(file = r"C:\Users\Dhruv\Pictures\ovr.png")
ovl = PhotoImage(file = r"C:\Users\Dhruv\Pictures\ovl.png")
imgs = [mpt, ycrc, bcrc, gcrc, ovu, ovd, ovr, ovl]

def butswap0_0():
	global i0
	i0 = i0+1
	a = i0%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap0_0).grid(row = 0, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap0_0).grid(row = 0, column = 0)

def butswap0_1():
	global i1
	i1 = i1+1
	a = i1%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap0_1).grid(row = 0, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap0_1).grid(row = 0, column = 1)

def butswap0_2():
	global i2
	i2 = i2+1
	a = i2%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap0_2).grid(row = 0, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap0_2).grid(row = 0, column = 2)

def butswap1_0():
	global i3
	i3 = i3+1
	a = i3%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap1_0).grid(row = 1, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap1_0).grid(row = 1, column = 0)

def butswap1_1():
	global i4
	i4 = i4+1
	a = i4%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap1_1).grid(row = 1, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap1_1).grid(row = 1, column = 1)

def butswap1_2():
	global i5
	i5 = i5+1
	a = i5%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap1_2).grid(row = 1, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap1_2).grid(row = 1, column = 2)

def butswap2_0():
	global i6
	i6 = i6+1
	a = i6%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap2_0).grid(row = 2, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap2_0).grid(row = 2, column = 0)

def butswap2_1():
	global i7
	i7 = i7+1
	a = i7%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap2_1).grid(row = 2, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap2_1).grid(row = 2, column = 1)

def butswap2_2():
	global i8
	i8 = i8+1
	a = i8%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap2_2).grid(row = 2, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap2_2).grid(row = 2, column = 2)

def butswap3_0():
	global i9
	i9 = i9+1
	a = i9%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap3_0).grid(row = 3, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap3_0).grid(row = 3, column = 0)

def butswap3_1():
	global i10
	i10 = i10+1
	a = i10%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap3_1).grid(row = 3, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap3_1).grid(row = 3, column = 1)

def butswap3_2():
	global i11
	i11 = i11+1
	a = i11%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap3_2).grid(row = 3, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap3_2).grid(row = 3, column = 2)

def butswap4_0():
	global i12
	i12 = i12+1
	a = i12%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap4_0).grid(row = 4, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap4_0).grid(row = 4, column = 0)

def butswap4_1():
	global i13
	i13 = i13+1
	a = i13%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap4_1).grid(row = 4, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap4_1).grid(row = 4, column = 1)

def butswap4_2():
	global i14
	i14 = i14+1
	a = i14%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap4_2).grid(row = 4, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap4_2).grid(row = 4, column = 2)

def butswap5_0():
	global i15
	i15 = i15+1
	a = i15%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap5_0).grid(row = 5, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap5_0).grid(row = 5, column = 0)

def butswap5_1():
	global i16
	i16 = i16+1
	a = i16%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap5_1).grid(row = 5, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap5_1).grid(row = 5, column = 1)

def butswap5_2():
	global i17
	i17 = i17+1
	a = i17%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap5_2).grid(row = 5, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap5_2).grid(row = 5, column = 2)

def butswap6_0():
	global i18
	i18 = i18+1
	a = i18%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap6_0).grid(row = 6, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap6_0).grid(row = 6, column = 0)

def butswap6_1():
	global i19
	i19 = i19+1
	a = i19%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap6_1).grid(row = 6, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap6_1).grid(row = 6, column = 1)

def butswap6_2():
	global i20
	i20 = i20+1
	a = i20%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap6_2).grid(row = 6, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap6_2).grid(row = 6, column = 2)

def butswap7_0():
	global i21
	i21 = i21+1
	a = i21%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap7_0).grid(row = 7, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap7_0).grid(row = 7, column = 0)

def butswap7_1():
	global i22
	i22 = i22+1
	a = i22%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap7_1).grid(row = 7, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap7_1).grid(row = 7, column = 1)

def butswap7_2():
	global i23
	i23 = i23+1
	a = i23%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap7_2).grid(row = 7, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap7_2).grid(row = 7, column = 2)

def butswap8_0():
	global i24
	i24 = i24+1
	a = i24%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap8_0).grid(row = 8, column = 0)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap8_0).grid(row = 8, column = 0)

def butswap8_1():
	global i25
	i25 = i25+1
	a = i25%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap8_1).grid(row = 8, column = 1)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap8_1).grid(row = 8, column = 1)

def butswap8_2():
	global i26
	i26 = i26+1
	a = i26%8
	stgImg = imgs[a]
	Button(root, text = 'Click Me !', image = imgs[a], command=butswap8_2).grid(row = 8, column = 2)
	return
Button(root, text = 'Click Me !', image = mpt, command=butswap8_2).grid(row = 8, column = 2)

root.mainloop()