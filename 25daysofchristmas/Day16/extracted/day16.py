from zipfile import ZipFile
import os
import re  


files = '''ab.zip   a.zip     dec.zip  eq.zip                      gen.zip  it.zip   pf.zip    te.zip   what.zip
ad.zip   cd.zip    edm.zip  fb.zip                      idk.zip  nm.zip   qq.zip    tm.zip   word.zip
and.zip  eg.zip  io.zip   owg.zip  rand.zip  uuu.zip  xt.zip'''

files = files.rstrip().split()
number_unzipped = 0
number_v11 = 0

passwd_ans = []
v11_ans = []

print(files)

for zip_file in files:
    with ZipFile(zip_file, 'r') as zipped:
        for info in zipped.infolist():
            number_unzipped += 1
            data = zipped.read(info.filename)
            if re.findall(rb"password", data) != []:
                passwd_ans.append(info.filename)
            if re.findall(rb"1\.1", data) != []:
                number_v11 += 1
                v11_ans.append(info.filename)

    os.remove(zip_file)

print("[*] Total files extracted: {}".format(number_unzipped))
print("[*] Version 1.1: {}".format(number_v11))
print("[*] files with password :")
print(passwd_ans)

# t = "wfjbno wpofjwopfwpfowwfw ifjwfjflf 1111.123 fjdwnfowowh"
# print(re.findall(r"....\....", t))