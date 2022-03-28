from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time

class sony_remote:
  
  def __init__(self, start_frame_dur, pause_frame_dur, one_frame_dur, zero_frame_dur, on_duty, off_duty):
    self.start_frame_dur = start_frame_dur
    self.pause_frame_dur = pause_frame_dur
    self.one_frame_dur = one_frame_dur
    self.zero_frame_dur = zero_frame_dur
    self.on_duty = on_duty
    self.off_duty = off_duty
  
  def start_sending(self):
    PWM0.duty(self.on_duty)
    time.sleep_us(self.start_frame_dur)
    PWM0.duty(self.off_duty)
  
  def send_bin_dataframe(self, data_frame):
    for i in data_frame:
      # There is a pause, then the value
      PWM0.duty(self.off_duty)
      time.sleep_us(self.pause_frame_dur)
      
      if i == '0':
        PWM0.duty(self.on_duty)
        time.sleep_us(self.zero_frame_dur)
        PWM0.duty(self.off_duty)
      elif i == '1':
        PWM0.duty(self.on_duty)
        time.sleep_us(self.one_frame_dur)
        PWM0.duty(self.off_duty)


setScreenColor(0x111111)

app_title = M5Title(title="TV-B-Gone", x=3, fgcolor=0x110c0c, bgcolor=0xff9800)
inst_btn = M5Rect(34, 67, 67, 67, 0x2472ac, 0xcc9912)
pressme = M5TextBox(35, 92, "Press M5", lcd.FONT_Default, 0xFFFFFF, rotate=0)

#sony_tv_toggle_code = list(str(101010010000))
sony_device1 = sony_remote(2400, 500, 1200, 600, 40, 100)
sony_40khz = {'tv':list(str(101010010000)), 'radio':list(str(101010000001))}


def toggle_sony(dataframe_dict):
  global sony_device1
  for key, val in dataframe_dict.items():
    for i in range(3):
      sony_device1.start_sending()
      sony_device1.send_bin_dataframe(val)
      time.sleep_ms(25)


def makegone():
  global sony_40khz
  toggle_sony(sony_40khz)


def buttonA_wasPressed():
  inst_btn.setBgColor(0xff0000)
  pressme.setColor(0x66ffff)
  pressme.show()
  makegone()
  pass
btnA.wasPressed(buttonA_wasPressed)


def buttonA_wasReleased():
  inst_btn.setBgColor(0x2472ac)
  pressme.setColor(0xffffff)
  pressme.setText("Press M5")
  pressme.show()
  pass
btnA.wasReleased(buttonA_wasReleased)

IR_PIN = machine.Pin(9, mode=machine.Pin.OUT)
PWM0 = machine.PWM(IR_PIN, freq=40000, duty=100, timer=0)
