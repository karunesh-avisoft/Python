try:
  f = open("demofile.txt",'r')
  try:
    f.write("Lorum Ipsum")
  except:
    print("Unknown error occurred!")
  finally:
    f.close()
    print("Closed the file & stopped!")
except FileNotFoundError:
  print('FileNotFound:FIle not found!!')
except:
  print("Unknown:Something went wrong when opening the file!")  
finally:
  print('\n\tDONE\n')
  
