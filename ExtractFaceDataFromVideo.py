import cv2

#parent directory

Parent = "C:/Users/Hameed/Documents/GitHub/Flames/note4/Persons-Name-Identification-using-python-opencv"
  
print("Please enter your name >")
#take user name as input to create a directory on person name
SubDirectoryName = str(input())
# Path for subdirectory
#path = os.path.join(Parent, ) 
cap= cv2.VideoCapture(Parent+'/'+SubDirectoryName+'.avi')
i=0
c=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if c % cap.get(cv2.CAP_PROP_POS_FRAMES)==0 :
     #cv2.imwrite(SubDirectoryName+str(i)+'.jpg',frame)
     c+=1
    i+=1

cap.release()
cv2.destroyAllWindows()