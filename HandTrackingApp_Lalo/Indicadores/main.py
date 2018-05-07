
from DrawingFunctions import *

# scr = cv2.imread('../Images/kd1.png')
scr = cv2.imread('../Images/kd4.jpg')

out, area = UsedSpace(scr)

centroids = MassCenter(scr, out)

cv2.waitKey(0)

cv2.destroyAllWindows()
