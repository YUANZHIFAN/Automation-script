#!/usr/bin/env python
# -- coding: utf-8 --
import os
import time
import threading

now1 = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
androidlog = '' + now1 + 'androidlog.txt'
apk_name = raw_input("your apk name: \n")
# check the input value
while True:
    seed_num = raw_input('How many pseudo random seed(-s) do you want?\nenter int num(>0):')
    if seed_num.isdigit() and int(seed_num) > 0:
        print 'OK, your seed number are: ' + seed_num
        break
    else:
        print 'Please enter a number and the number > 0'
# check the input value
while True:
    events_num = raw_input('how many monkey events do you want\nevents(>0):')
    if events_num.isdigit() and int(events_num) > 0:
        print 'OK, you want to loop ' + events_num + 'times monkey test'
        break
    else:
        print 'Please enter a number and the number > 0'
# the log path
log_path = '/sdcard/'
# the log name
log_name = '' + now1 + 'monkey.txt'
log_name2 = '' + now1 + 'android.txt'

# monkey shell script
monkey_shell = 'adb  shell monkey -v -v -v -p ' + apk_name + ' -s ' + seed_num + ' ' \
                                                                                 '--ignore-crashes --ignore-timeouts --kill-process-after-error --pct-touch 100 ' \
                                                                                 '--pct-syskeys 0 --pct-motion 0 --pct-trackball 0  --throttle 100 --randomize-throttle ' + events_num + ' >' + log_path + '' + log_name + ''
monkey_shell_2 = 'adb  shell monkey -v -v -v -p ' + apk_name + ' -s ' + seed_num + ' ' \
                                                                                 '--throttle 100 --randomize-throttle ' + events_num + ' >' + log_path + '' + log_name + ''
logcat1 = 'adb logcat CrashReport:E AndroidRuntime:E ActivityManager:E *:s | findstr ' + apk_name + ' > ' + log_path + '' + log_name2 + ''


# logcat2 = 'adb -s 192.168.68.102:5555 logcat CreashReport:E AndroidRuntime:E ActivityManager:E *:s | findstr '+apk_name+' > '+log_path+''+log_name3+''
def adblogcat():
    device = os.popen('adb devices').read()
    if device.strip().endswith('device'):
        os.system('adb start-server')
        os.system(logcat1)
    else:
        print 'check your phone  has linked your computer well '
    return
monkey = dict(i='' + monkey_shell + '', a=''+monkey_shell_2+'')
while True:
    monkey_type = raw_input('which apk do you want to test?\n(\'i\' or \'a\'):')
    try:
        monkey_num = monkey[monkey_type]
    except KeyError:
        print 'Please enter \'i\' or \'a\'! - -#'
    else:
        break

def monkeytest():
    #    print 'now let\'s check your phone'
    phonedevice = os.popen('adb devices').read()
    if phonedevice.strip().endswith('device'):
        os.system(''+monkey_num+'')
#       os.system('adb kill-server')
        os.system('adb reboot')
    else:
        print 'please check your phone has linked your computer well'
    return()
def run():
    threads = []
    t1 = threading.Thread(target=adblogcat)
    threads.append(t1)
    t2 = threading.Thread(target=monkeytest)
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    return

# find 'adb' command at your os

sysPath = os.environ.get('PATH')
if not sysPath.find('platform-tools'):
    print '''please install the android-sdk and put the 'platform-tools' dir in your system PATH'''
else:
    # kill the 'tadb.exe'
    tadb = os.popen('tasklist').read()
    if tadb.find('tadb.exe') != -1:
        print 'Find \'tadb.exe\', it must be killed!!!!!!'
        os.system('taskkill /im tadb.exe /F')
        print 'OK,the \'tadb.exe\' has been killed, let\'s go on'
        run()
        '''
        for t in threads:
            t.setDaemon(True)
            t.start()
        '''
    else:
        print 'not find \'tadb.exe\',great! go on!'
        '''
        for t in threads:
            t.setDaemon(True)
            t.start()
        '''
        run()

print 'pls enter something to close this table'
raw_input("anything")

