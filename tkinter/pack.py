from tkinter import *
'''pack篇'''
'''pack是布局管理器，可以视为一个弹性的容器'''
#-*- coding:utf-8 -*-

root = Tk()
'''
# 查看当前root下的子组件，解释器没有报异常说明pack已经创建，并可以使用，此时输出为空，root没有任何子组件
print(root.pack_slaves()) # 空的 列表 []

# 向root中pack一个Label
Label(root, text='pack').pack()

# 打印出子组件，此时存在创建的Label
print(root.pack_slaves())   # [<tkinter.Label object .!label>]
root.mainloop()
# 总结：pack_slave可以查看当前组件拥有的子组件，查看包含关系 
'''

# 改变root的大小为 80 * 80
root.geometry('80x80') # +0+0 是把窗体放在windos窗体的(0,0)处  此处的称号是x  不是*
print(root.pack_slaves())
# for i in range(5):
#     Label(root, text='pack'+str(i)).pack()
Label(root, text='pack1', bg='red').pack(fill=Y)
Label(root, text='pack2', bg='blue').pack(fill=BOTH)
Label(root, text='pack3', bg='green').pack(fill=X)
print(root.pack_slaves())
root.mainloop()