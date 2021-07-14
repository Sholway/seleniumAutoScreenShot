# -*- coding: utf-8 -*-
#
  
from selenium import webdriver
import time
  
  
def capture(url, save_fn="C:\\Users\\X\\Desktop\\crossdomain.png"):
  browser = webdriver.Firefox() # Get local session of firefox
  browser.set_window_size(900, 500)
  browser.get(url) # Load page
  browser.execute_script("""
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);
  
      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }
  
      setTimeout(f, 1000);
    })();
  """)
  
  for i in range(1):
    if "scroll-done" in browser.title:
      break
    time.sleep(3)
  
  browser.save_screenshot(save_fn)
  print ("ScreenShot Done in Desktop\crossdomain.png")
  browser.close()
  
  
if __name__ == "__main__":
  url=input("Input Url:")
  url=url.strip()
  url=url+"crossdomain.xml"
  print ('你的url:'+url)
  capture(url)
  time.sleep(30)
  