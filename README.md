# sqlitenote
利用sqlite文件数据库存储笔记内容的应用(sqlitenote)

  ![Image text](https://github.com/maytom2016/sqlitenote/blob/master/ui.png)
2021年7月18号更新，v105版本

BUG修复

1、调整保存机制，使得提示结果更加准确。

2、调整界面UI，避免笔记标签与标题重合。

3、优化删除功能，使得不再重复刷新列表。

4、优化新建、保存功能，当有新分类时，自动切换到新分类标签。

5、添加列表滚动条。

1. Adjust the saving mechanism to make the prompt results more accurate

2. Adjust the UI of the interface to avoid the overlap between note labels and titles.

3. optimize the deletion function, so that no longer refresh the list repeatedly.

4. Optimize the new and save functions. When there is a new category, it will automatically switch to the new category label

5. Add a list scrollbar.

##############################################################
2020年3月1号更新，v104版本
新增列表菜单，包括新建、保存、删除、导入、导出、打开其他数据库

New list menu, including new, save, delete, import, export, open other databases

功能修复如下：

Features are fixed as follows:

优化新增、保存、删除功能，使得不会出现不必要的刷新列表

Optimized new, save, and delete functions so that unnecessary refresh lists do not appear

优化退出时检测是否需要保存功能，避免不必要的询问

Optimize the detection of saving function when exiting, avoid unnecessary inquiries

##############################################################

2019年11月20号更新，v103版本

Updated November 20, 2019, v103 version

上一个版本很多问题，所以没过几天就更新了。主要改动如下：

There was a lot of problems with the previous version, so it was updated in a few days. The main changes are as follows:

1、点完保存，还是会弹出没有保存的菜单      解决

1. After saving, it will pop up a menu without saving.

2、笔记分类组合框下拉的范围太短，要加长。  解决

2. The range of the drop-down list of the note classification combo box is too short and needs to be lengthened. 

3、没有复制粘贴的按钮。                  解决

3. There is no copy and paste button. 

4、保存刷新列表问题。                    暂时还原

4. Save the refresh list problem. Temporary restoration

5、文字计数没有通过打开文件进行动态变化。  解决

5. The text count does not change dynamically by opening the file. solve

6、增加右键菜单

6. increase the right-click menu

想要功能很多，时间总是很少，下面是想要做的功能列表，下一次如果有更新就做。

Want to have a lot of features, time is always very small, the following is a list of features you want to do, the next time you have an update.

1、窗口不能放大缩小，没有进行分辨率适配。 
2、搜索笔记（标题）功能。

1, the window can not be zoomed in and out, no resolution adaptation.
2. Search for notes (title) function.

##############################################################

2019年11月6号更新，v102版本

Updated November 6, 2019, version v102

主要变动，1.加入未保存文件进行提醒。

Main changes: 1. Add unsaved files to remind.

2.修复保存文件时不必要的更新列表。

2. Repair the list of unnecessary updates when saving files.

下一步可能做的功能，右键菜单，包括复制、粘贴、撤销等等。

Next possible functions, right-click menu, including copy, paste, undo, etc.

虽然用键盘crtl +cvz 都可以办到，但是还是做一下吧！

Although it can be done with crtl + cvz, let's do it!

##############################################################

由于不喜欢很多txt文件占用我的桌面，所以想用一个文件来存储其中的数据，组装了这个程序，功能十分简单，应该有很多BUG，不过谁在乎呢？现在就我自己用，
发现一个就改一个吧！

Because I hate many txt files occupy my desktop,I packaging this program for saving all data in a file.There are many bugs on this program.But who cares about it.Anyway,I'm alone useing it.If i found a bug,I will repair it.


我要特别感谢CSDN的技术大佬们，尤其是 (欧程)，复制粘贴在改改就很舒服。
https://blog.csdn.net/wlsyn/article/details/49762407

I'm so grateful to  CSDN's Blogger,Especially oucheng.Copy、Paste and Fix it, easier.
