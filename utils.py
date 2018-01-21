import cv2

def BGR2Gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def showImg(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showImgNb(img):
    if len(img.shape) == 3: # BGR img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
    else: # grayscale
        plt.imshow(img, cmap='gray' ) #, interpolation='bicubic')
    plt.show()

def saveImg(file,img):
    cv2.imwrite(file,img)

def showImgNb(img):
    if len(img.shape) == 3: # BGR img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    io.imshow(img)

def computeHistogram(gray_img):
    hist = np.bincount(gray_img.ravel(),minlength=256)
    return hist

def autoThreshold(gray_img):
    hist = computeHistogram(gray_img)
    T = int(round( np.sum(hist * np.arange(256))/np.sum(hist) ))
    oT = T # old T value
    iteration_count = 0

    while True:
        iteration_count += 1
        r1 = np.sum(hist[:T] * np.arange(256)[:T]) / np.sum(hist[:T])
        r2 = np.sum(hist[T:] * np.arange(256)[T:]) / np.sum(hist[T:])
        oT, T = T, int(round( (r1+r2)/2 ))
        if oT == T:
            break
    print(f"debug: run {iteration_count} times")
    return T

def createVideo():
    new_video = []
    for img in videodata:
        img = RGB2BGR(img)
        g_img = BGR2Gray(img)
        gbA_img = cv2.GaussianBlur(g_img, (7,7), 1.1)
        new_video.append(gbA_img)

    new_video = np.stack(new_video)
    new_video.shape

    new_video = new_video.astype(np.uint8)
    skvideo.io.vwrite("5x5video.mp4", new_video)

def Gaussian_Mask(kernlen=7, nsig=1):

    # index creation
    minusN = int(-(kernlen-1)/2)
    plusN = int((kernlen-1)/2)
    i = j = np.arange(minusN,plusN+1)
    ii, jj = np.meshgrid(i,j)

    gm = np.power(np.e,-(np.power(ii,2)+np.power(jj,2))/(2*np.power(nsig,2)))
    gnn = np.full(gm.shape,gm.min())
    Gm_pos = np.round(gm/gnn)
    Gm = Gm_pos/np.sum(Gm_pos)

    return Gm

def applyGaussianFilter(g_img,kernsize,sd):
    padsize = int((kernsize-1)/2)
    kern = Gaussian_Mask(kernsize, sd)
    getpadsize = lambda x: ((x,x),(x,x))
    pad_img = np.pad(g_img, getpadsize(padsize), 'edge')

    def getPadCoor(x,y):
        return x+padsize, y+padsize
    def getImagePart(pad_img,xy,padsize):
        x, y = xy
        return pad_img[y-padsize : (y+padsize+1) , x-padsize : x+padsize+1]
    Y,X = g_img.shape


    lst_img = []
    for y in range(Y):
        row_img = []
        for x in range(X):
            s = np.sum(kern * getImagePart(pad_img,getPadCoor(x,y),padsize))
            row_img.append(s)
        lst_img.append(row_img)
    new=np.array(lst_img)
    return new

def compareImgNb(img1,img2,x):
    img[]
