from AOLME import *
img = read_img("head.jpg")
save_img(img, "head2.jpg")

show_img(img)
show_comps(img)
print("image size=", img_size(img))

show_img(img)
rotate_img(img, 90)

color = get_pixel(img, [0, 0])
print(color)

put_pixel(img, [0, 0], [0, 0, 0])
color = get_pixel(img, [0, 0])
print(color)

pixel_range = [0, 100, 0, 100]
put_pixel_group(img, pixel_range, [0, 0,0])
show_img(img)

print("Click on the last image and then press any key to close all windows")
cv2.waitKey()
cv2.destroyAllWindows()
