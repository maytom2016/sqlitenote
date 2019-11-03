import sqlite3
import time
import tkinter.messagebox
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import os
#import sys

# 数据库文件绝句路径
#DB_FILE_PATH = 'c:\\test.db'
DB_FILE_PATH=os.path.expanduser('~')+'\sqlitenotes\\default.db'

# 表名称
TABLE_NAME = 'notes'
def getid():   #获取当前选择的ID
    nowselection = lb.get(lb.curselection())
    dhlo = nowselection.find(',')
    return int(nowselection[0:dhlo])

def creattable(DB_FILE_PATH1):
    # 数据库
    create_table_sql = '''CREATE TABLE `notes` (
                              `id` int(11) NOT NULL,
                              `created time` varchar(30) NOT NULL,
                              `modify time` varchar(30) DEFAULT NULL,
                               classify varchar(30) DEFAULT NULL,
                              `title` varchar(30) DEFAULT NULL,
                              `content` varchar(20000) DEFAULT NULL,
                               PRIMARY KEY (`id`)
                            )'''
    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    cu.execute(create_table_sql)
    conn.commit()
    cu.close()


def getnow():
    print (time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())))

def newnote():
    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    select_sql='''SELECT ID FROM notes'''
    cu.execute(select_sql)
    r = cu.fetchall()
    if r:
     str1 = str(max(r))
     str1=str1.replace('(','').replace(',)','')
     newid=int(str1)+1
    else:
        newid=1

    if ( players.get() == "all"):
        classify1 = "default"
    else:
        classify1 = players.get()
    data =[(newid,time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())),time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())),classify1,text1.get("1.0","end"),text.get("1.0","end")),]
    label2.set(newid)
    save_sql = '''INSERT INTO notes values (?, ?, ?, ?, ?, ?)'''
    for d in data:
     cu.execute(save_sql, d)
     conn.commit()
    cu.close()
    combboxreflash()
    combbox_click()

def updatetc():
   update_sql = 'UPDATE notes SET [modify time]= ?,classify = ?,title= ? ,content= ? WHERE ID = ? '
   if (players.get() == "all"):
       classify1 = "default"
   else:
       classify1 = players.get()

   if (label2.get()!='0'):
    data = (time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())),classify1,text1.get("1.0","end"),text.get("1.0","end"),label2.get())


    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    cu.execute(update_sql,data)
    conn.commit()
    cu.close()
    combboxreflash()
    combbox_click()



def loadcontent(*args): #ID+title
  if lb.curselection():
    nowselection=lb.get(lb.curselection())
    dhlo= nowselection.find(',')
    databaseid=int(nowselection[0:dhlo])
    label2.set(databaseid)

    data=(databaseid,)
    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    select_sql ='SELECT title FROM notes WHERE ID = ? '
    cu.execute(select_sql,data)
    r = cu.fetchall()
    title1=str(r).replace('[(\'','').replace('\',)]','').replace('\\n', '')
    text1.delete(0.0, END)
    text1.insert(0.0,title1)
    select_sql='SELECT content FROM notes WHERE ID = ? '
    cu.execute(select_sql, data)
    r = cu.fetchall()
    content = str(r).replace('[(\'', '').replace('\',)]', '').replace('\\n', '\n')
    text.delete(0.0, END)
    text.insert(0.0, content)
    cu.close()
def combbox_click(*args):
  if(players.get()!="all"):
    lb.delete(0, END)
    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    sql= '''SELECT ID,title FROM notes where classify = \"'''+ players.get()+'\"'
    cu.execute(sql)
    r = cu.fetchall()
    for n in r:
        string1 = str(n).replace(', \'', ',').replace('\'', '').replace('\\n', '').replace('(', '').replace(')', '')
        lb.insert('end', string1)
    cu.close()
  else:
      loadalltitle()
def loadalltitle():
    lb.delete(0, END)
    sql = '''SELECT ID,title FROM notes'''
    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    cu.execute(sql)
    r = cu.fetchall()
    for n in r:
        string1 = str(n).replace(', \'', ',').replace('\'', '').replace('\\n', '').replace('(', '').replace(')', '')
        lb.insert('end', string1)
    cu.close()
