def clean(txt):
    txt = txt.replace('&middot;', '*')
    return txt.replace('<br />', '\n')

t = """4gb &middot; 01 ellesmere rx 470 113-1e3471u.s5n elpida (113-1e3471u.s5n) &middot; edw4032babg<br />4gb &middot; 02 ellesmere rx 470 113-1e3471u.s5n elpida (113-1e3471u.s5n) &middot; edw4032babg<br />8gb &middot; 05 ellesmere rx 470 113-1e3470u.s61 samsung (113-1e3470u.s61) &middot; k4g80325fb<br />8gb &middot; 06 ellesmere rx 470 113-1e3470u.s61 samsung (113-1e3470u.s61) &middot; k4g80325fb<br />4gb &middot; 09 ellesmere rx 470 113-1e3471u.o5o elpida (113-1e3471u.o5o) &middot; edw4032babg<br />8gb &middot; 0a ellesmere rx 470 113-1e3470u.s61 samsung (113-1e3470u.s61) &middot; k4g80325fb"""


print(clean(t))