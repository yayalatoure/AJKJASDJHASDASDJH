
from DrawingFunctions import *

# ch = 's'

# while (ch != 'q' and ch != 'Q'):

    # Recorre carpeta completa y anda revisando
src = cv2.imread('/home/lalo/Dropbox/Proyecto_Dibujos/Dibujos/Test 2/1 MEDIO - 13.jpg')

out, area = UsedSpace(src)
# centroids = MassCenter(src, out)

cv2.waitKey(0)




cv2.destroyAllWindows()