def deletenowselection():
    sql='''DELETE FROM notes WHERE id= ?'''
    print(label2.get())
    if (lb.curselection()):
      nowselection = lb.get(lb.curselection())
      dhlo = nowselection.find(',')
      databaseid = int(nowselection[0:dhlo])
      data=(label2.get(),)
      conn = sqlite3.connect(DB_FILE_PATH)
      cu = conn.cursor()
      cu.execute(sql,data)
      conn.commit()
      cu.close()
      combboxreflash()

      combbox_click()
      if(lb.get(0)==""):
         players.current(0)
         combbox_click()
      print(lb.get(0))

    else:
        tkinter.messagebox.showinfo('提示', '没选中要删除的笔记')


        # print("呵呵")
        # print(os.path.dirname(os.path.realpath(__file__)))
        # print(os.path.realpath(__file__))
        #print (os.path.expanduser('~'))  引用用户根目录
        #print(os.path.expanduser('~')+'\sqlitenotes\\default.db')

def databaseexist():
    sql='''select count(*)  from sqlite_master where type='table' and name = 'notes';'''

    if not os.path.exists(os.path.dirname(DB_FILE_PATH)):
        os.mkdir(os.path.dirname(DB_FILE_PATH))

    conn = sqlite3.connect(DB_FILE_PATH)
    cu = conn.cursor()
    cu.execute(sql)
    r = cu.fetchall()
    if(r==[(0,)]):
        creattable(DB_FILE_PATH)
    # else:
    #     print("不用建立表")
def ontextchange(*args):
     str1=str(len(text.get("1.0","end"))-1)
     label3.set('2W/'+str1)
     print(text.get("1.0","end"))

def combboxreflash():
     conn = sqlite3.connect(DB_FILE_PATH)
     cu = conn.cursor()
     cu.execute(sql)
     cu.execute(sql0)
     r = cu.fetchall()
     sf = ["all"] + r
     players["values"] = sf

mygui = Tk(className="sqlite笔记V1.0")
mygui.geometry('900x600')
mygui.resizable(0, 0)        # 禁止调整窗口大小
#文本框title
text1=Text(mygui, width=20, height=1,font=("隶书",18))
text1.place(x=300,y=25)


#文本框content

text=scrolledtext.ScrolledText(mygui,width=62, height=21,font=("隶书",18))  #滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
text.place(x=130,y=70)
text.bind('<KeyRelease>',ontextchange)


#label提醒当前数据库文件位置
lb1=Label(mygui,text='当前数据库文件位置为'+DB_FILE_PATH)
lb1.place(x=130,y=0)
#label2提醒当前数据库文件位置
label2 = StringVar()
label2.set('0')
lb2=Label(mygui,text='0',textvariable=label2)
lb2.place(x=280,y=30)

#统计字数，以免字数过长无法保存
label3 = StringVar()
label3.set('2W/0')
la=Label(mygui,text='2W/0', textvariable=label3)
la.place(x=520,y=0)

#列表1
lb = Listbox(mygui, listvariable="qwe",width=17,height=31)  # 实例化一个Listbox/listvariable指定列表内容
#lb.bind('<Double-Button-1>',loadcontent)
lb.bind('<Double-Button-1>',loadcontent)
lb.place(x=0,y=25)

databaseexist()

sql0='''select distinct classify from notes;'''
sql = '''SELECT ID,title FROM notes'''
conn = sqlite3.connect(DB_FILE_PATH)
cu = conn.cursor()
cu.execute(sql)
r = cu.fetchall()
for n in r:
    string1 = str(n).replace(', \'', ',').replace('\'', '').replace('\\n', '').replace('(', '').replace(')', '')
    lb.insert('end', string1)
#组合框
players = ttk.Combobox(mygui, textvariable="abc",width=15,height=1)
cu.execute(sql0)
r = cu.fetchall()
sf=["all"]+r
players["values"] = sf
#players["state"] = "readonly"
players.current(0)
players.bind("<<ComboboxSelected>>", combbox_click)
players.place(x=0,y=0)


cu.close()



#按钮1新建
bt=Button(mygui,text='新建',width=4,height=1,command = newnote)
bt.place(x=130,y=25)
#按钮2保存
bt2=Button(mygui,text='保存',width=4,height=1,command = updatetc)
bt2.place(x=175,y=25)
#按钮3删除
bt3=Button(mygui,text='删除',width=4,height=1,command = deletenowselection)
bt3.place(x=220,y=25)

mainloop()
