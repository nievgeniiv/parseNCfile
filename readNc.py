from scipy.io import netcdf
import sys

nc = netcdf.netcdf_file(str(sys.argv[1]))
param = [ 'longitude','latitude','level','time','cc','pv','r','clwc','q','t','u','v','w']
f = open('dataFromToFile.txt', 'w')
i = 0
while i <= len(param) - 1:
    if i < 4:
        f = open(param[i]+'.txt', 'w')
        f.write(param[i] + ' = \n')
        for x in nc.variables[param[i]][:]:
            f.write(str(x) + '\n')
        f.close()
    else:
        f = open(param[i]+'.txt', 'w')
        f.write(param[i] + ' = \n')
        f.write('[')
        for x in nc.variables[param[i]][:]:
            f.write('[')
            for k in x:
                f.write('[')
                for l in k:
                    f.write('[')
                    for r in l:
                        f.write(str(l) + '   ')
                    f.write(']   ')
                f.write(']   ')
            f.write(']   ')
        f.write(']   \n')
        f.close()
    i += 1
f.close()
