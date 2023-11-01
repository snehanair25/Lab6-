#Sneha Nair


def encoder(pass_string):
    encodedlst = []
    for element in pass_string:
        nums = int(element) + 3
        encodedlst.append(nums)
    strresult = ""
    for ele in encodedlst:
        strresult += str(ele)
    return strresult



def main():
     while True:
      print("Menu")
      print("\n------------")
      print("1. Encode")
      print("2. Decode")
      print("3. Quit")

      user_option = int(input("Please enter an option: "))
      if user_option == 3:
          break
      elif user_option == 1:
          pass_string = input("Please enter your password to encode:  ")
          encoded_string = encoder(pass_string)
          print("Your password has been encoded and stored!")
      else:
          print("The encoded password is" + " " + encoded_string + " " +  "," + " " + "and the original password is" )




if __name__ == "__main__":    main()
