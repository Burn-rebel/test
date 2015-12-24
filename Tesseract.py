'''
Created on Dec 2, 2015

@author: burn
'''
# type into textfield -> click submit -> check toast message
def fill_sign_up_field_and_check_error(self, selector_name, to_type, error_msg):
        self.pageLib.find_and_type(self.accLib.get_selector(selector_name), to_type, clear = False, click_search = False)
        thread.start_new_thread(self.pageLib.take_multiple_screenshots, (4, 0.3, 1), {})
        self.pageLib.find_and_click(self.accLib.get_selector("sign_up_button"), pause_after_found = 1)
        self.pageLib.set_pause(2)
        if not self.pageLib.recognize_text_on_multiple_screenshots(4, error_msg):
            return "e > Error message '" + error_msg + "' is not present when '" + selector_name + "' field is filled with '" + to_type + "' and form is submitted\n"      
        return "" 
# take multiple screenshots in order to catch the error on the screen
def take_multiple_screenshots(self, circles, pause_between_circles, pre_pause = 0):
        if pre_pause != 0:
            self.set_pause(pre_pause, print_msg = True)
        for scr_num in range(circles):
            self.save_screenshot(pic_location = "../../screenshots", title = "rec_" + str(scr_num))
            self.set_pause(pause_between_circles, print_msg = False)
        return None
    def recognize_text_on_multiple_screenshots(self, circles, text):
        for scr_num in range(circles):
            self.write_to_console("> [is_text_present_on_screen] scanning: try " + str(scr_num + 1) + "/" + str(circles), no_new_line = True)
            if text in self.recognize_text_on_pic(pic_location = "../../screenshots/rec_" + str(scr_num) + ".png", print_scanned_text = False):
                self.write_to_console("[+]")
                return True
            self.write_to_console("[-]")
        return False
    def recognize_text_on_pic(self, pic_location = None, print_scanned_text = True): 
        im = Image.open(pic_location)
        im = im.convert('RGB') # convert to RGB
        im.save(pic_location)
        rec_text = pytesseract.image_to_string(Image.open(pic_location), lang = "eng") # recognize
        if print_scanned_text: # print
            self.write_to_console("----- ----- Recognized text ----- -----\n")
            self.write_to_console(rec_text)
            self.write_to_console("\n----- ----- ----- ----- ----- -----")
        return rec_text