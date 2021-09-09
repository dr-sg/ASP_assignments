N = 64
k0 = 2
x = np.cos(2*np.pi*k0/N*np.arange(N)) # signal in time domain

X = []  # dft - initially empty
nv = np.arange(-N/2,N/2)
kv = np.arange(-N/2,N/2)

for k in kv:
    s = np.cos(2*np.pi*k/N*np.arange(N))
    dot_product = sum(x*np.conjugate(s))
    # print(abs(dot_product), end=' | ')
    X = np.append(X, dot_product)

plt.plot(kv, abs(X))
# plt.plot(nv, x)
plt.axis([-N/2, N/2-1, 0, N/2])
# plt.axis([-N/2, N/2-1, -1, 1])
plt.show()