import numpy as np
import matplotlib.pyplot as plt


def rdfile(filename):
    data = np.loadtxt(filename)
    return data


def retrievedata(data, darray, param):
    for x in darray:
        data.append(x[param])
    return data


def sumall(darray, param):
    return sum([x[param] for x in darray])


#  files with parameter indnum=100 cycles=10000
f1 = rdfile("inout/rezs0.txt")
f2 = rdfile("inout/rezs1.txt")
f3 = rdfile("inout/rezs2.txt")
f4 = rdfile("inout/rezsn.txt")
#  files with parameter indnum=200 cycles=5000
f11 = rdfile("inout/rezs01.txt")
f21 = rdfile("inout/rezs11.txt")
f31 = rdfile("inout/rezs21.txt")
f41 = rdfile("inout/rezsn1.txt")
#  files with parameter indnum=400 cycles=5000 and a stop on 2000 cycles no change of max
ft1 = rdfile("inout/rezst0.txt")
ft2 = rdfile("inout/rezst1.txt")
ft3 = rdfile("inout/rezst2.txt")
ft4 = rdfile("inout/rezstn.txt")

alltimes = []
alltimes = retrievedata(alltimes, f1, 0)
alltimes = retrievedata(alltimes, f2, 0)
alltimes = retrievedata(alltimes, f3, 0)
alltimes = retrievedata(alltimes, f4, 0)
alltimes = retrievedata(alltimes, f11, 0)
alltimes = retrievedata(alltimes, f21, 0)
alltimes = retrievedata(alltimes, f31, 0)
alltimes = retrievedata(alltimes, f41, 0)
alltimes = retrievedata(alltimes, ft1, 0)
alltimes = retrievedata(alltimes, ft2, 0)
alltimes = retrievedata(alltimes, ft3, 0)
alltimes = retrievedata(alltimes, ft4, 0)

allacc = []
allacc = retrievedata(allacc, f1, 1)
allacc = retrievedata(allacc, f2, 1)
allacc = retrievedata(allacc, f3, 1)
allacc = retrievedata(allacc, f4, 1)
allacc = retrievedata(allacc, f11, 1)
allacc = retrievedata(allacc, f21, 1)
allacc = retrievedata(allacc, f31, 1)
allacc = retrievedata(allacc, f41, 1)
allacc = retrievedata(allacc, ft1, 1)
allacc = retrievedata(allacc, ft2, 1)
allacc = retrievedata(allacc, ft3, 1)
allacc = retrievedata(allacc, ft4, 1)

timeavg = sum(alltimes) / len(alltimes)
accavg = sum(allacc) / len(allacc)
t1 = [sumall(f1, 0) / len(f1), sumall(f11, 0) / len(f11), sumall(ft1, 0) / len(ft1)]
t2 = [sumall(f2, 0) / len(f2), sumall(f21, 0) / len(f21), sumall(ft2, 0) / len(ft2)]
t3 = [sumall(f3, 0) / len(f3), sumall(f31, 0) / len(f31), sumall(ft3, 0) / len(ft3)]
t4 = [sumall(f4, 0) / len(f4), sumall(f41, 0) / len(f41), sumall(ft4, 0) / len(ft4)]
a1 = [sumall(f1, 1) / len(f1), sumall(f11, 1) / len(f11), sumall(ft1, 1) / len(ft1)]
a2 = [sumall(f2, 1) / len(f2), sumall(f21, 1) / len(f21), sumall(ft2, 1) / len(ft2)]
a3 = [sumall(f3, 1) / len(f3), sumall(f31, 1) / len(f31), sumall(ft3, 1) / len(ft3)]
a4 = [sumall(f4, 1) / len(f4), sumall(f41, 1) / len(f41), sumall(ft4, 1) / len(ft4)]

arrx = [148, 170, 157, 227]
arry = [100, 100, 100, 100]
# the histogram of the data
plt.figure(figsize=(20, 15))

plt.subplot(221)

plt.grid(True, alpha=0.5, ls='--')

plt.hist(alltimes, 100, alpha=0.90)
plt.xlabel('Laikas(s)')
plt.ylabel('Pasikartojimai')
plt.title('Skaičiavimams užimamo laiko histograma')
plt.annotate('Raudonos brūkšninės linijos žymi pilnuojo perrinkimo būdu gautų rezultatų poziciją', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.annotate('sqr0', xy=(148, 225), xytext=(50, 225),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqr1', xy=(170, 250), xytext=(250, 250),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqr2', xy=(157, 275), xytext=(100, 275),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqrn', xy=(227, 150), xytext=(300, 150),
             arrowprops=dict(facecolor='black', shrink=0.05),)
#  plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#  plt.xlim(40, 160)
#  plt.ylim(0, 0.03)
plt.xticks(np.arange(0, 700, 50))
plt.yticks(np.arange(0, 300, 25))
plt.axvline(148, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(170, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(157, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(227, color='r', linestyle='dashed', linewidth=1, zorder=0)

plt.subplot(222)

plt.grid(True, alpha=0.5, ls='--')

plt.hist(allacc, 100, alpha=0.90)
plt.axvline(100, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Tikslumo histograma')
plt.annotate('Raudona brūkšninė linija žymi pilnuojo perrinkimo būdu gautų rezultatų poziciją', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')

plt.subplot(223)

plt.grid(True, alpha=0.5, ls='--')

plt.plot(arrx, arry, 'bo')
plt.plot(timeavg, accavg, 'ro')
plt.xlabel('Laikas(s)')
plt.ylabel('Tikslumas(%)')
plt.title('Pilno perrinkimo tikslumai, lyginant su vidutiniu visų skaičiavimų tikslumu')
plt.yticks(np.arange(40, 110, 10))
plt.xticks(np.arange(140, 260, 10))

plt.subplot(224)

plt.grid(True, alpha=0.5, ls='--')

plt.plot(arrx[0], arry[0], 'b^')
plt.plot(t1, a1, 'bo')
plt.plot(arrx[1], arry[1], 'g^')
plt.plot(t2, a2, 'go')
plt.plot(arrx[2], arry[2], 'r^')
plt.plot(t3, a3, 'ro')
plt.plot(arrx[3], arry[3], 'k^')
plt.plot(t4, a4, 'ko')
plt.plot(t1, a1, label='sqr0', color='b')
plt.plot(t2, a2, label='sqr1', color='g')
plt.plot(t3, a3, label='sqr2', color='r')
plt.plot(t4, a4, label='sqr3', color='k')
plt.yticks(np.arange(30, 110, 10))

plt.xlabel('Laikas(s)')
plt.ylabel('Tikslumas(%)')
plt.title('Pilno perrinkimo tikslumai, lyginant su vidutiniais failų skaičiavimų tikslumais.')
plt.legend(loc=4)
plt.annotate('Apskritimais pažymėti biogeoografiniai skaičiavimai, trikampiais - pilnojo perrinkimo.\nTaip pat matomas'
             ' ir bandymų nuoseklumas. Pirmas bandymas yra kairiausias,\npaskutinis - dešiniausias atitinkamose spalvos'
             'e.', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.savefig('inout/grafikas.png', bbox_inches='tight')

