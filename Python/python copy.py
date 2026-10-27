# import matplotlib.pyplot as plt
# c = ['0','da','ds']
# f = ['0',"40k","65k"]
# plt.bar(c,f,color ="r")
# # o,*,s,^,x,d
# # --,- :,-.
# plt.title("Exellence technologies")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.show()
import matplotlib.pyplot as plt
c = ['0','da','ds',"cs"]            # o,*,s,^,x,d
f = [0,40,65,1]                     # --,- :,-.
plt.style.use("ggplot")
# plt.style.use("classic")
plt.style.use("dark_background")
plt.style.use("Solarize_Light2")
plt.plot(c,f,color ="r",marker = "o",linestyle ="--", mfc = 'g', mec = "r", linewidth = 2, markersize = 8, label = "Exellence technologies")
plt.fill_between(c,f,color = "red",alpha = 0.5)
plt.legend()
plt.title("Exellence technologies")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()