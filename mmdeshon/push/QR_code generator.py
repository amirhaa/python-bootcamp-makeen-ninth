from make_user import create_user
import qrcode
user_detail = create_user()
image = qrcode.make(f"Name is: '{user_detail[0]}'\nUsername is '{user_detail[1]}'\nUserID is '{user_detail[2]}'")
type(image)
image.save("User_Details.png")
