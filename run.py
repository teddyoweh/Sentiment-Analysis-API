
  
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddyoweh@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Questions.
import os
from app import main


#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	main.run(host='0.0.0.0', port=port)
 